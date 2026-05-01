"""
Shared NSFG loader for the statistics chapters.

The first chapter (eda.qmd) walks through this code line by line.
Subsequent chapters import the cleaned `live`, `first`, `other`
DataFrames from here so they don't reload and re-validate the data on
every render.
"""

from __future__ import annotations

import gzip
import os
import re

import numpy as np
import pandas as pd

COLORS = {
    "first":     "#2196F3",
    "other":     "#4CAF50",
    "highlight": "#F44336",
    "neutral":   "#9E9E9E",
}


def parse_dct(dct_path: str) -> list[dict]:
    """Parse a Stata .dct file. Each column line has the form

        _column(START)  TYPE  NAME  %WIDTH(s|f)  "label"

    where START is the 1-indexed byte where this column begins and
    WIDTH is the number of bytes it occupies. Type letter `s` = string,
    `f` = numeric.
    """
    columns = []
    pattern = re.compile(
        r"_column\((\d+)\)\s+(\w+)\s+(\w+)\s+%(\d+)([a-z])"
    )
    with open(dct_path) as f:
        for line in f:
            match = pattern.search(line)
            if match:
                start, type_word, name, width, fmt = match.groups()
                start_idx = int(start) - 1                  # 0-indexed
                end_idx = start_idx + int(width)            # exclusive
                dtype = "str" if fmt == "s" else type_word
                columns.append({
                    "name":  name,
                    "start": start_idx,
                    "end":   end_idx,
                    "dtype": dtype,
                })
    return columns


def load_fixed_width(dat_path: str, columns: list[dict]) -> pd.DataFrame:
    records = []
    opener = gzip.open if dat_path.endswith(".gz") else open
    with opener(dat_path, "rt") as f:
        for line in f:
            record = {}
            for col in columns:
                raw = line[col["start"]:col["end"]].strip()
                if raw == "":
                    record[col["name"]] = np.nan
                elif col["dtype"].startswith("str"):
                    record[col["name"]] = raw
                else:
                    try:
                        record[col["name"]] = float(raw)
                    except ValueError:
                        record[col["name"]] = np.nan
            records.append(record)
    return pd.DataFrame(records)


def load_pregnancy_data(data_dir: str = "data") -> pd.DataFrame:
    """Load + clean the NSFG 2002 female-pregnancy file."""
    columns = parse_dct(os.path.join(data_dir, "2002FemPreg.dct"))
    df = load_fixed_width(os.path.join(data_dir, "2002FemPreg.dat.gz"), columns)
    df["agepreg"] = df["agepreg"] / 100.0
    if "birthwgt_lb" in df.columns and "birthwgt_oz" in df.columns:
        df["totalwgt_lb"] = df["birthwgt_lb"] + df["birthwgt_oz"] / 16.0
    return df


def load_groups(data_dir: str = "data"):
    """Return (live, first, other) DataFrames split by birth order."""
    df = load_pregnancy_data(data_dir)
    live = df[df["outcome"] == 1].copy()
    first = live[live["birthord"] == 1]
    other = live[live["birthord"] > 1]
    return live, first, other


# ----------------------------------------------------------------------------
# Reusable PMF / CDF classes (built from scratch in earlier chapters).
# Later chapters import these so they can compose, not redefine them.
# ----------------------------------------------------------------------------

def _is_nan(v) -> bool:
    try:
        return np.isnan(v)
    except (TypeError, ValueError):
        return False


class Pmf:
    """Probability Mass Function. See chapter on PMFs for the build-up."""

    def __init__(self, values):
        counts: dict = {}
        for v in values:
            if not _is_nan(v):
                counts[v] = counts.get(v, 0) + 1
        total = sum(counts.values())
        self.d: dict = {v: c / total for v, c in counts.items()}

    def prob(self, value, default: float = 0.0) -> float:
        return self.d.get(value, default)

    def values(self):
        return sorted(self.d.keys())

    def probs(self):
        return [self.d[v] for v in self.values()]

    def mean(self) -> float:
        return sum(v * p for v, p in self.d.items())

    def __repr__(self):
        return f"Pmf({len(self.d)} values, mean={self.mean():.3f})"


class Cdf:
    """Empirical Cumulative Distribution Function. See CDF chapter."""

    def __init__(self, values):
        clean = np.array(sorted(v for v in values if not _is_nan(float(v))))
        n = len(clean)
        self.xs = clean
        self.ps = np.arange(1, n + 1) / n

    def prob(self, x: float) -> float:
        idx = np.searchsorted(self.xs, x, side="right")
        return idx / len(self.xs)

    def value(self, p: float) -> float:
        if p <= 0:
            return self.xs[0]
        if p >= 1:
            return self.xs[-1]
        idx = int(p * len(self.xs))
        return self.xs[idx]

    def median(self) -> float:
        return self.value(0.5)

    def iqr(self) -> float:
        return self.value(0.75) - self.value(0.25)

    def percentile_rank(self, x: float) -> float:
        return self.prob(x) * 100

    def sample(self, n: int) -> np.ndarray:
        u = np.random.uniform(0, 1, size=n)
        return np.array([self.value(ui) for ui in u])
