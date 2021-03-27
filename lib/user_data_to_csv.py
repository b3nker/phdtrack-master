import os
import sys
import time
from utils import file_len

sys.path.append('./')  # relative to where you execute the command/script


start_time = time.time()
user_directory = sys.argv[1]
user_prediction_file_path = sys.argv[2]

set_ids = set()
output_directory = sys.argv[3]
output_csv = open(output_directory, "a")
with open(user_prediction_file_path) as open_file_object:
    for line in open_file_object:
        infos = line.rstrip("\n").split(',')
        user_id = infos[0]
        set_ids.add(user_id)
        user_prediction = infos[1]
        file_length = file_len(user_directory + '/' + user_id + '.csv')  # number of records for a given user
        output_csv.write(user_id + ',' + user_prediction + ',' + str(file_length) + '\n')

# Write user_id that has not any prediction (i.e, not in accio's matches)
files = [filename for filename in os.listdir(user_directory)]
for file in files:
    cur_id = file.split('.')[0]
    if not (cur_id in set_ids):
        # print(cur_id)
        output_csv.write(cur_id + ',' + ',' + str(file_len(user_directory + '/' + file)) + '\n')

output_csv.close()

# files = [filename for filename in os.listdir(user_directory)]
# output_csv = open(output_directory + '/' + 'users_data.csv', "a")
# for file in files:
#     file_length = file_len(file)
#     user_id = file.split('.')[0]
#     output_csv.write( user_id + ',' + str(file_length) + '\n')
# output_csv.close()
end_time = time.time()
print("Writing users information\nExecution time : ", end_time - start_time, " sec")
