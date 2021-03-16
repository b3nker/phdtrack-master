import math
import os
import sys
import time

def file_len(fname):
    with open(userDirectory + '/' + fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

start_time = time.time()
# inputs
userDirectory = sys.argv[1]
trainDirectory = sys.argv[2]
testDirectory = sys.argv[3]
ratio = 0.8
if len(sys.argv) > 4:
    ratio = float(sys.argv[4])

# mkdir the output directory
if not os.path.exists(trainDirectory):
    os.makedirs(trainDirectory)
# mkdir the output directory
if not os.path.exists(testDirectory):
    os.makedirs(testDirectory)

files = [filename for filename in os.listdir(userDirectory)]
#print(files)
for file in files:
    file_length = file_len(file)
    lines_train = math.ceil(file_length*ratio)
    lines_test = file_length - lines_train
    it_train = 0
    it_test = 0
    f = open(userDirectory + '/' + file)
    output_train = open(trainDirectory + '/' + file, "a")
    output_test = open(testDirectory + '/' + file, "a")
    while it_train < lines_train:
        output_train.write(f.readline())
        it_train += 1
    while it_test < lines_test:
        output_test.write(f.readline())
        it_test += 1
    f.close()
    print("filename", file, "train :", lines_train, "test : ", lines_test)


end_time = time.time()
print("Spliting dataset in", ratio, "train, and ", round(1 - ratio, 2), "test\nExecution time : ",
      end_time - start_time, " sec")
