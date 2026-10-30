FROM ubuntu:22.04

# Install runtime dependencies (OpenSSL 3 and zlib)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libssl3 \
    zlib1g \
    ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the challenge binary
COPY nervcenter .
RUN chmod +x nervcenter

# Expose control port and session sensor port pool
EXPOSE 2000
EXPOSE 2001-2050

CMD ["./nervcenter"]

