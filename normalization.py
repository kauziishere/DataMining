import csv
import warnings
import sys
from math import *
class normalization:
	def __init__(self, data):
		self.row = len(data)
		self.column = len(data[0])
		self.data = [[int(data[i][j]) for j in range(0, column)] for i in range(0, row)]
		self.normalized = [[0 for i in range(0, column)] for j in range(0, row)]

	"""
		Min-Max Normalization for given data
	"""

	def min_max_normalization(self):
		print(self.data)
		for i in range(0, self.column):
			min = 0
			max = 0
			for j in range(0, self.row):
				if(self.data[j][i] > self.data[max][i]):
					max = j
				elif(self.data[j][i] < self.data[min][i]):
					min = j
			for j in range(0, self.row):
				self.data[j][i] = (self.data[j][i] - self.data[min][i])/(self.data[max][i] - self.data[min][i])

	"""
		Function to create csv file the given data matrix
	"""

	def write_to_csv(self, filename, data):
		with open(filename, 'w') as f:
			spamwriter = csv.writer(f, delimiter=',')
			for i in data:
				spamwriter.writerow(i)


	"""
		Z-Score normalization for the given data
	"""
	def z_score_normalization(self):
		normalized = self.normalized
		for i in range(0, self.column):
			val = 0.0
			for j in range(0, self.row):
				val += float(self.data[j][i])
			devi = 0.0
			for j in range(0,self.row):
				devi += (self.data[j][i] - val/(self.row+1))**2
			for j in range(0, self.row):
				normalized[j][i] = (self.data[j][i] - val/(self.row+1))/(sqrt(devi/(self.row+1)))
		self.normalized = normalized

if __name__ == "__main__":
	data = []
	with open("temp.csv", 'r') as f:
		data_file = csv.reader(f, delimiter = ',')
		for i in data_file:
			data.append(i)
	obj = normalization(data)
	obj.z_score_normalization()
	obj.write_to_csv("normalized.csv", obj.normalized)
