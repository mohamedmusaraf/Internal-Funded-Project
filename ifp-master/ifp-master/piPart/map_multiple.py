#links for plotting multiple places in google maps

#https://www.geeksforgeeks.org/python-plotting-google-map-using-gmplot-package/
#https://www.tutorialspoint.com/plotting-google-map-using-gmplot-package-in-python



# Import gmplot library.
from gmplot import *
# Place map
# First two arugments are the geogrphical coordinates .i.e. Latitude and Longitude
#and the zoom resolution.
gmap = gmplot.GoogleMapPlotter(17.438139, 78.39583, 18)

gmap.apikey="AIzaSyArBRi4XDa5VtIqlTBiu1sutN0GLQV1QDM" ##wont work because your api is faulty without billing account
# Location where you want to save your file.
gmap.draw('/home/karthik/Desktop/ifp/viewMap.html')