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


#Start timer
start_time = time.time()
#Inputs
datasetPath = sys.argv[1]
outputDirectory = sys.argv[2]
#Creates a dataframe
df = pd.read_csv(datasetPath, nrows=1000000)
#print(df.phone.nunique()) #nb of unique users
#Splits location column into 2 columns lat and long
df[['lat', 'long']] = df['location'].str.split('|', 1, expand=True)
df.drop('location', inplace=True, axis=1)

current_user = ''
#Reads dataframe line by line
for index, row in df.iterrows():
    row_id = row['phone']
    row_lat = row['lat']
    row_long = row['long']
    row_time = date_to_millis(row['time'])
    if current_user != row_id:
        if current_user != '':
            current_file.close()
        current_user = row_id
        if not os.path.exists(outputDirectory + '/' + row_id +".csv"):
            current_file = open(outputDirectory + '/' + row_id +".csv", "a") # a: append
            current_file.write("id_user, lat, long, timestamp\n")
        else:
            current_file = open(outputDirectory + '/' + row_id +".csv", "a") # a: append
    current_file.write(str(row_id) + ', ' + str(row_lat) + ', ' + str(row_long) + ', ' + str(row_time) + '\n')

#End timer
end_time = time.time()
#Prints infos
#print(df)
print("Execution time : ",end_time - start_time, " sec")
#print(df[['phone']])
 
