import os
import psutil
import sys
import concurrent.futures
import pandas as pd
from compareHeatmaps import find_prediction

heatmapTrainFile = sys.argv[1]
heatmapTestFile = sys.argv[2]

filename = 'resultComparison/results.csv'
open(filename, "w+").close()

cols_train = list(pd.read_csv(heatmapTrainFile, nrows =1))
df_train = pd.read_csv(heatmapTrainFile, sep=',',usecols= [i for i in cols_train if i!= 'day' and i !='nbPoints'])

cols_test = list(pd.read_csv(heatmapTestFile, nrows =1))
df_test = pd.read_csv(heatmapTestFile, sep=',',usecols= [i for i in cols_test if i!= 'day' and i !='nbPoints'])

#print(df_train)
for index, row in df_test.iterrows():
	find_prediction(row,df_train)
#	print(row)
#	print('=========\n\n')

#NB_PROCESS = psutil.cpu_count(logical=False)
#
#executor = concurrent.futures.ProcessPoolExecutor(NB_PROCESS)
#
## For each trace launch the trace processing job
#futures = [executor.submit(find_prediction,row,df_train) for index, row in df_test.iterrows()]
#
## Wait for the processes to finish
#concurrent.futures.wait(futures) 