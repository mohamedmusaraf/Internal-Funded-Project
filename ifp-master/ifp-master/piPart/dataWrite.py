import csv
import time

with open('data.csv',mode='a') as file:
	writer=csv.writer(file,delimiter=',')

	for i in range(10):
		writer.writerow([12,12,1,'12:00PM'])
		print('inserted')
		time.sleep(2)