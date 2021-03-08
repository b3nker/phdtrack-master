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
	for line in f :
		newUser = line.split(",")[0]
		currentUser = newUser
		curFile = open(outputDirectory+"/"+newUser + ".csv", "a")
		curFile.write("id_user, lat, long, timestamp\n")
		while currentUser == newUser :
			data = line.split(",")
			newUser = data[0]
			timeStamp = data[1]
			coordonates = data[2]
			values = coordonates.split("|")
			latitude = values[0]
			longitude = values[1].rstrip("\n")
			dt = datetime.strptime(timeStamp,'%Y-%m-%d %H:%M:%S')
			timestamp_ms = dt.timestamp() * 1000
			timestamp_ms_str = str(timestamp_ms)
			curFile.write(newUser+","+latitude+","+longitude+","+timestamp_ms_str+"\n")
			line = next(f)
			i=i+1
			print(i)
		
		curFile.close()
		if i>1000000 :
			break

endTimer = time.time()
totalTime = endTimer - startTimer
print(totalTime,"sec")

	