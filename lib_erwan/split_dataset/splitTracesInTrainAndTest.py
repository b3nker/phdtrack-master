import sys
import os
import time
import numpy as np
import math
import itertools
import pandas as pd
import datetime as dt
import ntpath
import concurrent.futures
import psutil
import shutil

def copyTrainTest(name,seq,total,percentile,inputDirectory,trainDir,testDir):
	if int(seq)/float(total) <= percentile:
		shutil.copyfile(inputDirectory+str(name)+'.csv',trainDir+'/'+ str(name)+'.csv')
	else:
		shutil.copyfile(inputDirectory+str(name)+'.csv',testDir+'/'+ str(name)+'.csv')

startTimer = time.time()

#inputs
inputDirectory = sys.argv[1]
train = sys.argv[2]
test=sys.argv[3]
ratio=0.5

if len(sys.argv)>4:
	ratio=float(sys.argv[4])

#print("ratio==",ratio)

# mkdir the output directory
if not os.path.exists(train):
	os.makedirs(train)

# mkdir the output directory
if not os.path.exists(test):
	os.makedirs(test)

files = [filename.split('.')[0] for filename in os.listdir(inputDirectory) if filename.endswith(".csv")]

#print(files)
serie=pd.Series(files)

#print("Serie==",serie)
df=serie.str.split('-',expand=True)

#print("df==",df)
#print("df max==",df[1].max())
for c in df.columns[1:]:
	#print(c)
	df[c]=df[c].apply(int)

#print("new df ==",df)
df=df.sort_values(by=list(df.columns),axis=0)

#print("df sort ==",df)
df['name']=df[0]

#print(df['name'])
#print("new df ==",df)

for c in df.columns[1:]:
	if c != 'name':
		#print(df[c].astype(str))
		df['name']=df['name']+'-'+df[c].astype(str)


df['count']=df.groupby(0)['name'].transform('count')
df=df.reset_index()
total=len(df)
#print(df)

seq=4546464
currentUser=''

for index, row in df.iterrows():
	#print("row=",row)
	if currentUser == row[0]:
		seq=seq+1
	else:
	    seq=0
	#print(row['name'],seq,row['count'], row[0])
	copyTrainTest(row['name'],seq,row['count'],ratio,inputDirectory,train,test)
	currentUser=row[0]

endTimer = time.time()
totalTime = endTimer - startTimer
print("Execution time splitting the dataset in train and test directory : ",totalTime,"sec")
