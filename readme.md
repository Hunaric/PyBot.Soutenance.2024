# Projet Python de géolocalisation pour le robot policier (Commande vocale)

Developpé par deux etudiants de GASA FORMATION en 3ème année de licence
- **FANGNON Hugues Nathanael**
- **YESSOUFOU Walyi**

## Objectif du projet

Notre université a conçu un robot policier capable de gérer la circulation à Cotonou afin de réduire les embouteillages.
Pour lui permettre d’indiquer des lieux que les citoyens ou les touristes peuvent rechercher, il nous a été demandé de concevoir une interface intelligente capable d’écouter et de répondre.

Étant donné que la façon dont les Béninois indiquent un lieu est particulière — les rues étant souvent peu connues de la majorité des citoyens —, nous avons dû programmer le robot pour qu’il comprenne et s’exprime comme un Béninois le ferait lorsqu’il donne une indication de lieu.

## Tâches pour la réalisation

Nous avons commencé par utiliser une base de données géographique trouvée sur Hot Export Tool, mais celle-ci n’était pas totalement à jour concernant certaines localités du Bénin. Pour compléter et fiabiliser nos informations, nous avons intégré les données issues des travaux de Lionel TODOME, diplômé en géomatique à CY Paris Cergy Université et administrateur SIG. Ses recherches nous ont été d’une grande utilité.

Il est important de noter que la norme de référence spatiale utilisée au Bénin pour l’annotation des systèmes de coordonnées est le EPSG:32631. Ce système est particulier car il présente la longitude avant la latitude et prend également en compte l’altitude. Il est adapté aux travaux à l’échelle nationale, ce qui nous a conduits à convertir la base de données exportée depuis Hot Export Tool, initialement en CRS:84 (WGS 84), vers le EPSG:32631.

Cette conversion a été réalisée grâce à la bibliothèque Python GeoPandas, qui s’appuie sur la bibliothèque PyProj pour la gestion des systèmes de coordonnées et des transformations géographiques.
Nous avons ainsi pu cartographier le département à l’aide d’un GeoDataFrame, facilitant la visualisation et la manipulation spatiale des données. 

### Difficultés et insuffisances

La principale difficulté rencontrée concernait l’appellation des lieux, car la reconnaissance vocale s’est révélée complexe en raison de l’accent béninois et des variantes linguistiques locales. Pour pallier ce problème, nous avons adopté une approche approximative permettant à notre interface d’identifier et de localiser certains lieux malgré ces contraintes.

Le projet étant centré sur l’écoute et la réponse vocale, nous n’avons pas développé de version graphique ou textuelle de l’application. L’essentiel de notre travail s’est donc concentré sur l’extraction, le nettoyage et la transformation de la base de données en données exploitables, afin de permettre au robot d’interagir efficacement avec les utilisateurs.

## Le Mémoire de recherche

[📄 Consulter le rapport complet (PDF)](./Memoire_complet.pdf)



## Pour l'installer:

Ouvrir le terminal dans le repertoire du projet et suivez les etapes:
- S'assurer d'avoir virtualenv d'installer avec python : `pip install virtualenv`
- Creer l'environnement virtuel : `py -m venv venv`
- Lancer l'environnemnent virtuel:
    - Sous Windows : `.\venv\Scripts\activate`
    - Sous Unix et MacOS : `source venv/bin/activate`
- Installer les dependances necessaire en excutant: `pip install -r requirements.txt`
- Executer ensuite le fichier main.py `& ./venv/Scripts/python.exe main.py`
