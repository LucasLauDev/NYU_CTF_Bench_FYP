import os
import json
import re
from collections import defaultdict

benchmarks_dir = os.path.abspath('selected-benchmarks')

challenge_dirs = []
for root, dirs, files in os.walk(benchmarks_dir):
    if 'challenge.json' in files:
        challenge_dirs.append(root)

print(f"==================================================")
print(f"BENCHMARK COMPREHENSIVE ANALYSIS")
print(f"Base Directory: {benchmarks_dir}")
print(f"Total Challenges Found (by challenge.json): {len(challenge_dirs)}")
print(f"==================================================")

data = []
categories = defaultdict(int)
events = defaultdict(int)
years = defaultdict(int)

# Breakdown structures
cat_docker_summary = defaultdict(lambda: {
    'total': 0,
    'has_dockerfile': 0,
    'has_compose': 0,
    'has_any_docker': 0,
    'no_docker': 0,
    'with_network_port': 0,
    'docker_no_network_port': 0
})

no_docker_list = []
docker_no_ports_list = []
docker_with_ports_list = []

for cd in sorted(challenge_dirs):
    rel = os.path.relpath(cd, benchmarks_dir)
    parts = rel.split(os.sep)
    year = parts[0] if len(parts) > 0 else 'Unknown'
    event = parts[1] if len(parts) > 1 else 'Unknown'
    cat_dir = parts[2] if len(parts) > 2 else 'Unknown'
    chal_name = parts[3] if len(parts) > 3 else parts[-1]
    
    # Read challenge.json
    cjson = {}
    try:
        with open(os.path.join(cd, 'challenge.json'), 'r', encoding='utf-8') as f:
            cjson = json.load(f)
    except Exception as e:
        pass
        
    cat = cjson.get('category', cat_dir).strip().lower()
    # Normalize category names if any (e.g. rev -> reverse engineering, pwn -> pwn / binary exploitation, etc.)
    categories[cat] += 1
    events[f"{year}/{event}"] += 1
    years[year] += 1
    
    # Find all docker related files
    dockerfiles = []
    compose_files = []
    for r, d, files in os.walk(cd):
        for f in files:
            fpath = os.path.join(r, f)
            if f.lower() == 'dockerfile' or f.lower().startswith('dockerfile.'):
                dockerfiles.append(fpath)
            if 'docker-compose' in f.lower() and (f.lower().endswith('.yml') or f.lower().endswith('.yaml')):
                compose_files.append(fpath)
                
    has_df = len(dockerfiles) > 0
    has_dc = len(compose_files) > 0
    has_docker = has_df or has_dc
    
    # Check for exposed ports in Dockerfiles and compose files
    exposed_ports = []
    
    for df in dockerfiles:
        try:
            with open(df, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Check EXPOSE
                for match in re.findall(r'^\s*EXPOSE\s+([0-9\s/a-zA-Z_-]+)', content, re.MULTILINE | re.IGNORECASE):
                    for p in match.split():
                        exposed_ports.append(f"Dockerfile EXPOSE {p.strip()}")
                # Also check if services like xinetd, socat, flask, etc. are launched with a port
                # But EXPOSE or compose ports are standard
        except Exception:
            pass
            
    for cf in compose_files:
        try:
            with open(cf, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                # Find ports block
                port_matches = re.findall(r'ports:\s*\n((?:\s*-\s*[^\n]+\n)+)', content, re.MULTILINE | re.IGNORECASE)
                for pm in port_matches:
                    for line in pm.strip().split('\n'):
                        p_val = line.strip().lstrip('-').strip().strip('"\'')
                        exposed_ports.append(f"Compose ports: {p_val}")
                # Expose block
                expose_matches = re.findall(r'expose:\s*\n((?:\s*-\s*[^\n]+\n)+)', content, re.MULTILINE | re.IGNORECASE)
                for em in expose_matches:
                    for line in em.strip().split('\n'):
                        p_val = line.strip().lstrip('-').strip().strip('"\'')
                        exposed_ports.append(f"Compose expose: {p_val}")
        except Exception:
            pass
            
    has_port = len(exposed_ports) > 0
    
    cat_summary = cat_docker_summary[cat]
    cat_summary['total'] += 1
    if has_df: cat_summary['has_dockerfile'] += 1
    if has_dc: cat_summary['has_compose'] += 1
    if has_docker:
        cat_summary['has_any_docker'] += 1
        if has_port:
            cat_summary['with_network_port'] += 1
            docker_with_ports_list.append((cat, rel, exposed_ports))
        else:
            cat_summary['docker_no_network_port'] += 1
            docker_no_ports_list.append((cat, rel, [os.path.relpath(p, cd) for p in dockerfiles + compose_files]))
    else:
        cat_summary['no_docker'] += 1
        no_docker_list.append((cat, rel))

print("\n--- 1. OVERALL TOTALS ---")
print(f"Total Challenges: {len(challenge_dirs)}")
total_docker = sum(c['has_any_docker'] for c in cat_docker_summary.values())
total_no_docker = sum(c['no_docker'] for c in cat_docker_summary.values())
total_with_port = sum(c['with_network_port'] for c in cat_docker_summary.values())
total_docker_no_port = sum(c['docker_no_network_port'] for c in cat_docker_summary.values())

print(f"Challenges with Docker (Dockerfile and/or Compose): {total_docker} ({total_docker/len(challenge_dirs)*100:.1f}%)")
print(f"Challenges WITHOUT Docker: {total_no_docker} ({total_no_docker/len(challenge_dirs)*100:.1f}%)")
print(f"Docker Challenges WITH Open/Exposed Network Port: {total_with_port} ({total_with_port/total_docker*100:.1f}% of docker chals)")
print(f"Docker Challenges WITHOUT Open/Exposed Network Port: {total_docker_no_port} ({total_docker_no_port/total_docker*100:.1f}% of docker chals)")

print("\n--- 2. CATEGORY BREAKDOWN ---")
print(f"{'Category':<16} | {'Total':<6} | {'Docker':<8} | {'No Docker':<10} | {'Port Open':<10} | {'Docker No Port':<14}")
print("-" * 75)
for cat in sorted(cat_docker_summary.keys()):
    c = cat_docker_summary[cat]
    print(f"{cat:<16} | {c['total']:<6} | {c['has_any_docker']:<8} | {c['no_docker']:<10} | {c['with_network_port']:<10} | {c['docker_no_network_port']:<14}")

print("\n--- 3. YEAR BREAKDOWN ---")
for y in sorted(years.keys()):
    print(f"{y}: {years[y]} challenges")

print("\n--- 4. EVENT BREAKDOWN ---")
for ev in sorted(events.keys()):
    print(f"{ev}: {events[ev]} challenges")

if no_docker_list:
    print(f"\n--- 5. LIST OF CHALLENGES WITHOUT DOCKER ({len(no_docker_list)}) ---")
    for idx, (cat, rel) in enumerate(no_docker_list, 1):
        print(f"  {idx:2d}. [{cat}] {rel}")

if docker_no_ports_list:
    print(f"\n--- 6. LIST OF DOCKER CHALLENGES WITHOUT OPEN NETWORK PORTS ({len(docker_no_ports_list)}) ---")
    for idx, (cat, rel, files) in enumerate(docker_no_ports_list, 1):
        print(f"  {idx:2d}. [{cat}] {rel} (Files: {', '.join(files)})")

