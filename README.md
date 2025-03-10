<h1 align="center">Analyse des changements climatiques en Europe<br>basée sur les données E-OBS (1950–2023)</h1>

Ce projet analyse les variations des températures moyennes en Europe entre 1950 et 2023 à l’aide des données météorologiques E-OBS. L’objectif est de démontrer le rôle essentiel de la géomatique et des SIG dans le suivi et la compréhension des évolutions climatiques. L’approche repose sur le traitement des données climatiques en Python et R, avec des visualisations interactives et cartographiques pour analyser les tendances du réchauffement climatique.  

*Mots-clés : SIG, Python, R, Pandas, NetCDF, Plotly (Python), Folium (Python)*

Points clés :
- Traitement des données climatiques : Chargement et analyse des données NetCDF issues d’E-OBS pour extraire les températures minimales et maximales journalières.  
- Standardisation et nettoyage des données : Filtrage des données météorologiques pour exclure les valeurs aberrantes et supprimer les jours bissextiles.  
- Analyse des tendances climatiques : Comparaison des températures entre deux périodes distinctes (1950-1986 et 1987-2023) pour identifier les évolutions spatiales du réchauffement climatique.  
- Visualisation interactive : Développement d’une interface web en Python avec Plotly (Python) pour afficher les cartes climatiques dynamiques.  
- Représentation cartographique des températures :  
  - Carte des températures minimales journalières moyennes en Europe (1950–2023)  
  - Carte des températures maximales journalières moyennes en Europe (1950–2023)  
  - Carte du climat moyen en Europe (1950–2023)
  - Carte de l’évolution des températures journalières moyennes (1950–1986 vs 1987–2023)
  - Carte du nombre moyen de jours de gel (1991–2020)
  - Animation de l’évolution du nombre de jours de gel (1950–2023, GIF)  

<br> <br>
Fonctionnalités :
- Pandas (Python) – Manipulation des données climatiques (nettoyage, tri, agrégation).  
- ncdf4 (R) – Extraction et traitement des données NetCDF.  
- Matplotlib (Python) / Plotly (Python) – Création de visualisations cartographiques (cartes statiques et interactives).  
- Folium (Python) – Intégration des cartes dans une interface interactive pour une exploration dynamique.  
- R – Analyse statistique et génération des cartes climatiques.

<br> <br>
📂 **DataFormatGeoJsonVisualization**  
Ce dossier contient les fichiers GeoJSON utilisés pour la visualisation des données spatiales. Ces fichiers permettent d'afficher les résultats sur des cartes interactives. 

📂 **ScriptsPythonVisualization**  
Ce dossier regroupe les scripts Python dédiés à la visualisation des données climatiques. Il inclut la génération de cartes interactives avec **Plotly** et **Folium**. 

📂 **ScriptsR**  
Ce dossier contient les scripts R pour le traitement et l’analyse des données climatiques. Il inclut l'extraction des données NetCDF, les calculs statistiques et la création de cartes statiques. 

<br> <br>
Exemple de carte interactive : Températures journalières moyennes en Europe (1950-1986)
- Affichage des informations au survol** : En plaçant le curseur sur une zone, une infobulle affiche la **température moyenne (°C)** et les **coordonnées géographiques (latitude, longitude)**.
- Échelle de couleurs :  
   - Rouge foncé → Températures les plus élevées  
   - Bleu → Températures les plus basses
- Points noirs : Localisation des capitales européennes
- Légende dynamique :  
   - Zones sans données (blanc)  
   - Étendues d’eau (bleu clair)
- Boutons de navigation : Permettent de passer entre **1950-1986, 1987-2023 et l'évolution des températures**.  

<div align="center">
    <img src="https://github.com/DariaPodlovchenko/Analyse-des-changements-climatiques/raw/main/MapEx.jpg" width="600">
</div>


<br> <br>
Source des données : 
<br>Site E-OBS : https://www.ecad.eu/download/ensembles/download.php 
<br>Data : https://surfobs.climate.copernicus.eu/dataaccess/access_eobs.php#datafiles

Les données utilisées dans ce projet proviennent de la base **E-OBS** (Ensemble Observational Dataset), issue du **European Climate Assessment & Dataset (ECA&D)**. Ce jeu de données météorologiques en accès libre regroupe des observations provenant de nombreuses stations réparties à travers l’Europe.  

Pour cette étude, la **version 29** d’E-OBS a été exploitée, couvrant la période de **1950 à 2023**. Ce jeu de données contient plusieurs variables climatiques, notamment : Température minimale quotidienne (TN), Température maximale quotidienne (TX), Température moyenne quotidienne (TG), Somme quotidienne des précipitations (RR), Pression moyenne au niveau de la mer (PP), Vitesse moyenne quotidienne du vent (FG), Humidité relative moyenne quotidienne (HU), Radiation globale (QQ).

*Dans ce projet, seules les **températures minimales (TN) et maximales (TX)** ont été sélectionnées pour l’analyse. Les valeurs de ces variables ont été calculées par interpolation, en prenant en compte les observations des stations météorologiques, le relief, la distance aux côtes et les régularités climatiques. La résolution spatiale des données est de **0,25°** (environ 25 km²), et la zone d’étude couvre l’Europe entre **34° et 72° de latitude nord** et **-12° et 42° de longitude**. Les données sont fournies sous **format NetCDF**, largement utilisé en climatologie pour stocker et traiter des données multidimensionnelles.*
