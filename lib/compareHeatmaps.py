import os
import sys
import pandas as pd
import math
import numpy as np

def topsoe_distance(p, q):
	print(p, q)
	v=0
	for i in range(0,len(p)):
		#print(v)
		if p[i] == 0 or q[i] == 0:
			v = v+0
			continue
		v = v + (p[i]*math.log((2*p[i])/( p[i]+q[i])) + q[i]* math.log((2*q[i])/( p[i]+q[i])))
	return v


def heatmap_to_matrix(path):
	df = pd.read_csv(path)
	df.drop(df.columns[[1,2]], axis=1, inplace=True)
	df = df.to_numpy()
	return df


# Inputs
path_heatmap_test = sys.argv[1]
path_heatmap_train = sys.argv[2]

def find(test_row, df_train):

matrix_test = heatmap_to_matrix(path_heatmap_test)
matrix_train = heatmap_to_matrix(path_heatmap_train)
