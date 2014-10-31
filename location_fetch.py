import sqlite3
from geopy.geocoders import Nominatim
geolocator = Nominatim()

# Creates or opens a file called mydb with a SQLite3 DB
db = sqlite3.connect('./hackathon.db')
cursor = db.cursor()

# location query
location_query = 'select \
	latitude, longitude, location \
	from locations \
	where location isnull'
	
cursor.execute(location_query)
all_rows = cursor.fetchall()

# build features
for row in all_rows:

	location = geolocator.reverse([row[0], row[1]])
	address = location.address
	lat = str(row[0])
	long = str(row[1])
	
	update_query = 'update locations \
		set location = "?" \
		where latitude = ? and longitude = ?'
		
	cursor.execute("update locations set location = ? \
		where latitude = ? and longitude = ?", \
		(address, lat, long))
	db.commit()
	print(address)
	
exit()
