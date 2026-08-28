#!/usr/bin/env python3
"""
clean_dataset.py

Filters challenges from test_dataset.json in categories 'web', 'misc', and 'crypto',
copies them to a new 'selected-benchmark' folder, and prepares the corresponding
JSON dataset file for selected challenges.
"""

import argparse
import json
import logging
import os
import shutil
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("clean_dataset")

DEFAULT_CATEGORIES = ["web", "misc", "crypto"]
DEFAULT_SRC_JSON = "test_dataset.json"
DEFAULT_DEST_DIR = "selected-benchmarks"
DEFAULT_OUTPUT_JSON = "selected-benchmarks/selected_dataset.json"


def clean_and_select_dataset(
    src_json_path: str = DEFAULT_SRC_JSON,
    dest_dir_name: str = DEFAULT_DEST_DIR,
    output_json_path: str = DEFAULT_OUTPUT_JSON,
    categories: list = None,
):
    if categories is None:
        categories = DEFAULT_CATEGORIES

    target_categories = set(cat.lower() for cat in categories)
    src_json = Path(src_json_path).resolve()

    if not src_json.exists():
        logger.error(f"Source JSON file not found: {src_json}")
        raise FileNotFoundError(f"Source JSON file not found: {src_json}")

    workspace_dir = src_json.parent
    dest_dir = workspace_dir / dest_dir_name
    dest_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Loading dataset from {src_json}...")
    with open(src_json, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    selected_dataset = {}
    category_counts = {cat: 0 for cat in target_categories}

    logger.info(f"Filtering challenges in categories: {sorted(list(target_categories))}...")

    for key, challenge_info in dataset.items():
        category = challenge_info.get("category", "").lower()
        if category in target_categories:
            orig_path_str = challenge_info.get("path", "")
            src_challenge_path = (workspace_dir / orig_path_str).resolve()

            if not src_challenge_path.exists():
                logger.warning(f"Challenge folder not found at {src_challenge_path}, skipping {key}")
                continue

            # Determine relative subpath inside 'test' (or root)
            rel_path = Path(orig_path_str)
            if rel_path.parts and rel_path.parts[0] == "test":
                rel_path = Path(*rel_path.parts[1:])

            dest_challenge_path = dest_dir / rel_path

            # Copy challenge files
            dest_challenge_path.parent.mkdir(parents=True, exist_ok=True)
            if dest_challenge_path.exists():
                shutil.rmtree(dest_challenge_path)
            shutil.copytree(src_challenge_path, dest_challenge_path)

            # Build updated entry
            new_entry = dict(challenge_info)
            new_entry["path"] = (Path(dest_dir_name) / rel_path).as_posix()

            selected_dataset[key] = new_entry
            category_counts[category] += 1

    out_file = workspace_dir / output_json_path
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(selected_dataset, f, indent=2)

    logger.info("=== Cleaning & Dataset Generation Summary ===")
    logger.info(f"Total challenges selected: {len(selected_dataset)}")
    for cat, count in sorted(category_counts.items()):
        logger.info(f"  - {cat}: {count} challenges")
    logger.info(f"Destination folder created/updated: {dest_dir}")
    logger.info(f"JSON dataset file created: {out_file}")

    return selected_dataset


def main():
    parser = argparse.ArgumentParser(
        description="Extract web, misc, and crypto challenges from test_dataset.json into selected-benchmark folder."
    )
    parser.add_argument(
        "--src-json",
        default=DEFAULT_SRC_JSON,
        help="Path to source dataset JSON file (default: test_dataset.json)",
    )
    parser.add_argument(
        "--dest-dir",
        default=DEFAULT_DEST_DIR,
        help="Destination directory name (default: selected-benchmark)",
    )
    parser.add_argument(
        "--output-json",
        default=DEFAULT_OUTPUT_JSON,
        help="Output dataset JSON filename (default: selected_dataset.json)",
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        default=DEFAULT_CATEGORIES,
        help="Categories to filter (default: web misc crypto)",
    )

    args = parser.parse_args()

    clean_and_select_dataset(
        src_json_path=args.src_json,
        dest_dir_name=args.dest_dir,
        output_json_path=args.output_json,
        categories=args.categories,
    )


if __name__ == "__main__":
    main()
