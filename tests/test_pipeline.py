"""
tests/test_pipeline.py — Unit tests for SDG-3 analysis utilities
Author: Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic
"""
import pytest
import numpy as np
from scripts.spatial_utils import normalise_indicator, compute_sdg3_composite, classify_sdg_progress


def test_normalise_positive():
    vals = [10, 20, 30, 40, 50]
    result = normalise_indicator(vals, direction="positive")
    assert float(result[0]) == pytest.approx(0.0)
    assert float(result[-1]) == pytest.approx(100.0)


def test_normalise_negative():
    vals = [10, 50, 100]
    result = normalise_indicator(vals, direction="negative")
    assert float(result[0]) == pytest.approx(100.0)
    assert float(result[-1]) == pytest.approx(0.0)


def test_normalise_constant():
    vals = [42, 42, 42]
    result = normalise_indicator(vals)
    assert all(v == 50.0 for v in result)


def test_composite_equal_weights():
    ind = {"a": [0.0, 50.0, 100.0], "b": [0.0, 50.0, 100.0]}
    result = compute_sdg3_composite(ind)
    np.testing.assert_allclose(result, [0.0, 50.0, 100.0])


def test_classify_progress():
    assert classify_sdg_progress(85) == "on_track"
    assert classify_sdg_progress(70) == "progressing"
    assert classify_sdg_progress(50) == "lagging"
