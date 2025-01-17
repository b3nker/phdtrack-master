

import time
import sys
import os
import numpy as np
import math
import itertools
import pandas as pd
import datetime as dt
import ntpath
import concurrent.futures
import psutil
import time

def splitTraceByTimeGamp(trace,minGap):
	df = pd.read_csv(trace,names=['lat','lng','timestamp'])
	print(df)
	try:
		df['timestamp']=pd.to_datetime(df['timestamp'], unit='ms')
	except:
		df['timestamp']=pd.to_datetime(df['timestamp'])
	df['gap'] = df['timestamp'].diff() >  dt.timedelta(seconds=minGap)
	df['gap'] = df['gap'].apply(lambda x: 1 if x else 0).cumsum()
	return dict(tuple( df.groupby('gap')))

def splitTraceByFixedSlices(trace,sliceSize):
	#try:
	df = pd.read_csv(trace,names=['id_user', 'lat','lng','timestamp'],header=0)
	df['timestamp']=pd.to_datetime(df['timestamp'], unit='ms')
	#df['bin'] = df['timestamp']#.apply(lambda x: x)
	minTime= df['timestamp'].min()
	#df['bin'] = df['timestamp'].apply(lambda x: (x-pd.Timestamp.min).total_seconds() // sliceSize)
	df['bin'] = df['timestamp'].apply(lambda x: (x-minTime).total_seconds() // sliceSize)
	listBins=list(df['bin'].unique())
	#print(listBins)
	df['bin']=df['bin'].apply(lambda x: listBins.index(x))
	#except Exception as e:
	#	print("Exception:")
	#	print("\n\n"+str(e))
	#	print(traceback.format_exc())
	#	raise(e)
	#print(df['timestamp'])
	return dict(tuple( df.groupby('bin')))

def getTraceDuration(dataframe):
	dataframe['timestamp']=pd.to_datetime(dataframe['timestamp'])#, unit='ms')
	minTime= dataframe['timestamp'].min()
	maxTime= dataframe['timestamp'].max()
	#print(minTime,maxTime)
	return (maxTime - minTime).total_seconds() 

def processCsvTraceFile(filename,inputDirectory,outputDirectory,sliceSize):
	trace=os.path.join(inputDirectory, filename)
	name=ntpath.basename(trace).replace('.csv', '')
	outDfSet= splitTraceByFixedSlices(trace,sliceSize)
	#print(trace+" size="+str(len(outDfSet)))
	cpt=0
	for key, value in outDfSet.items():
		#print(os.path.join(outputDirectory, name+"_"+str(int(key))+".csv"))
		#print(value)
#		nbRecord=len(value)
#		traceDuration= getTraceDuration(value)
#		if int(nbRecord) >= minRecord and traceDuration >= minDuration:
		value['timestamp']=value['timestamp'].apply(lambda x :"%d" % (time.mktime( x.timetuple())*1000+ x.microsecond/1000) )
		value.to_csv(os.path.join(outputDirectory, name+"-"+str(int(key))+".csv"),index=False,columns=['id_user','lat','lng','timestamp'],header=False)
#			cpt=cpt+1




#Start of script

NB_PROCESS = psutil.cpu_count(logical=False)


#Start timer
start_time = time.time()
#inputs
inputDirectory = sys.argv[1]
outputDirectory = sys.argv[2]
sliceSize = int(sys.argv[3]) # in seconds
#minRecord = int(sys.argv[4]) # number of record 
#minDuration=int(sys.argv[5]) # min time duration of a trace in seconds

# mkdir the output directory
if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)


# Create pool of processes
executor = concurrent.futures.ProcessPoolExecutor(NB_PROCESS)

# For each trace launch the trace processing job
futures = [executor.submit(processCsvTraceFile,filename,inputDirectory,outputDirectory,sliceSize) for filename in os.listdir(inputDirectory) if filename.endswith(".csv")]
#futures = [processCsvTraceFile(filename,inputDirectory,outputDirectory,sliceSize) for filename in os.listdir(inputDirectory) if filename.endswith(".csv")]


# Wait for the processes to finish
concurrent.futures.wait(futures)

#End timer
end_time = time.time()
print("Spliting dataset per traces\nExecution time : ",end_time - start_time, " sec")





