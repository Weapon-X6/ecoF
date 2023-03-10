from flask import Flask

import folium
import pandas as pd

app = Flask(__name__)


@app.route("/")
def index():
    eco_footprints = pd.read_csv("footprint.csv")
    max_eco_footprint = eco_footprints["Ecological footprint"].max()
    political_countries_url = (
        "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
    )

    map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
    folium.Choropleth(
        geo_data=political_countries_url,
        data=eco_footprints,
        columns=["Country/region", "Ecological footprint"],
        key_on="feature.properties.name",
        bins=[0, 1, 1.5, 2, 3, 4, 5, 6, 7, 8, max_eco_footprint],
        fill_color="RdYlGn_r",
        fill_opacity=0.8,
        line_opacity=0.3,
        nan_fill_color="white",
        legend_name="Ecological footprint per capita",
        name="Countries by ecological footprint per capita",
    ).add_to(map)
    # add a toggle for the choropleth
    folium.LayerControl().add_to(map)

    return map._repr_html_()


if __name__ == "__main__":
    app.run(debug=True)
