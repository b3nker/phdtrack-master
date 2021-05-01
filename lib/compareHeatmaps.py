import os
import sys
import pandas as pd
import math
import numpy as np

def topsoe_distance(p, q):
	v=0
	hasComputed  = False
	for i in range(0,len(p)):
		#print(v)
		if p[i] == 0 or q[i] == 0:
			v = v+0
			continue
		hasComputed = True
		v = v + (p[i]*math.log((2*p[i])/( p[i]+q[i])) + q[i]* math.log((2*q[i])/( p[i]+q[i])))
		#print("ICII",v, p[i], q[i], math.log((2*p[i])/( p[i]+q[i])))
	return {'v': v, 'hasComputed': hasComputed}

def find_prediction(test_row, df_train):
	best_distance = 10000
	predicted_user = -1
	id_user = int(test_row[0])
	p = test_row[1: len(test_row) - 1]
	#print("============ P :\n",p)
	for index, row in df_train.iterrows():
		cur_user = int(row[0])
		q = row[1:len(row) - 1]
		#print(index,"\n============ Q :\n",q,"========\n\n")
		cur_result = topsoe_distance(p, q)
		distance = cur_result['v']
		hasComputed = cur_result['hasComputed']
		#print(index, distance)
		if hasComputed and distance < best_distance:
			best_distance = distance
			predicted_user = cur_user
	print("initial user : ", id_user, " predicted user :", predicted_user, "topsoe_distance : ", best_distance)
	filename = 'resultComparison/results.csv'
	with open(filename,'a+') as f :
		f.write(str(id_user)+','+str(predicted_user)+'\n')
