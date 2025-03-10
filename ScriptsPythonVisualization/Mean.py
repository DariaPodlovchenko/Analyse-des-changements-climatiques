import plotly.graph_objects as go
import geopandas as gpd

mapbox_access_token = "TOKEN"

data_file = 'mean.geojson'  
europe_geojson_path = 'europe.geojson' 

gdf = gpd.read_file(data_file).dropna(subset=['geometry'])
gdf_europe = gpd.read_file(europe_geojson_path).dropna(subset=['geometry'])

def add_europe_boundaries(fig, gdf_europe):
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

def add_capitals(fig, capitals):
    fig.add_trace(go.Scattermapbox(
        lon=[capital['lon'] for capital in capitals],
        lat=[capital['lat'] for capital in capitals],
        mode='markers',
        marker=dict(size=7, color='black'),
        hovertext=[capital['name'] for capital in capitals],
        hoverinfo="text",
        showlegend=False
    ))

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
    {"name": "Skopje (Macédoine du Nord)", "lon": 21.4300, "lat": 41.9981},
    {"name": "Sofia (Bulgarie)", "lon": 23.3219, "lat": 42.6977},
    {"name": "Ljubljana (Slovénie)", "lon": 14.5058, "lat": 46.0569},
    {"name": "Sarajevo (Bosnie-Herzégovine)", "lon": 18.4131, "lat": 43.8563},
    {"name": "Tallinn (Estonie)", "lon": 24.7536, "lat": 59.4370},
    {"name": "Bratislava (Slovaquie)", "lon": 17.1077, "lat": 48.1486},
    {"name": "Podgorica (Monténégro)", "lon": 19.2594, "lat": 42.4410},
    {"name": "Lisbonne (Portugal)", "lon": -9.139, "lat": 38.7223},
    {"name": "Copenhague (Danemark)", "lon": 12.5683, "lat": 55.6761},
    {"name": "Moscou (Russie)", "lon": 37.6173, "lat": 55.7558},
    {"name": "Zagreb (Croatie)", "lon": 15.9819, "lat": 45.8150}
]


lon, lat, values = gdf.geometry.x, gdf.geometry.y, gdf['mean_temp']

fig = go.Figure()  # Создание фигуры
fig.add_trace(go.Scattermapbox(
    lon=lon,
    lat=lat,
    mode='markers',
    marker=dict(
        size=8,
        color=values,
        colorscale=[[0, 'blue'], [0.2, 'white'], [0.25, 'white'], [1, 'red']],  
        cmin=-8,  
        cmax=28,  
        colorbar=dict(
            title=dict(text="Température (°C)", font=dict(family="Montserrat", size=12, color="black")),
            tickvals=[-8, 0, 10, 20, 28],  
            ticktext=["-8", "0", "10", "20", "28"], 
            len=1, 
            thickness=20  
        )
    ),
    showlegend=False,
    hovertext=[f"Température: {value:.1f}°C<br>Coordonnées: ({lon:.2f}, {lat:.2f})" 
               for value, lon, lat in zip(values, lon, lat)],
    hoverinfo="text"
))


add_europe_boundaries(fig, gdf_europe)
add_capitals(fig, european_capitals)

fig.update_layout(
    mapbox=dict(
        accesstoken=mapbox_access_token,
        style="mapbox://styles/dariapodlovchenko/cm5noy13a000g01s36d1z0uhk", 
        center={"lat": 50, "lon": 10},  
        zoom=3  
    ),
    title={
        "text": "Moyenne des Températures journalières en Europe (1950-2023)", 
        "x": 0.5,  
        "font": {"family": "Montserrat"}  
    },
    margin=dict(
        l=250, 
        r=250,  
        t=50,   
        b=50    
    )
)

fig.update_layout(
    annotations=[
        dict(
            text="<span style='font-size: 12px;'>●   Сapitales européennes</span>",
            x=0.020,
            y=0.09,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            font=dict(size=12, color="black")
        ),
        dict(
            text=" ",
            x=0.017,
            y=0.05,
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
            y=0.05,
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
            y=0.01,
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
            y=0.01,
            xref="paper",
            yref="paper",
            showarrow=False,
            align="left",
            font=dict(size=12, color="black")
        )
    ]
)

fig.write_html("mean_temp.html")

