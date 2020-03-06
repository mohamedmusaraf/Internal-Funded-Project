from firebase import firebase
#import firebase_admin
#from firebase_admin import db,credentials
#import time
from tkinter import *


win=Tk()
win.title('sample data')
win.geometry('500x500')


listbox=Listbox(win,height=20,width=500)
listbox.pack()

label=Label(win,text="")
label.pack()


firebase=firebase.FirebaseApplication('https://sensordb-eb5ba.firebaseio.com/',None)
#cred = credentials.Certificate('firebase_credentials/sensorDB-65afdd6c3963.json')
#firebase_admin.initialize_app(cred,{'databaseURL':'https://sensordb-eb5ba.firebaseio.com/'})
#ref=db.reference('sensordb-eb5ba/sensors/')




data=firebase.get('sensors/','')

keys=list(data.keys())


def list_update():

	var=listbox.curselection()
	
	if len(var)==0:
		new_list()
	else:
		string=str(listbox.get(ACTIVE))
		array=string.split('--')
		global data
		global keys
		ind=0
		print(keys)
		for i in range(len(keys)):
			if 	data[keys[i]]['Time']==array[4] and data[keys[i]]['Serviced']=="0":
				ind=i
				break
		print(ind)
		listbox.delete(var)
		firebase.put('sensors/{}'.format(keys[ind]),'Serviced',"1")	


service_but=Button(win,text="Serviced?",command=list_update)
service_but.pack()



def list_populate():
	flag=0
	for i in range(len(keys)):
		if data[keys[i]]['Serviced']=="0":
			label['text']=""
			lat=data[keys[i]]['Lat']
			lon=data[keys[i]]['Long']
			serviced=data[keys[i]]['Serviced']
			Type=data[keys[i]]['Type']
			Time=data[keys[i]]['Time']
			flag=1

			listbox.insert(END,'{}--{}--{}--{}--{}'.format(lat,lon,serviced,Type,Time))
	if flag==0:
		label['text']="no more records to be serviced"
		
		
	
			#firebase.put('sensordb-eb5ba/sensors/{}'.format(keys[i]),'Serviced','1')

def new_list():
	
	global data
	data=firebase.get('sensors/','')
	global keys
	keys=list(data.keys())
	print(len(keys))
	list_populate()

	

list_populate()
	
win.mainloop()







