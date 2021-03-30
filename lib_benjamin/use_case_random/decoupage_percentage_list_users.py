import math
import os
import sys
import time

sys.path.append('.')  # relative to where you execute the command/script
from lib.utils import file_len

start_time = time.time()
# inputs
userDirectory = sys.argv[1]
trainDirectory = sys.argv[2]
testDirectory = sys.argv[3]
path_to_selected_id_users = sys.argv[4] # just for current iteration

ratio = 0.8
if len(sys.argv) > 5:
    ratio = float(sys.argv[5])

# mkdir the output directory
if not os.path.exists(trainDirectory):
    os.makedirs(trainDirectory)
# mkdir the output directory
if not os.path.exists(testDirectory):
    os.makedirs(testDirectory)

id_set = set()


with open(path_to_selected_id_users) as f:
    for line in f:
        id_set.add(line.rstrip('\n'))
for id in id_set:
    file_length = file_len(userDirectory + id + '.csv')
    lines_train = math.ceil(file_length * ratio)
    lines_test = file_length - lines_train
    it_train = 0
    it_test = 0
    f = open(userDirectory + id + '.csv')
    output_train = open(trainDirectory + id + '.csv', "a")
    output_test = open(testDirectory + id + '.csv', "a")
    while it_train < lines_train:
        output_train.write(f.readline())
        it_train += 1
    while it_test < lines_test:
        output_test.write(f.readline())
        it_test += 1
    f.close()
    # print("filename", file, "train :", lines_train, "test : ", lines_test)
end_time = time.time()
print("Spliting dataset in", ratio, "train, and ", round(1 - ratio, 2), "test\nExecution time : ",
      end_time - start_time, " sec")
