import csv
import time
from firebase import firebase

firebase=firebase.FirebaseApplication('https://sensordb-eb5ba.firebaseio.com/',None)

with open('data.csv') as csvfile:
	reader=csv.reader(csvfile,delimiter=',')
	for row in reader:

		data={
				'Lat':row[0],
				'Long':row[1],
				'Type':row[2],
				'Time':row[3],
				'Serviced':"0"
			}
		result=firebase.post('/sensordb-eb5ba/sensors/',data)
		print(result)

		




