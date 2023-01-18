import folium
import pandas as pd

eco_footprints = pd.read_csv("footprint.csv")
political_countries_url = (
    "http://geojson.xyz/naturalearth-3.3.0/ne_50m_admin_0_countries.geojson"
)

map = folium.Map(location=(30, 10), zoom_start=3, tiles="cartodb positron")
folium.Choropleth(
    geo_data=political_countries_url,
    data=eco_footprints,
    columns=["Country/region", "Ecological footprint"],
    key_on="feature.properties.name",
).add_to(map)

map.save("footprint.html")