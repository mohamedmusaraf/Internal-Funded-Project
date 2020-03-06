import requests
api_key="AIzaSyArBRi4XDa5VtIqlTBiu1sutN0GLQV1QDM"

url='https://maps.googleapis.com/maps/api/staticmap?'

location=input('enter location: ')
center=location
zoom=10
r=requests.get(url+'center='+center+'&zoom='+str(zoom)+'&size=1024x768&key='+api_key)

print(url+'center='+center+'&zoom='+str(zoom)+'&size=1024x768&key='+api_key)



