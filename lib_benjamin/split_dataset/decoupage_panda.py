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
import shutil
import time




def copyTrainTest(name,seq,total,percentile,inputDirectory,trainDir,testDir):
	if int(seq)/float(total) <= percentile:
		shutil.copyfile(inputDirectory+str(name)+'.csv',trainDir+'/'+ str(name)+'.csv')
	else:
		shutil.copyfile(inputDirectory+str(name)+'.csv',testDir+'/'+ str(name)+'.csv')


#Start timer
start_time = time.time()
#inputs
inputDirectory = sys.argv[1]
train = sys.argv[2]
test=sys.argv[3]
ratio=0.8
if len(sys.argv)>4:
	ratio=float(sys.argv[4])
#print("ratio==",ratio)
# mkdir the output directory
if not os.path.exists(train):
	os.makedirs(train)
# mkdir the output directory
if not os.path.exists(test):
	os.makedirs(test)


files = [filename.split('.')[0] for filename in os.listdir(inputDirectory) if filename.endswith(".csv")] #Ensemble des noms de fichiers
#print(files)
serie=pd.Series(files)
#print(serie)
df=serie.str.split('-',expand=True) #Dataframe
#print(df)
#print(df[1].max())
#print(df.columns[1:])
for c in df.columns[1:]:
	df[c]=df[c].apply(int)
#print(df)
df=df.sort_values(by=list(df.columns),axis=0) #Tri selon le id
#print(df)
df['name']=df[0]
#print(df['name'])
for c in df.columns[1:]:
	if c != 'name':
		#print(df[c].astype(str))
		df['name']=df['name']+'-'+df[c].astype(str)

df['count']=df.groupby(0)['name'].transform('count')
df=df.reset_index()
total=len(df)

seq=4546464
currentUser=''
for index, row in df.iterrows():
	if currentUser == row[0]:
		seq=seq+1
	else:
		seq=0
	#print(row['name'],seq,row['count'])
	copyTrainTest(row['name'],seq,row['count'],ratio,inputDirectory,train,test)
	currentUser=row[0]

#End timer
end_time = time.time()
print("Spliting dataset in", ratio, "train, and ", round(1-ratio,2), "test\nExecution time : ",end_time - start_time, " sec")





