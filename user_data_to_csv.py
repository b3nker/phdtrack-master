import os
import sys
import time


def file_len(fname):
    with open(userDirectory + '/' + fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


start_time = time.time()
userDirectory = sys.argv[1]
outputDirectory = sys.argv[2]
files = [filename for filename in os.listdir(userDirectory)]
output_csv = open(outputDirectory + '/' + 'users_data.csv', "a")
for file in files:
    file_length = file_len(file)
    user_id = file.split('.')[0]
    output_csv.write( user_id + ',' + str(file_length) + '\n')
end_time = time.time()
print("Writing users information\nExecution time : ", end_time - start_time, " sec")