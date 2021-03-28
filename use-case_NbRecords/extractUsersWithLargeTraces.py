import sys
import os
import pandas as pd
import shutil
import time

inputFile = sys.argv[1]
outputDirectory = sys.argv[2]
restartProcess = sys.argv[3]
usersAlreadyInSet = sys.argv[4]
nbOfUsersToRead = int(sys.argv[5])

if restartProcess.lower() == 'true' :
	open(usersAlreadyInSet, 'w').close()
	if os.path.exists(outputDirectory):
		shutil.rmtree(outputDirectory)

if not os.path.exists(outputDirectory):
	os.makedirs(outputDirectory)

start_time = time.time()

usersAlreadyAdded = set()
with open(usersAlreadyInSet,'r') as f :
	for line in f:
		id = line
		usersAlreadyAdded.add(id)
	f.close()

nbUsers=len(usersAlreadyAdded)

usersDf = pd.read_csv(inputFile,sep='-', names=['id','nbRows'], header=None, skiprows=nbUsers, nrows=nbOfUsersToRead)

for index, row in usersDf.iterrows():
	fileName = str(row['id'])+'.csv'
	shutil.copyfile('../record_dataset/users/'+fileName, outputDirectory+ (fileName if outputDirectory.endswith('/') else '/'+fileName))

usersDf.to_csv(usersAlreadyInSet, columns=['id'], mode='a', index=False, header=False)

end_time = time.time()
print("Execution time adding ",nbOfUsersToRead," users to the dataset : ",end_time - start_time,"sec")