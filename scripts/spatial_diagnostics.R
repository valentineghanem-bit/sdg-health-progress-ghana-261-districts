# spatial_diagnostics.R — Spatial lag/error model selection
# Author: Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic
# ORCID: 0009-0002-8332-0220
# Packages: spdep, spatialreg

# Lagrange Multiplier tests to select between SLM and SEM:
# lm_tests <- lm.LMtests(ols_model, lw, test = "all")
# If LM-lag > LM-error: use spatial lag model (SLM)
# If LM-error > LM-lag: use spatial error model (SEM)

# GWR bandwidth selection and fitting — see analysis.R for details

cat("Spatial diagnostics helper loaded.\n")
