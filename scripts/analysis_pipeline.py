"""
analysis_pipeline.py — Main SDG-3 spatial analysis pipeline
Author: Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic
ORCID: 0009-0002-8332-0220
"""
from scripts.spatial_utils import normalise_indicator, compute_sdg3_composite


def run_pipeline():
    """
    Main pipeline entry point.
    Loads data, computes SDG-3 composite, runs spatial analysis.
    Data must be in data/processed/sdg_inputs.csv
    """
    print("SDG-3 Health Progress Ghana — Analysis Pipeline")
    print("=" * 55)

    # Synthetic demonstration — replace with real data load
    demo_regions = [
        "Greater Accra", "Ashanti", "Central", "Eastern", "Western",
        "Volta", "Oti", "Bono East", "Ahafo", "Bono",
        "Western North", "Upper East", "Upper West",
        "Northern", "Savannah", "Northern East"
    ]
    demo_anc4 = [96.4, 91.3, 87.3, 85.6, 83.4, 81.2, 72.4, 73.1, 74.8, 76.5,
                 67.8, 61.4, 57.2, 52.1, 48.3, 43.8]

    normalised = normalise_indicator(demo_anc4, direction="positive")
    composite = compute_sdg3_composite({"anc4": normalised})

    print("\nDemo: Regional ANC4+ → Normalised SDG sub-index")
    for region, norm in zip(demo_regions, composite):
        print(f"  {region:<25} {norm:5.1f}")

    print("\nPipeline complete. Provide real district CSV for full analysis.")


if __name__ == "__main__":
    run_pipeline()
