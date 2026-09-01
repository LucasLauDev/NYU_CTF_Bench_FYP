#!/usr/bin/env python3
"""
Script to count CTF challenges in selected-benchmarks that do NOT have a docker-compose file
or do NOT use Docker containers, broken down by category.
"""

import os
import sys
import json
from collections import defaultdict

def count_non_docker_challenges(benchmarks_dir: str):
    if not os.path.exists(benchmarks_dir):
        print(f"Error: Directory '{benchmarks_dir}' does not exist.")
        sys.exit(1)

    challenge_dirs = []
    # Identify all challenge root directories by locating challenge.json
    for root, dirs, files in os.walk(benchmarks_dir):
        if 'challenge.json' in files:
            challenge_dirs.append(root)

    docker_challenges = []
    non_docker_challenges = []

    category_total = defaultdict(int)
    category_docker = defaultdict(int)
    category_no_docker = defaultdict(int)

    for cd in sorted(challenge_dirs):
        rel_path = os.path.relpath(cd, benchmarks_dir)
        
        # Determine category from challenge.json or path hierarchy
        category = 'unknown'
        json_path = os.path.join(cd, 'challenge.json')
        if os.path.exists(json_path):
            try:
                with open(json_path, 'r', encoding='utf-8') as f:
                    cdata = json.load(f)
                    category = cdata.get('category', '').lower()
            except Exception:
                pass
        
        if not category or category == 'unknown':
            parts = rel_path.split(os.sep)
            category = parts[2] if len(parts) >= 3 else 'unknown'

        has_compose = False
        has_dockerfile = False
        
        for r, dirs, files in os.walk(cd):
            for f in files:
                f_lower = f.lower()
                if 'docker-compose' in f_lower and (f_lower.endswith('.yml') or f_lower.endswith('.yaml')):
                    has_compose = True
                if f_lower == 'dockerfile':
                    has_dockerfile = True

        category_total[category] += 1

        if has_compose or has_dockerfile:
            docker_challenges.append((category, rel_path))
            category_docker[category] += 1
        else:
            non_docker_challenges.append((category, rel_path))
            category_no_docker[category] += 1

    print("=" * 70)
    print("                 CTF CHALLENGE DOCKER SUMMARY                 ")
    print("=" * 70)
    print(f"Base Directory                           : {os.path.abspath(benchmarks_dir)}")
    print(f"Total Challenges Found                   : {len(challenge_dirs)}")
    print(f"Challenges with Docker / Docker Compose  : {len(docker_challenges)}")
    print(f"Challenges WITHOUT Docker / Compose      : {len(non_docker_challenges)}")
    print("=" * 70)

    print("\n" + "=" * 70)
    print("               CATEGORY BREAKDOWN FOR DOCKER USAGE              ")
    print("=" * 70)
    print(f"{'Category':<15} | {'Total':<10} | {'With Docker':<15} | {'Without Docker':<15}")
    print("-" * 70)
    for cat in sorted(category_total.keys()):
        tot = category_total[cat]
        doc = category_docker[cat]
        nodoc = category_no_docker[cat]
        print(f"{cat:<15} | {tot:<10} | {doc:<15} | {nodoc:<15}")
    print("=" * 70)

    if non_docker_challenges:
        print("\n[List of Challenges Without Docker / Compose]")
        for idx, (cat, path) in enumerate(non_docker_challenges, 1):
            print(f" {idx:2d}. [{cat}] {path}")
    else:
        print("\nAll challenges are dockerized!")

    return len(challenge_dirs), len(docker_challenges), len(non_docker_challenges)

if __name__ == '__main__':
    default_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'selected-benchmarks')
    target_dir = sys.argv[1] if len(sys.argv) > 1 else default_dir
    count_non_docker_challenges(target_dir)
