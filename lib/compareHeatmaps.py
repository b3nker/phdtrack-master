import os
import sys

class HeatMap:
	cells = set()
	def __init__(self, pCells, pId):
		self.cells = pCells
		self.id_user = pId

def topsoeDistance(setCells1, setCells2):
	return 0

def compareTwoHeatmap(h1, h2):
	return topsoeDistance(h1.cells,h2.cells)

heatmapTrain = sys.argv[1]
heatMapTestDirectory = sys.argv[2]

map_result = {}

for filename in os.listdir(heatMapTestDirectory):
	if filename.endswith(".csv"):
		return