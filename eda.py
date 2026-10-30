"""
Comprehensive Exploratory Data Analysis (EDA) for NYU_CTF_Bench.
Balanced visual suite combining clean horizontal stacked bars, donut charts,
line trends, and single-hue sequential gradient frequency bars (darker = higher count).
"""
import json
from pathlib import Path
from collections import Counter
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.colors as mcolors
import numpy as np

# ── Global Plot Style Configuration (Professional Academic Theme) ────────────
plt.rcParams.update({
    "figure.facecolor": "#ffffff",
    "axes.facecolor": "#ffffff",
    "axes.edgecolor": "#cbd5e1",
    "axes.linewidth": 0.8,
    "axes.labelcolor": "#1e293b",
    "axes.labelsize": 10.5,
    "axes.labelweight": "semibold",
    "axes.titlecolor": "#0f172a",
    "axes.titlesize": 12.0,
    "axes.titleweight": "bold",
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.color": "#f1f5f9",
    "grid.linewidth": 0.75,
    "xtick.color": "#64748b",
    "xtick.labelsize": 9.5,
    "ytick.color": "#1e293b",
    "ytick.labelsize": 9.5,
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "Inter", "DejaVu Sans", "Arial"],
    "font.size": 9.5,
    "figure.dpi": 200,
    "legend.framealpha": 0.95,
    "legend.edgecolor": "#e2e8f0",
    "legend.fontsize": 9.0,
})

BASE_DIR     = Path(__file__).parent
INDEX_FILE   = BASE_DIR / "selected_dataset.json"
SELECTED_DIR = BASE_DIR / "selected-benchmarks"
MITRE_FILE   = BASE_DIR / "mitre_attack_mapping" / "test_mapping.json"
OUT_DIR      = BASE_DIR / "eda_figures"
OUT_DIR.mkdir(exist_ok=True)

# Cohesive Palette (Muted Navy, Slate, and Steel Blues)
CAT_COLORS = {
    "web": "#1e40af",        # Deep Indigo
    "forensics": "#0e7490",  # Slate Cyan
    "misc": "#64748b",       # Muted Slate
}
STAGE_COLORS = {
    "CSAW-Quals": "#60a5fa",   # Steel Blue
    "CSAW-Finals": "#1e3a8a",  # Deep Navy
}


def get_gradient_colors(counts, min_factor=0.35, max_factor=0.92):
    """Generate monochromatic shades: lighter = fewer, darker = more."""
    cmap = plt.get_cmap("Blues")
    min_c = min(counts) if counts else 0
    max_c = max(counts) if counts else 1
    if max_c == min_c:
        norm_vals = [0.7] * len(counts)
    else:
        norm_vals = [min_factor + (c - min_c) / (max_c - min_c) * (max_factor - min_factor) for c in counts]
    return [mcolors.to_hex(cmap(v)) for v in norm_vals]


def load_data():
    """Load benchmark index and enrich with challenge metadata and MITRE mapping."""
    with open(INDEX_FILE, encoding="utf-8") as f:
        index = json.load(f)

    # Load MITRE techniques if available
    mitre_techs = {}
    mitre_mapping = {}
    if MITRE_FILE.exists():
        try:
            with open(MITRE_FILE, encoding="utf-8") as mf:
                mdata = json.load(mf)
                mitre_techs = mdata.get("techniques", {})
                mitre_mapping = mdata.get("mapping", {})
        except Exception as e:
            print(f"Warning: failed loading {MITRE_FILE}: {e}")

    records = []
    for uid, meta in index.items():
        r = dict(meta)
        r["uid"] = uid
        
        rel_path = meta["path"].replace("selected-benchmarks/", "")
        cp = SELECTED_DIR / rel_path / "challenge.json"
        
        r["num_files"] = 0
        r["mitre_ids"] = mitre_mapping.get(uid, [])
        r["mitre_names"] = [mitre_techs.get(tid, tid) for tid in r["mitre_ids"]]

        if cp.exists():
            try:
                with open(cp, encoding="utf-8") as f:
                    ch = json.load(f)
                r["num_files"] = len(ch.get("files", []) or [])
            except Exception as e:
                print(f"Warning: failed reading {cp}: {e}")
        
        records.append(r)
    return records


def save_figure(fig, name):
    """Save figure with clean padding and crisp resolution."""
    p = OUT_DIR / f"{name}.png"
    fig.savefig(p, bbox_inches="tight", facecolor="white", dpi=200)
    plt.close(fig)
    print(f"  [+] Saved figure -> {p.name}")


# ── Figure 1: Donut Chart - Category Proportion ──────────────────────────────
def fig01_category_donut(records):
    """Figure 1: Donut ring chart representing category proportion with darker-to-lighter gradient."""
    cats = Counter(r["category"] for r in records)
    total = len(records)
    
    order = sorted(cats.keys(), key=lambda c: cats[c], reverse=True)
    counts = [cats[c] for c in order]
    colors = get_gradient_colors(counts, min_factor=0.40, max_factor=0.92)
    labels = [f"{c.capitalize()}\n({cats[c]}, {cats[c]/total*100:.1f}%)" for c in order]

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    wedges, texts = ax.pie(
        counts,
        labels=labels,
        colors=colors,
        startangle=140,
        pctdistance=0.75,
        wedgeprops=dict(width=0.38, edgecolor="white", linewidth=2.0),
        textprops=dict(color="#1e293b", fontsize=9.5, fontweight="medium")
    )

    ax.text(0, 0.06, f"{total}", ha="center", va="center", fontsize=20, fontweight="bold", color="#0f172a")
    ax.text(0, -0.12, "Challenges", ha="center", va="center", fontsize=9.5, color="#64748b", fontweight="medium")

    ax.set_title("NYU CTF Bench: Challenge Category Composition", pad=12)
    save_figure(fig, "01_category_distribution_donut")


# ── Figure 2: Horizontal Stacked Bar - Quals vs Finals by Category ───────────
def fig02_stage_by_category_hbar(records):
    """Figure 2: Clean horizontal stacked bar of Quals vs Finals per category."""
    categories = sorted(list({r["category"] for r in records}))
    
    quals_counts = [sum(1 for r in records if r["category"] == c and "Quals" in r["event"]) for c in categories]
    finals_counts = [sum(1 for r in records if r["category"] == c and "Finals" in r["event"]) for c in categories]
    totals = [q + f for q, f in zip(quals_counts, finals_counts)]

    order = sorted(range(len(categories)), key=lambda i: totals[i])
    cat_labels = [categories[i].capitalize() for i in order]
    q_vals = [quals_counts[i] for i in order]
    f_vals = [finals_counts[i] for i in order]
    tot_vals = [totals[i] for i in order]

    fig, ax = plt.subplots(figsize=(8.5, 3.6))
    y_pos = np.arange(len(cat_labels))
    bar_height = 0.52

    ax.barh(y_pos, q_vals, height=bar_height, color=STAGE_COLORS["CSAW-Quals"], label="Quals", edgecolor="white", linewidth=0.8)
    ax.barh(y_pos, f_vals, left=q_vals, height=bar_height, color=STAGE_COLORS["CSAW-Finals"], label="Finals", edgecolor="white", linewidth=0.8)

    for yi, (q, f, tot) in enumerate(zip(q_vals, f_vals, tot_vals)):
        if q >= 2:
            ax.text(q / 2, yi, str(q), va="center", ha="center", color="#0f172a", fontweight="semibold", fontsize=9)
        if f >= 2:
            ax.text(q + f / 2, yi, str(f), va="center", ha="center", color="white", fontweight="semibold", fontsize=9)
        ax.text(tot + 0.4, yi, f"Total: {tot}", va="center", ha="left", color="#334155", fontweight="medium", fontsize=9)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(cat_labels)
    ax.set_xlim(0, max(tot_vals) * 1.25)
    ax.set_xlabel("Number of Challenges", labelpad=7)
    ax.set_title("NYU CTF Bench: Category Breakdown by Competition Stage", pad=10)
    ax.legend(loc="lower right", frameon=True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "02_competition_stage_by_category")


# ── Figure 3: Line Trend Chart - Yearly Progression (2017–2023) ──────────────
def fig03_yearly_trend_line(records):
    """Figure 3: Multi-line trend with markers showing challenge volume evolution."""
    years = sorted(list({r["year"] for r in records}))
    categories = ["web", "forensics", "misc"]
    
    fig, ax = plt.subplots(figsize=(8.5, 4.0))
    markers = {"web": "o", "forensics": "s", "misc": "^"}
    linestyles = {"web": "-", "forensics": "--", "misc": "-."}

    for c in categories:
        counts = [sum(1 for r in records if r["year"] == y and r["category"] == c) for y in years]
        ax.plot(
            years, counts,
            color=CAT_COLORS[c],
            label=c.capitalize(),
            marker=markers[c],
            markersize=6.5,
            linewidth=2.0,
            linestyle=linestyles[c]
        )
        for xi, (y, val) in enumerate(zip(years, counts)):
            if val > 0:
                ax.annotate(
                    f"{val}",
                    (xi, val),
                    textcoords="offset points",
                    xytext=(0, 6),
                    ha="center",
                    fontsize=8.5,
                    color=CAT_COLORS[c],
                    fontweight="semibold"
                )

    ax.set_ylim(-0.5, 8.5)
    ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.set_xlabel("Competition Year", labelpad=8)
    ax.set_ylabel("Number of Challenges", labelpad=8)
    ax.set_title("NYU CTF Bench: Yearly Category Volume Trend (2017–2023)", pad=12)
    ax.legend(loc="upper left", frameon=True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.6)
    ax.grid(axis="x", linestyle=":", alpha=0.4)

    save_figure(fig, "03_yearly_trend_by_category")


# ── Figure 4: Horizontal Gradient Bar - MITRE ATT&CK Techniques Frequency ─────
def fig04_mitre_attack_techniques_hbar(records):
    """Figure 4: Frequency of MITRE ATT&CK techniques with lighter-to-darker gradient."""
    all_techs = []
    for r in records:
        for tid, tname in zip(r.get("mitre_ids", []), r.get("mitre_names", [])):
            all_techs.append(f"{tname} ({tid})")

    tech_counts = Counter(all_techs)
    top_techs = tech_counts.most_common(12)
    
    # Sort ascending for horizontal bar (largest at top)
    order = top_techs[::-1]
    labels = [t[0] for t in order]
    counts = [t[1] for t in order]

    # Monochromatic lighter-to-darker gradient
    colors = get_gradient_colors(counts)

    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    y_pos = np.arange(len(labels))
    bars = ax.barh(y_pos, counts, color=colors, height=0.55, edgecolor="none")

    for bar, count in zip(bars, counts):
        ax.text(
            bar.get_width() + 0.25,
            bar.get_y() + bar.get_height() / 2,
            f" {count}",
            va="center", ha="left",
            fontsize=9.0, fontweight="bold", color="#1e293b"
        )

    ax.set_yticks(y_pos)
    ax.set_yticklabels(labels, fontsize=9.0)
    ax.set_xlim(0, max(counts) * 1.2)
    ax.set_xlabel("Number of Challenges", labelpad=7)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
    ax.set_title("NYU CTF Bench: Top MITRE ATT&CK Techniques Frequency", pad=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "04_mitre_attack_techniques")


# ── Figure 5: Horizontal Stacked Bar - Provided Attachment Files ─────────────
def fig05_attachment_files_hbar(records):
    """Figure 5: Horizontal stacked bar of provided attachment files per category."""
    categories = ["web", "forensics", "misc"]
    file_buckets = ["0 Files", "1 File", "2 Files", "3+ Files"]
    BUCKET_COLORS = ["#cbd5e1", "#93c5fd", "#3b82f6", "#1e3a8a"]

    def get_bucket(n):
        if n == 0: return "0 Files"
        elif n == 1: return "1 File"
        elif n == 2: return "2 Files"
        else: return "3+ Files"

    counts_by_cat = {
        b: [sum(1 for r in records if r["category"] == c and get_bucket(r["num_files"]) == b) for c in categories]
        for b in file_buckets
    }
    totals = [sum(counts_by_cat[b][ci] for b in file_buckets) for ci in range(len(categories))]

    order = sorted(range(len(categories)), key=lambda i: totals[i])
    cat_labels = [categories[i].capitalize() for i in order]

    fig, ax = plt.subplots(figsize=(8.5, 3.8))
    y_pos = np.arange(len(cat_labels))
    bar_height = 0.52
    left = np.zeros(len(cat_labels))

    for b, col in zip(file_buckets, BUCKET_COLORS):
        vals = np.array([counts_by_cat[b][i] for i in order])
        ax.barh(y_pos, vals, left=left, height=bar_height, color=col, label=b, edgecolor="white", linewidth=0.8)
        for yi, (v, l) in enumerate(zip(vals, left)):
            if v >= 2:
                text_color = "white" if col in ["#1e3a8a", "#3b82f6"] else "#0f172a"
                ax.text(l + v / 2, yi, str(v), ha="center", va="center", color=text_color, fontweight="semibold", fontsize=9)
        left += vals

    for yi, tot in enumerate([totals[i] for i in order]):
        ax.text(tot + 0.4, yi, f"Total: {tot}", va="center", ha="left", color="#334155", fontweight="medium", fontsize=9)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(cat_labels)
    ax.set_xlim(0, max(totals) * 1.25)
    ax.set_xlabel("Number of Challenges", labelpad=7)
    ax.set_title("NYU CTF Bench: Provided Attachment Files per Category", pad=10)
    ax.legend(loc="lower right", frameon=True, title="Attachments")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.6)
    ax.grid(axis="y", visible=False)

    save_figure(fig, "05_attachment_files_distribution")


def main():
    print("=" * 60)
    print("Running Comprehensive EDA for NYU CTF Bench")
    print("=" * 60)
    records = load_data()
    print(f"Loaded {len(records)} benchmark challenges from {INDEX_FILE.name}\n")
    
    fig01_category_donut(records)
    fig02_stage_by_category_hbar(records)
    fig03_yearly_trend_line(records)
    fig04_mitre_attack_techniques_hbar(records)
    fig05_attachment_files_hbar(records)
    print(f"\nAll figures successfully generated in: {OUT_DIR}\n")


if __name__ == "__main__":
    main()
