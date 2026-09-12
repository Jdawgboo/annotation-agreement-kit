"""Dependency-free two-rater agreement metrics."""
from __future__ import annotations

import argparse
import json
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Hashable, Sequence


@dataclass(frozen=True)
class Agreement:
    observed: float
    expected: float
    cohen_kappa: float
    disagreements: tuple[int, ...]


def cohen_kappa(left: Sequence[Hashable], right: Sequence[Hashable]) -> Agreement:
    if len(left) != len(right) or not left:
        raise ValueError("two non-empty label sequences of equal length are required")
    labels = set(left) | set(right)
    observed = sum(a == b for a, b in zip(left, right)) / len(left)
    left_counts, right_counts = Counter(left), Counter(right)
    expected = sum((left_counts[label] / len(left)) * (right_counts[label] / len(right)) for label in labels)
    kappa = (observed - expected) / (1 - expected) if expected != 1 else 1.0
    return Agreement(observed, expected, kappa, tuple(index for index, pair in enumerate(zip(left, right)) if pair[0] != pair[1]))


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate two-rater Cohen's kappa from JSON labels")
    parser.add_argument("labels", type=Path, help="JSON object with left and right arrays")
    args = parser.parse_args()
    payload = json.loads(args.labels.read_text())
    result = cohen_kappa(payload["left"], payload["right"])
    print(json.dumps(result.__dict__, indent=2))


if __name__ == "__main__":
    main()
