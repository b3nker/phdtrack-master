import sys
import os

#inputs
inputDirectory = sys.argv[1]

files = [filename for filename in os.listdir(inputDirectory) if filename.endswith("-0.csv") ]

for file_name in files :
	f1 = open(file_name, 'a+')
	id = str(file_name).split('-')[0]
	#print("nom=",file_name," id=",id)
	files_with_same_id = [filename for filename in os.listdir(inputDirectory) if filename.startswith(id)]
	files_with_same_id.remove(file_name)
	#print(files_with_same_id)
	for file_to_append in files_with_same_id :
		f2 = open(file_to_append, 'r') 
		f1.write(f2.read())
		os.remove(file_to_append)