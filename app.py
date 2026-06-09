"""
SDG-3 Health Progress in Ghana — Interactive Dash Application
Author: Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic
ORCID: 0009-0002-8332-0220
"""
import dash
from dash import dcc, html

app = dash.Dash(__name__, title="SDG-3 Health Progress Ghana")

app.layout = html.Div([
    html.H1("SDG-3 Health Progress in Ghana: 261 Districts (2000–2030)"),
    html.P("Interactive spatial analysis dashboard. See dashboard/ for the static HTML version."),
    dcc.Markdown("""
    **Study:** Spatial determinants of SDG-3 progress across 261 Ghana districts.

    **Key findings:**
    - Moran's I = 0.71 (p < 0.001) — strong spatial clustering
    - North–South gap: 72.4 (Greater Accra) vs 29.6 (North East)
    - Top predictor: Healthcare facility density (SHAP = 3.4)
    - National composite: 28.4 (2000) → 48.9 (2022)
    """),
])

if __name__ == "__main__":
    app.run(debug=True)
