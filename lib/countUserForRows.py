import sys
import os

inputDirectory = sys.argv[1]
i = 0
nbr = 0
set_ = set()

with open(inputDirectory) as f:
	next(f)
	for line in f :
		id = line.split(",")[0]
		if not (id in set_) :
			set_.add(id)
		i = i+1
		if i > 100000 :
			break
f.close()

j = 0
nbr =0
curId=''
with open(inputDirectory) as f1:
	next(f1)
	for line in f1 :
		id = line.split(",")[0]
		if curId != id :
			nbr = nbr +1
			curId = id
		j = j+1
		if j > 100000 :
			break
f1.close()

print(len(set_))
print(nbr)