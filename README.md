mapper
======

Asset Tracking Mapper

This repository contains the source data files for the Coca Cola hackathon as well as some scripts to
generate geojson files.

The hackathon.db file is a SQLITE database file that contains the source data as well as imported
location addressses matching the hackathon latitude & longitude coordinates.

The factory.py file is a python script that will look for the hackathon.db in the same directory and will
generate geojson files for each beacon with the filename convention of <beacon_name>.geojson.

If you open a geojson file, github will render it in-place and you will see the map along with the beacon
sighting locations and lines interconnecting the sighting markers in the order they occurred.

Each beacon sighting marker has associated properties that are displayed in their popup including

- Name
- Date
- Location

If you are running chrome you can install an extension that will provide a gejson.io button that you can use
to open a page at geojson that will render the map there.

https://chrome.google.com/webstore/detail/geojsonio/oibjgofbhldcajfamjganpeacipebckp

You can learn more about github geojson support at this link.

https://help.github.com/articles/mapping-geojson-files-on-github/
