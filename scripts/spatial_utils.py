"""
spatial_utils.py — Utility functions for SDG-3 spatial analysis
Author: Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic
ORCID: 0009-0002-8332-0220
"""
import numpy as np


def normalise_indicator(values, direction="positive"):
    """
    Normalise a health indicator to 0-100 scale.
    direction='positive': higher raw value = higher SDG progress
    direction='negative': lower raw value = higher SDG progress (e.g. mortality)
    """
    arr = np.array(values, dtype=float)
    mn, mx = arr.min(), arr.max()
    if mx == mn:
        return np.full_like(arr, 50.0)
    normalised = (arr - mn) / (mx - mn) * 100
    if direction == "negative":
        normalised = 100 - normalised
    return normalised


def compute_sdg3_composite(indicators, weights=None):
    """
    Compute SDG-3 composite index from normalised sub-indicators.
    indicators: dict of {name: array_of_values}
    weights: dict of {name: weight} — equal weights if None
    Returns: np.array of composite scores (0-100)
    """
    names = list(indicators.keys())
    if weights is None:
        weights = {n: 1.0 / len(names) for n in names}
    composite = np.zeros(len(next(iter(indicators.values()))))
    for name in names:
        composite += np.array(indicators[name]) * weights.get(name, 0)
    return composite


def classify_sdg_progress(score):
    """Classify a 0-100 SDG progress score into tier."""
    if score >= 80:
        return "on_track"
    elif score >= 65:
        return "progressing"
    else:
        return "lagging"
