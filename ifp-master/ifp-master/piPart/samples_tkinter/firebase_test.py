from firebase import firebase

firebase=firebase.FirebaseApplication('https://sensordb-eb5ba.firebaseio.com/sensordb-eb5ba/',None)

result=firebase.get('/sensordb-eb5ba/sensors/','')
print(result)
