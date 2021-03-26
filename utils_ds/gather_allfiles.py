import sys
import os

#inputs
inputDirectory = sys.argv[1]

files = [filename for filename in os.listdir(inputDirectory)]
print(files)
for file in files :
	f1 = open(inputDirectory+"/"+file, 'a+')
	id = str(file).split('-')[0]
	#print("nom=",file_name," id=",id)
	new_file = open(inputDirectory+"/"+id+".csv", 'a+')
	new_file.write(f1.read())
