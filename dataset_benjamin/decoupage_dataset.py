import pandas as pd
import os
import sys
from datetime import datetime
import time

#Converts a date in the following format : YYYY-MM-dd hh:mm:ss to millis
def date_to_millis(date):
    dt = datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
    timestamp_ms = dt.timestamp() * 1000
    return int(timestamp_ms)

my_set = {}

#Start timer
start_time = time.time()
#Inputs
datasetPath = sys.argv[1]
outputDirectory = sys.argv[2]
nbrows = int(sys.argv[3])
#Creates a dataframe
df = pd.read_csv(datasetPath, nrows=nbrows)
#print(df.head())
#print(df.phone.nunique()) #nb of unique users
#Splits location column into 2 columns lat and long

df[['lat', 'long']] = df['location'].str.split('|', 1, expand=True)
df.drop('location', inplace=True, axis=1)

if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)

current_user = ''
cpt = 0
#Reads dataframe line by line
for index, row in df.iterrows():
    row_id = row['phone']
    #row_location = row['location']
    #location = row_location.split('|')
    #row_lat = location[0]
    #row_long = location[1]
    row_lat = row['lat'] #dataset is wrong, lat is long 
    row_long = row['long'] #dataset is wrong, long is lat
    row_time = date_to_millis(row['time'])
    if current_user != row_id:
        if current_user != '':
            current_file.close()
        current_user = row_id
        cpt += 1
        if not os.path.exists(outputDirectory + '/' + str(cpt) +".csv"):
            current_file = open(outputDirectory + '/' + str(cpt) +".csv", "a") # a: append
            #current_file.write("id_user,lat,long,timestamp\n")
        else:
            current_file = open(outputDirectory + '/' + str(cpt) +".csv", "a") # a: append
    current_file.write(str(cpt) + ',' + str(row_long) + ',' + str(row_lat) + ',' + str(row_time) + '\n') #long -> lat and lat -> long

#End timer
end_time = time.time()
#Prints infos
#print(df)
print("Spliting dataset per user\nExecution time : ",end_time - start_time, " sec")
#print(df[['phone']])
 
