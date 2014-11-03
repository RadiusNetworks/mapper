import sqlite3
import json

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('./hackathon.db')
cursor = db.cursor()

# beacon query
beacon_query = 'select beacons.beacon_name from beacons;'
cursor.execute(beacon_query)
all_rows = cursor.fetchall()

# build features
for row in all_rows:
	beacon = row[0]

	geo = {
		'type':'FeatureCollection',
		'features':[]
	}

# 	line = {
# 		'type':'Feature',
# 		'properties':{},
# 		'geometry':{
# 			'type':'LineString',
# 			'coordinates':[]
# 		}
# 	}

	# sightings query
	sighting_query = 'select \
		sightings.beacon_name as Name, \
		sightings.latitude as Latitude, \
		sightings.longitude Longitude, \
		sightings.start_time as "Date", \
		locations.location as "Location" \
	from sightings inner join locations \
	on sightings.latitude = locations.latitude \
	and sightings.longitude = locations.longitude \
	where sightings.latitude != 0	\
	and sightings.beacon_name = "' + beacon + '" ' \
	'order by sightings.beacon_name, sightings.start_time;'

	# execute sightings query
	cursor.execute(sighting_query)
	all_rows = cursor.fetchall()

	# build features
	for row in all_rows:
		
		props = {
			'Name':row[0],
			'Date':row[3],
			'Location':row[4]
		}
		geom = {
			'type':'Point',
			'coordinates':[
				row[2],
				row[1]
			]
		}
		feature = {
			'type':'Feature',
			'properties':props,
			'geometry':geom
		}
		geo['features'].append(feature)
	
# 		line['geometry']['coordinates'].append([
# 			row[2],
# 			row[1]
# 		])
# 
# 	# add line feature to feature collection
# 	geo['features'].append(line)

	filename = beacon + '.geojson'
	print filename
	print geo
	with open(filename, 'w') as file:
  		json.dump(geo, file)
	
exit()