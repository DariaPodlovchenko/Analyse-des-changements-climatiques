import plotly.graph_objects as go
import geopandas as gpd
import json

mapbox_access_token = "TOKEN"

with open('mean_temp_period1.geojson', 'r') as f:
    data_period1 = json.load(f)

with open('mean_temp_period2.geojson', 'r') as f:
    data_period2 = json.load(f)

with open('evolution_temp.geojson', 'r') as f:
    data_evolution = json.load(f)

europe_geojson_path = 'europe.geojson'  
gdf_europe = gpd.read_file(europe_geojson_path)

gdf_europe = gdf_europe[gdf_europe.geometry.notnull()]
gdf_europe = gdf_europe[gdf_europe.geometry.type.isin(['Polygon', 'MultiPolygon'])]

def extract_and_filter_data(geojson, europe_boundary):
    points = gpd.GeoDataFrame(
        {
            "value": [feature['properties']['value'] for feature in geojson['features']],
            "geometry": gpd.points_from_xy(
                [feature['geometry']['coordinates'][0] for feature in geojson['features']],
                [feature['geometry']['coordinates'][1] for feature in geojson['features']]
            )
        }
    )
    filtered_points = gpd.clip(points, europe_boundary)
    return (
        filtered_points.geometry.x.tolist(),
        filtered_points.geometry.y.tolist(),
        filtered_points['value'].tolist()
    )

europe_boundary = gdf_europe.unary_union

lon1, lat1, values1 = extract_and_filter_data(data_period1, europe_boundary)
lon2, lat2, values2 = extract_and_filter_data(data_period2, europe_boundary)
lon_evo, lat_evo, values_evo = extract_and_filter_data(data_evolution, europe_boundary)

gdf_europe["hover_text"] = gdf_europe["NAME_FREN"]

european_capitals = [
    {"name": "Paris (France)", "lon": 2.3522, "lat": 48.8566},
    {"name": "Berlin (Allemagne)", "lon": 13.405, "lat": 52.52},
    {"name": "Madrid (Espagne)", "lon": -3.7038, "lat": 40.4168},
    {"name": "Rome (Italie)", "lon": 12.4964, "lat": 41.9028},
    {"name": "Oslo (Norvège)", "lon": 10.7522, "lat": 59.9139},
    {"name": "Berne (Suisse)", "lon": 7.4474, "lat": 46.9481},
    {"name": "Londres (Royaume-Uni)", "lon": -0.1278, "lat": 51.5074},
    {"name": "Stockholm (Suède)", "lon": 18.0686, "lat": 59.3293},
    {"name": "Helsinki (Finlande)", "lon": 24.9384, "lat": 60.1695},
    {"name": "Kiev (Ukraine)", "lon": 30.5238, "lat": 50.4501},
    {"name": "Vilnius (Lituanie)", "lon": 25.2797, "lat": 54.6872},
    {"name": "Riga (Lettonie)", "lon": 24.1052, "lat": 56.9496},
    {"name": "Varsovie (Pologne)", "lon": 21.0122, "lat": 52.2297},
    {"name": "Minsk (Biélorussie)", "lon": 27.5615, "lat": 53.9006},
    {"name": "Belgrade (Serbie)", "lon": 20.4573, "lat": 44.8176},
    {"name": "Istanbul (Turquie)", "lon": 28.9784, "lat": 41.0082},
    {"name": "Chisinau (Moldavie)", "lon": 28.8575, "lat": 47.0105},
    {"name": "Athènes (Grèce)", "lon": 23.7275, "lat": 37.9838},
    {"name": "Prague (République tchèque)", "lon": 14.4378, "lat": 50.0755},
    {"name": "Budapest (Hongrie)", "lon": 19.0402, "lat": 47.4979},
    {"name": "Bucarest (Roumanie)", "lon": 26.1025, "lat": 44.4268},
    {"name": "Bruxelles (Belgique)", "lon": 4.3517, "lat": 50.8503},
    {"name": "Amsterdam (Pays-Bas)", "lon": 4.9041, "lat": 52.3676},
    {"name": "Dublin (Irlande)", "lon": -6.2603, "lat": 53.3498},
    {"name": "Vienne (Autriche)", "lon": 16.3738, "lat": 48.2082},
    {"name": "Tirana (Albanie)", "lon": 19.8189, "lat": 41.3275},
    {"name": "Skopje (Macédoine du Nord)", "lon": 21.43, "lat": 41.9981},
    {"name": "Sofia (Bulgarie)", "lon": 23.3219, "lat": 42.6977},
    {"name": "Ljubljana (Slovénie)", "lon": 14.5058, "lat": 46.0569},
    {"name": "Sarajevo (Bosnie-Herzégovine)", "lon": 18.4131, "lat": 43.8563},
    {"name": "Tallinn (Estonie)", "lon": 24.7536, "lat": 59.437},
    {"name": "Bratislava (Slovaquie)", "lon": 17.1077, "lat": 48.1486},
    {"name": "Podgorica (Monténégro)", "lon": 19.2594, "lat": 42.441},
    {"name": "Lisbonne (Portugal)", "lon": -9.139, "lat": 38.7223},
    {"name": "Copenhague (Danemark)", "lon": 12.5683, "lat": 55.6761},
    {"name": "Moscou (Russie)", "lon": 37.6173, "lat": 55.7558},
    {"name": "Zagreb (Croatie)", "lon": 15.9819, "lat": 45.815}
]

fig = go.Figure()

fig.add_trace(go.Scattermapbox(
    lon=lon1,
    lat=lat1,
    mode='markers',
    marker=dict(
        size=8,
        color=values1,
        colorscale=[[0, 'blue'], [0.18, 'white'], [0.19, 'white'], [1, 'red']],
        colorbar=dict(
            title=dict(
                text="Température (°C)",
                font=dict(family="Montserrat", size=12, color="black")
            ),
            tickvals=[-5, 0, 5, 10, 15, 20],
            ticktext=["-5", "0", "5", "10", "15", "20"]
        ),
        showscale=True
    ),
    hovertext = [f"Température: {value:.1f}°C<br>Coordonnées: ({lon:.2f}, {lat:.2f})" 
             for value, lon, lat in zip(values1, lon1, lat1)],
    hoverinfo="text",
    name="1950-1986",
    visible=True,
    showlegend=False
))

fig.add_trace(go.Scattermapbox(
    lon=lon2,
    lat=lat2,
    mode='markers',
    marker=dict(
        size=8,
        color=values2,
        colorscale=[[0, 'blue'], [0.12, 'white'], [0.13, 'white'], [1, 'red']],
        colorbar=dict(
            title=dict(
                text="Température (°C)",
                font=dict(family="Montserrat", size=12, color="black")
            ),
            tickvals=[-5, 0, 5, 10, 15, 20],
            ticktext=["-5", "0", "5", "10", "15", "20"]
        ),
        showscale=True
    ),
    hovertext = [f"Température: {value:.1f}°C<br>Coordonnées: ({lon:.2f}, {lat:.2f})" 
             for value, lon, lat in zip(values1, lon1, lat1)],
    hoverinfo="text",
    name="1987-2023",
    visible=False,
    showlegend=False
))

fig.add_trace(go.Scattermapbox(
    lon=lon_evo,
    lat=lat_evo,
    mode='markers',
    marker=dict(
        size=8,
        color=values_evo,
        colorscale=[[0, 'blue'], [0.19, 'white'], [0.2, 'white'], [1, 'red']],
        colorbar=dict(
            title=dict(
                text="Évolution Température (°C)",
                font=dict(family="Montserrat", size=12, color="black")
            )
        ),
        showscale=True
    ),
    hovertext = [f"Évolution: {value:.1f}°C<br>Coordonnées: ({lon:.2f}, {lat:.2f})" 
             for value, lon, lat in zip(values1, lon1, lat1)],
    hoverinfo="text",
    name="Évolution",
    visible=False,
    showlegend=False
))

fig.add_trace(go.Scattermapbox(
    lon=[capital['lon'] for capital in european_capitals],
    lat=[capital['lat'] for capital in european_capitals],
    mode='markers',
    marker=dict(size=7, color='black'),
    hovertext=[capital['name'] for capital in european_capitals],
    hoverinfo="text",
    showlegend=False
))

for _, row in gdf_europe.iterrows():
    if row.geometry.geom_type == "Polygon":
        x, y = row.geometry.exterior.xy
        fig.add_trace(go.Scattermapbox(
            lon=list(x),
            lat=list(y),
            mode="lines",
            line=dict(width=1, color="grey"),
            hoverinfo="none",
            showlegend=False
        ))
    elif row.geometry.geom_type == "MultiPolygon":
        for poly in row.geometry.geoms:
            x, y = poly.exterior.xy
            fig.add_trace(go.Scattermapbox(
                lon=list(x),
                lat=list(y),
                mode="lines",
                line=dict(width=1, color="grey"),
                hoverinfo="none",
                showlegend=False
            ))

total_traces = len(fig.data)

fig.update_layout(
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="mapbox://styles/dariapodlovchenko/cm5noy13a000g01s36d1z0uhk", 
        center={"lat": 50, "lon": 10},  
        zoom=3  
    ),
    title={
        "text": "Températures journalières moyennes en Europe (1950-1986)",
        "x": 0.5,
        "font": {"family": "Montserrat"}
    },
    margin=dict(l=250, r=250, t=50, b=50),
    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            x=0.28,
            y=0.08,
            buttons=[
                dict(
                    label="1950-1986",
                    method="update",
                    args=[
                        {"visible": [True, False, False] + [True]*(total_traces - 3)},
                        {"title.text": "Températures journalières moyennes en Europe (1950-1986)"}
                    ]
                ),
                dict(
                    label="1987-2023",
                    method="update",
                    args=[
                        {"visible": [False, True, False] + [True]*(total_traces - 3)},
                        {"title.text": "Températures journalières moyennes en Europe (1987-2023)"}
                    ]
                ),
                dict(
                    label="Évolution",
                    method="update",
                    args=[
                        {"visible": [False, False, True] + [True]*(total_traces - 3)},
                        {"title.text": "Evolution des températures journalières moyennes en Europe (1950-1986 vs 1987-2023)"}
                    ]
                )
            ]
        )
    ]
)

fig.update_layout(
    annotations=[
        dict(
            text="<span style='font-size: 12px;'>●   Сapitales européennes</span>",
            x=0.020,
            y=0.2,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            font=dict(size=12, color="black")
        ),
        dict(
            text=" ",
            x=0.017,
            y=0.16,
            xref="paper",
            yref="paper",
            xanchor="left",
            yanchor="bottom",
            showarrow=False,
            bgcolor="#EBEBEB",  
            bordercolor="black",
            borderwidth=1,
            width=13,
            height=13
        ),
        dict(
            text="<span style='font-size: 12px;'> Pas de données</span>",
            x=0.035,
            y=0.16,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            font=dict(size=12, color="black")
        )
        ,
        dict(
            text=" ",
            x=0.017,
            y=0.12,
            xref="paper",
            yref="paper",
            xanchor="left",
            yanchor="bottom",
            showarrow=False,
            bgcolor="#C7E2FF",  
            bordercolor="black",
            borderwidth=1,
            width=13,
            height=13
        ),
        dict(
            text="<span style='font-size: 12px;'> Zones d'eau</span>",
            x=0.035,
            y=0.12,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            font=dict(size=12, color="black")
        )
    ]
)


fig.write_html("evolution_map.html")
