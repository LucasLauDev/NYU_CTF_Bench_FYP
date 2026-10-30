# NERV Center

> **Category:** Crypto / System  
> **Event:** CSAW CTF Finals 2023  
> **Author:** Brendan Dolan-Gavitt (`moyix`)  
> **Flag:** `csawctf{fly_m3_t0_th3_m00n_4nd_l3t_m3_h4ck_4mong_th3_st4rs}`  
> **Default Ports:** `2000` (Control Port) + `2001-2050` (Dynamic Session Sensor Ports)

---

## 1. Description & Connection Instructions

Get into the server, Shinji. Or Rei will have to do it again.

Connect to the control service via netcat:
```bash
nc localhost 2000
# or using the ctfnet alias:
nc nervcenter.moyix.net 2000
```

Upon connection, the server will display ASCII art and allocate a unique sensor port (e.g., `Session sensor port is: 2001`). Connect to that secondary port to manage sensor telemetry and trigger out-of-band data handling.

---

## 2. Docker Deployment & Environment Setup

This challenge is wrapped as a containerized service with custom networking and resource limits configured to support the low-level exploit.

### Launching the Service
```bash
# Build and run the container in background
docker compose up -d --build

# Inspect container status and logs
docker compose logs -f

# Tear down container
docker compose down
```

### Important Runtime Requirements
* **Port Range:** The service binds port `2000` for the control listener and allocates dynamic ports starting from `2001` (`SENSOR_PORT_BASE`) for sensor interactions. The `docker-compose.yml` maps `2000:2000` and `2001-2050:2001-2050`. (On Linux production hosts, `network_mode: "host"` may also be used).
* **Resource Limit (`nofile`):** The exploit requires holding open $>1024$ concurrent sockets. The container is configured with `ulimits.nofile` set to `2048` (soft/hard).

---

## 3. Vulnerability Mechanics & Technical Details

The way `select()` works is you create an `fd_set` and then add file descriptors to it using the `FD_SET()` macro. You can monitor the fds for read, write or exceptions (the last one in practice is only used to indicate TCP OOB data and some weird terminal conditions). Then you call select like:

```c
select(nfds, &readfds, &writefds, &exceptfds, &timeout);
```

And then when it returns you can check the sets using the `FD_ISSET()` macros to find out which fds are in which state.

But what is less well known (though it's documented in the man page) is that the max file descriptor you can monitor this way is hardcoded to `FD_SETSIZE`, which is 1024 – even though modern systems can have many more open files than that:

```
DESCRIPTION
       WARNING: select() can monitor only file descriptors numbers that are less
       than FD_SETSIZE (1024)—an unreasonably low limit for many modern applica‐
       tions—and this limitation will not change. All modern applications should
       instead use poll(2) or epoll(7), which do not suffer this limitation.
```

The `fd_set` struct is just a bitset of 1024 bits (128 bytes). Attempting to monitor fds larger than 1024 causes memory corruption by writing individual bits past the end of the bitset.

In the context of this network server:
1. By making a large number of connections (>1024) and managing their state using TCP Out-Of-Band (OOB) data (`exceptfds`), a client can control the bit pattern written past `fd_set`.
2. The bit corruption directly targets the RSA public key modulus ($N$) in memory.
3. Once specific bits in the modulus are perturbed, the modified key becomes factorable within seconds (e.g. via Pollard's rho / ECM / Brent's algorithm in `solver/`), allowing the attacker to decrypt the flag or forge administrative signatures.
