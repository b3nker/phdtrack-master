import sys
import os
import time
from datetime import datetime

datasetPath = sys.argv[1]
outputDirectory = sys.argv[2]
numberOfLine = int(sys.argv[3])

if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)

startTimer = time.time()
with open(datasetPath) as f:
	next(f)
	i = 1
	new_id_user = 1
	curFile = open(outputDirectory+"/"+str(new_id_user) + ".csv", "a")
	tmp_line = next(f)
	data = tmp_line.split(",")
	timeStamp = data[1]
	coordonates = data[2]
	values = coordonates.split("|")
	longitude = values[0]
	latitude = values[1].rstrip("\n")
	dt = datetime.strptime(timeStamp,'%Y-%m-%d %H:%M:%S')
	timestamp_ms = int(dt.timestamp() * 1000)
	timestamp_ms_str = str(timestamp_ms)
	curFile.write(str(new_id_user)+","+latitude+","+longitude+","+timestamp_ms_str+"\n")
	currentUser = data[0]
	
	for line in f :
		data = line.split(",")
		newUser = data[0]
		if currentUser != newUser :
			curFile.close()
			new_id_user = new_id_user + 1
			currentUser = newUser
			curFile = open(outputDirectory+"/"+str(new_id_user) + ".csv", "a")

		timeStamp = data[1]
		coordonates = data[2]
		values = coordonates.split("|")
		longitude = values[0]
		latitude = values[1].rstrip("\n")
		dt = datetime.strptime(timeStamp,'%Y-%m-%d %H:%M:%S')
		timestamp_ms = int(dt.timestamp() * 1000)
		timestamp_ms_str = str(timestamp_ms)
		curFile.write(str(new_id_user)+","+latitude+","+longitude+","+timestamp_ms_str+"\n")			
		i=i+1
		if i>=numberOfLine :
			break

endTimer = time.time()
totalTime = endTimer - startTimer
print("Execution time splitting the dataset by user : ",totalTime,"sec")

