import sys
import os
import time
from datetime import datetime

datasetPath = sys.argv[1]
outputDirectory = sys.argv[2]

if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)

currentUser = ""

startTimer = time.time()
with open(datasetPath) as f:
	next(f)
	i = 0
	new_id_user = 1
	for line in f :
		newUser = line.split(",")[0]
		currentUser = newUser
		#curFile = open(outputDirectory+"/"+newUser + ".csv", "a")
		curFile = open(outputDirectory+"/"+str(new_id_user) + ".csv", "a")
		#curFile.write("id_user, lat, lng, timestamp\n")
		while currentUser == newUser :
			data = line.split(",")
			newUser = data[0]
			timeStamp = data[1]
			coordonates = data[2]
			values = coordonates.split("|")
			latitude = values[0]
			longitude = values[1].rstrip("\n")
			dt = datetime.strptime(timeStamp,'%Y-%m-%d %H:%M:%S')
			timestamp_ms = int(dt.timestamp() * 1000)
			timestamp_ms_str = str(timestamp_ms)
			curFile.write(str(new_id_user)+","+latitude+","+longitude+","+timestamp_ms_str+"\n")
			#curFile.write(newUser+","+latitude+","+longitude+","+timestamp_ms_str+"\n")
			line = next(f)
			i=i+1
			#print(i)
		
		curFile.close()
		new_id_user = new_id_user + 1
		if i>1000 :
			break

endTimer = time.time()
totalTime = endTimer - startTimer
print(totalTime,"sec")

