# SDG-3 Health Progress in Ghana: Spatial Analysis of 261 Districts (2000–2030 Trajectory)

[![CI](https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/actions/workflows/ci.yml/badge.svg)](https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/) [![R 4.3+](https://img.shields.io/badge/R-4.3+-blue.svg)](https://www.r-project.org/) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--8332--0220-green.svg)](https://orcid.org/0009-0002-8332-0220)

**Author:** Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**ORCID:** [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)
**Affiliation:** Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**Reporting standard:** STROBE
**Date:** 2026
**Status:** Manuscript in preparation

## 1. Abstract

This study examines spatial variation in Sustainable Development Goal 3 (SDG-3) health progress across Ghana's 261 districts from 2000 to 2022, projecting trajectories toward the 2030 targets. A composite SDG-3 index was constructed from six sub-indicators: ANC4+ coverage, skilled birth attendance, under-5 mortality rate reduction, maternal mortality reduction, HIV incidence reduction, and TB treatment success. Spatial analysis revealed strong positive autocorrelation (Moran's I = 0.71, p < 0.001) with a pronounced north–south gradient. Greater Accra scored highest (72.4) while North East scored lowest (29.6), a 2.45-fold disparity. Machine learning identified healthcare facility density, poverty incidence, and NHIS coverage as the strongest predictors of SDG-3 progress. National composite score improved from 28.4 (2000) to 48.9 (2022), but current trajectories suggest northern regions will not meet 2030 targets without targeted intervention.

## 2. Research Question & Aims

**Primary question:** What are the spatial determinants and district-level heterogeneity of SDG-3 health progress in Ghana?

**Aims:**
1. Construct a validated SDG-3 composite index for 261 Ghana districts
2. Characterise spatial clustering and north–south gradient (LISA, Gi*, Moran's I)
3. Identify modifiable predictors of SDG progress using XGBoost and SHAP
4. Model GWR spatial heterogeneity in SDG-progress determinants
5. Project 2030 attainment trajectories under current trends

## 3. Methods Summary

| Method | Tool | Purpose |
|--------|------|---------|
| Global Moran's I (queen contiguity) | esda / libpysal (Python) | Spatial autocorrelation of SDG-3 composite index |
| LISA (999 permutations, BH-FDR) | esda / libpysal (Python) | Local cluster delineation (HH/LL/HL/LH) |
| Getis-Ord Gi* | esda / libpysal (Python) | Hotspot / coldspot detection |
| XGBoost + SHAP (LOROCV) | xgboost / shap (Python) | SDG-3 composite prediction + feature attribution |
| Random Forest (ensemble) | scikit-learn (Python) | Secondary predictor importance ranking |
| GWR (adaptive bi-square, AICc) | GWModel / mgwr (R) | Spatially varying coefficient estimation |
| Spatial regression diagnostics | spdep / spatialreg (R) | OLS / SLM / SEM model selection |

## 4. Data Sources

| Source | Variables | Year | Access |
|--------|-----------|------|--------|
| Ghana Demographic and Health Survey (GDHS) | ANC4+, skilled birth, U5MR, IYCF | 2003–2022 | Public (DHS Programme) |
| WHO Global Health Observatory | Malaria, TB, HIV incidence | 2000–2022 | Public |
| Ghana Health Service (GHS-P) | Facility density, NHIS coverage | 2010–2022 | Public |
| World Bank Open Data | Poverty incidence, education | 2000–2022 | Public |
| Ghana Statistical Service | District-level demographics | 2010–2021 | Public |

## 5. Key Findings

| Metric | Value |
|--------|-------|
| SDG-3 Moran's I | 0.71 (p < 0.001) |
| Highest regional score | 72.4 (Greater Accra) |
| Lowest regional score | 29.6 (North East) |
| North–South disparity | 2.45× |
| National trend 2000–2022 | +20.5 points (28.4 → 48.9) |
| Top predictor (SHAP) | Healthcare facility density (3.4) |
| XGBoost R² | 0.83 (LOROCV) |
| ANC4+ progress toward 2030 target | 69% |
| TB treatment success progress | 86% |
| HIV incidence reduction progress | 67% |

## 6. Repository Structure

\`\`\`
sdg-health-progress-ghana-261-districts/
├── dashboard/
│   └── SDG_HealthProgress_Ghana_Dashboard.html   # Self-contained interactive HTML dashboard
├── poster/
│   └── SDG_HealthProgress_Ghana_Poster.html       # A0 conference poster (print-ready HTML)
├── scripts/
│   ├── spatial_utils.py          # Python: SDG index normalisation + composite construction
│   ├── analysis_pipeline.py      # Python: main analysis entry point (LISA · GWR · XGBoost · SHAP)
│   └── spatial_diagnostics.R     # R: spatial lag/error model selection (LM tests · GWR)
├── tests/
│   └── test_pipeline.py          # Python: unit tests for spatial utility functions
├── app.py                        # Python: Plotly Dash interactive application
├── analysis.R                    # R: GWR bandwidth selection + spatialreg diagnostics
├── requirements.txt
├── CITATION.cff
├── LICENSE
├── .gitattributes
└── .github/workflows/ci.yml
\`\`\`

## 7. Reproducibility

### 7.1 Requirements

- Python 3.12 (pinned in \`requirements.txt\`)
- R 4.3+ with packages: spdep, spatialreg, GWmodel, mgwr, dplyr (see \`analysis.R\` header)
- Random seed: 42 throughout
- Estimated runtime: ~5–8 minutes on a standard laptop
- Tested on: Ubuntu 22.04 / macOS 14 / Windows 11 (CI: GitHub Actions)

### 7.2 Clone & install

\`\`\`bash
git clone https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts.git
cd sdg-health-progress-ghana-261-districts
pip install -r requirements.txt
\`\`\`

### 7.3 Run the analytical pipeline

\`\`\`bash
python scripts/analysis_pipeline.py          # SDG composite index construction + LISA + SHAP
Rscript scripts/spatial_diagnostics.R        # LM tests, SLM/SEM selection, GWR diagnostics
Rscript analysis.R                           # GWR bandwidth selection + coefficient mapping
\`\`\`

### 7.4 Run the test suite

\`\`\`bash
python -m pytest tests/ -v
\`\`\`

### 7.5 Launch the interactive Dash application

\`\`\`bash
python app.py
# Open http://127.0.0.1:8050 in your browser
\`\`\`

### 7.6 Open the static HTML dashboard

\`\`\`bash
# macOS
open dashboard/SDG_HealthProgress_Ghana_Dashboard.html
# Windows
start dashboard/SDG_HealthProgress_Ghana_Dashboard.html
# Linux
xdg-open dashboard/SDG_HealthProgress_Ghana_Dashboard.html
\`\`\`

No server required. The file is fully self-contained.

## 8. Outputs

| Output | Description |
|--------|-------------|
| SDG_HealthProgress_Ghana_Dashboard.html | Interactive HTML dashboard — all panels, choropleth map, LISA clusters |
| SDG_HealthProgress_Ghana_Poster.html | Printable A0 conference poster |

## 8a. Downloadable Artefacts (HTML)

Both the interactive dashboard and the conference poster are committed as self-contained HTML files — no server, no build step, no internet connection required to open them locally.

| Artefact | View on GitHub | Live preview | Direct download |
|----------|---------------|--------------|-----------------|
| Interactive dashboard | [View](https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/blob/main/dashboard/SDG_HealthProgress_Ghana_Dashboard.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/blob/main/dashboard/SDG_HealthProgress_Ghana_Dashboard.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/main/dashboard/SDG_HealthProgress_Ghana_Dashboard.html) |
| Conference poster | [View](https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/blob/main/poster/SDG_HealthProgress_Ghana_Poster.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/blob/main/poster/SDG_HealthProgress_Ghana_Poster.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts/main/poster/SDG_HealthProgress_Ghana_Poster.html) |

## 9. Reporting Standard

This study follows the STROBE (Strengthening the Reporting of Observational Studies in Epidemiology) statement for cross-sectional and ecological studies.

von Elm E, Altman DG, Egger M, et al. The Strengthening the Reporting of Observational Studies in Epidemiology (STROBE) statement: guidelines for reporting observational studies. *Lancet*. 2007;370(9596):1453–1457.

## 10. Ethical Statement

This study uses exclusively publicly available, anonymised, and aggregated district-level data from national surveys (GDHS), the WHO Global Health Observatory, and the Ghana Health Service. No individual-level data were collected or processed. No ethical approval was required.

## 11. Citation

Ghanem, V. G. (2026). *SDG-3 Health Progress in Ghana: Spatial Analysis of 261 Districts (2000–2030 Trajectory)*. GitHub. https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts

\`\`\`bibtex
@misc{ghanem2026sdg,
  author       = {Ghanem, Valentine Golden},
  title        = {{SDG-3 Health Progress in Ghana: Spatial Analysis of 261 Districts (2000--2030 Trajectory)}},
  year         = {2026},
  publisher    = {GitHub},
  url          = {https://github.com/valentineghanem-bit/sdg-health-progress-ghana-261-districts},
  orcid        = {0009-0002-8332-0220}
}
\`\`\`

See also \`CITATION.cff\` for machine-readable citation metadata.

## 12. License

Code: [MIT License](LICENSE)
Outputs and figures: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

## 13. Author & Contact

**Valentine Golden Ghanem**
Ghana COCOBOD Cocoa Clinic, Accra, Ghana
ORCID: [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)

## 14. Acknowledgements

Data sourced from the Ghana Demographic and Health Survey (DHS Programme), the WHO Global Health Observatory, the Ghana Health Service Population database, and the World Bank Open Data platform. Spatial analysis used open-source PySAL, esda, geopandas, and GWModel libraries. The author thanks the broader global health and spatial epidemiology communities whose open-source tools made this analysis possible.
