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

	line = {
		'type':'Feature',
		'properties':{},
		'geometry':{
			'type':'LineString',
			'coordinates':[]
		}
	}

	# sightings query
	sighting_query = 'select \
		beacons.beacon_name as Name, \
		beacons.uuid as UUID, \
		beacons.major as Major, \
		beacons.minor as Minor, \
		sightings.visit_id as Visit, \
		sightings.receiver_name as Observer, \
		sightings.latitude as Latitude, \
		sightings.longitude Longitude, \
		sightings.start_time as "Start Time", \
		sightings.end_time as "End Time" \
	from beacons inner join sightings \
	on beacons.beacon_name = sightings.beacon_name \
	where beacons.beacon_name = "' + beacon + '" ' \
	'and sightings.latitude != 0 \
	order by beacons.beacon_name, sightings.visit_id;'

	# execute sightings query
	cursor.execute(sighting_query)
	all_rows = cursor.fetchall()

	# build features
	for row in all_rows:
		props = {
			'Name':row[0],
			'UUID':row[1],
			'Major':row[2],
			'Minor':row[3],
			'Sighting':row[4],
			'Observer':row[5],
			'Start Time':row[8],
			'End Time':row[9]
		}
		geom = {
			'type':'Point',
			'coordinates':[
				row[7],
				row[6]
			]
		}
		feature = {
			'type':'Feature',
			'properties':props,
			'geometry':geom
		}
		geo['features'].append(feature)
	
		line['geometry']['coordinates'].append([
			row[7],
			row[6]
		])

	# add line feature to feature collection
	geo['features'].append(line)

	filename = beacon + '.geojson'
	with open(filename, 'w') as file:
  		json.dump(geo, file, ensure_ascii=False)
	
exit()