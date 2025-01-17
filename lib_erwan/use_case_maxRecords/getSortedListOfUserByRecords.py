import os
import sys
sys.path.append('.')
from lib.utils import file_len

inputDirectory = sys.argv[1]
files = [filename for filename in os.listdir(inputDirectory) if filename.endswith(".csv")]

open('dataset/nbRecordsPerUser.csv','w+').close()

map_user = {}

for file in files :
	file_length = file_len(inputDirectory+'/'+file)
	id = str(file).split('.')[0]
	map_user[id]=file_length

map_user = dict(sorted(map_user.items(), key=lambda item: item[1], reverse=True))

with open('dataset/nbRecordsPerUser.csv','w+') as f:
	for key in map_user:
		f.write(key+','+str(map_user[key])+'\n')

f.close()