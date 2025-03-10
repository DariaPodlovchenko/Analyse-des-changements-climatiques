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

Fonctionnalités
- Pandas (Python) – Manipulation des données climatiques (nettoyage, tri, agrégation).  
- ncdf4 (R) – Extraction et traitement des données NetCDF.  
- Matplotlib (Python) / Plotly (Python) – Création de visualisations cartographiques (cartes statiques et interactives).  
- Folium (Python) – Intégration des cartes dans une interface interactive pour une exploration dynamique.  
- R – Analyse statistique et génération des cartes climatiques.  

