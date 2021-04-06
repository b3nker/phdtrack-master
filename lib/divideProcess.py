import os
import psutil
import sys
import concurrent.futures
from compareHeatmaps import main

trainDirectory = sys.argv[1]
testDirectory = sys.argv[2]

NB_PROCESS = psutil.cpu_count(logical=False)

executor = concurrent.futures.ProcessPoolExecutor(NB_PROCESS)

# For each trace launch the trace processing job
futures = [executor.submit(main,filename,trainDirectory) for filename in os.listdir(testDirectory)]

# Wait for the processes to finish
concurrent.futures.wait(futures) 