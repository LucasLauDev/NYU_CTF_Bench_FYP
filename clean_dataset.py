#!/usr/bin/env python3
"""
clean_dataset.py

Filters challenges in categories ('web', 'misc', 'crypto') and optionally requires
Docker services (filtering out offline/static challenges without docker-compose).
Cleans destination directory and updates selected_dataset.json.
"""

import argparse
import json
import logging
import os
import shutil
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger("clean_dataset")

DEFAULT_CATEGORIES = ["forensics", "web", "misc", "crypto"]
DEFAULT_SRC_JSON = "selected-benchmarks/selected_dataset.json"
DEFAULT_DEST_DIR = "selected-benchmarks"
DEFAULT_OUTPUT_JSON = "selected-benchmarks/selected_dataset.json"


def has_docker_service(challenge_path: Path) -> bool:
    """Check if the challenge contains a docker-compose file."""
    compose_names = [
        "docker-compose.yml",
        "docker-compose.yaml",
        "compose.yml",
        "compose.yaml",
    ]
    for name in compose_names:
        if (challenge_path / name).exists():
            return True
    # Also check if any docker-compose exists in subdirectories
    return bool(list(challenge_path.rglob("docker-compose*.y*ml")))


def remove_empty_dirs(root_dir: Path):
    """Recursively remove empty subdirectories."""
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        current_dir = Path(dirpath)
        if current_dir != root_dir and not any(current_dir.iterdir()):
            try:
                current_dir.rmdir()
                logger.debug(f"Removed empty directory: {current_dir}")
            except OSError:
                pass


def clean_and_select_dataset(
    src_json_path: str = DEFAULT_SRC_JSON,
    dest_dir_name: str = DEFAULT_DEST_DIR,
    output_json_path: str = DEFAULT_OUTPUT_JSON,
    categories: list = None,
    require_docker: bool = True,
):
    if categories is None:
        categories = DEFAULT_CATEGORIES

    target_categories = set(cat.lower() for cat in categories)
    src_json = Path(src_json_path).resolve()

    # Fallback to selected_dataset.json if test_dataset.json does not exist
    if not src_json.exists():
        fallback_json = (src_json.parent / DEFAULT_OUTPUT_JSON).resolve()
        if fallback_json.exists():
            logger.info(f"Source JSON not found at {src_json}, using fallback {fallback_json}")
            src_json = fallback_json
        else:
            logger.error(f"Source JSON file not found: {src_json}")
            raise FileNotFoundError(f"Source JSON file not found: {src_json}")

    workspace_dir = src_json.parent
    # If src_json is inside dest_dir (e.g. selected-benchmarks/selected_dataset.json), workspace is its parent's parent
    if src_json.name == "selected_dataset.json" and src_json.parent.name == dest_dir_name:
        workspace_dir = src_json.parent.parent

    dest_dir = (workspace_dir / dest_dir_name).resolve()
    dest_dir.mkdir(parents=True, exist_ok=True)

    logger.info(f"Loading dataset from {src_json}...")
    with open(src_json, "r", encoding="utf-8") as f:
        dataset = json.load(f)

    selected_dataset = {}
    category_counts = {cat: 0 for cat in target_categories}
    removed_offline = []
    skipped_category = []

    logger.info(
        f"Filtering challenges in categories: {sorted(list(target_categories))} (require_docker={require_docker})..."
    )

    for key, challenge_info in dataset.items():
        category = challenge_info.get("category", "").lower()
        if category not in target_categories:
            skipped_category.append(key)
            continue

        orig_path_str = challenge_info.get("path", "")
        src_challenge_path = (workspace_dir / orig_path_str).resolve()

        if not src_challenge_path.exists():
            logger.warning(f"Challenge folder not found at {src_challenge_path}, skipping {key}")
            continue

        # Determine relative subpath inside 'test', 'selected-benchmarks', or root
        rel_path = Path(orig_path_str)
        if rel_path.parts and rel_path.parts[0] in ("test", dest_dir_name):
            rel_path = Path(*rel_path.parts[1:])

        dest_challenge_path = dest_dir / rel_path

        # Check for docker compose / network service
        if require_docker and not has_docker_service(src_challenge_path):
            logger.info(f"Excluding offline/no-docker challenge: {key} ({orig_path_str})")
            removed_offline.append((key, orig_path_str))
            # If the folder exists in destination directory, remove it
            if dest_challenge_path.exists():
                shutil.rmtree(dest_challenge_path)
                logger.info(f"  -> Deleted offline folder: {dest_challenge_path}")
            continue

        # If not in-place copy, copy challenge files to destination
        if src_challenge_path != dest_challenge_path:
            dest_challenge_path.parent.mkdir(parents=True, exist_ok=True)
            if dest_challenge_path.exists():
                shutil.rmtree(dest_challenge_path)
            shutil.copytree(src_challenge_path, dest_challenge_path)

        # Build updated entry
        new_entry = dict(challenge_info)
        new_entry["path"] = (Path(dest_dir_name) / rel_path).as_posix()

        selected_dataset[key] = new_entry
        category_counts[category] += 1

    # Clean up any leftover empty directories in dest_dir
    remove_empty_dirs(dest_dir)

    out_file = workspace_dir / output_json_path
    out_file.parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(selected_dataset, f, indent=2)
        f.write("\n")

    logger.info("=== Cleaning & Dataset Generation Summary ===")
    logger.info(f"Total challenges retained: {len(selected_dataset)}")
    for cat, count in sorted(category_counts.items()):
        logger.info(f"  - {cat}: {count} challenges")
    if require_docker:
        logger.info(f"Total offline challenges removed/excluded: {len(removed_offline)}")
    logger.info(f"Destination folder: {dest_dir}")
    logger.info(f"JSON dataset file updated: {out_file}")

    return selected_dataset


def main():
    parser = argparse.ArgumentParser(
        description="Filter web, misc, and crypto challenges and remove offline challenges without docker."
    )
    parser.add_argument(
        "--src-json",
        default=DEFAULT_SRC_JSON,
        help=f"Path to source dataset JSON file (default: {DEFAULT_SRC_JSON})",
    )
    parser.add_argument(
        "--dest-dir",
        default=DEFAULT_DEST_DIR,
        help=f"Destination directory name (default: {DEFAULT_DEST_DIR})",
    )
    parser.add_argument(
        "--output-json",
        default=DEFAULT_OUTPUT_JSON,
        help=f"Output dataset JSON filename (default: {DEFAULT_OUTPUT_JSON})",
    )
    parser.add_argument(
        "--categories",
        nargs="+",
        default=DEFAULT_CATEGORIES,
        help="Categories to filter (default: forensics web misc crypto)",
    )
    parser.add_argument(
        "--require-docker",
        action="store_true",
        default=True,
        help="Require docker-compose file for challenges (default: True)",
    )
    parser.add_argument(
        "--include-offline",
        dest="require_docker",
        action="store_false",
        help="Include offline/static challenges without docker compose",
    )

    args = parser.parse_args()

    clean_and_select_dataset(
        src_json_path=args.src_json,
        dest_dir_name=args.dest_dir,
        output_json_path=args.output_json,
        categories=args.categories,
        require_docker=args.require_docker,
    )


if __name__ == "__main__":
    main()

