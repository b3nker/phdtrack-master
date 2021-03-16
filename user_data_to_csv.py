import os
import sys
import time


def file_len(fname):
    with open(user_directory + '/' + fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


start_time = time.time()
user_directory = sys.argv[1]
user_prediction_file_path = sys.argv[2]


output_directory = sys.argv[3]
output_csv = open(output_directory, "a")
with open(user_prediction_file_path) as open_file_object:
    for line in open_file_object:
        infos = line.rstrip("\n").split(',')
        user_id = infos[0]
        user_prediction = infos[1]
        file_length = file_len(user_id + '.csv')  # number of records for a given user
        output_csv.write(user_id + ',' + user_prediction + ',' + str(file_length) + '\n')
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