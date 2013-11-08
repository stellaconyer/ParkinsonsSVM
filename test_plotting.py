import numpy as np
from sklearn import preprocessing, svm
from sklearn import cross_validation, grid_search
from random import randint
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import matplotlib.pyplot as plt

SCALE = .5
ABS = 0
LOW = 1
MID = 2
HIGHMID = 3
HIGH = 4

def generate_numpy_array():
	# Control:
	x_axis =  MID
	y_axis = HIGHMID
	control_data_array_x = np.genfromtxt('control_master_hourly.csv', usecols= (x_axis), delimiter=',')
	# control_data_array_x = preprocessing.scale(control_data_array_x)
	# control_labels_array = np.genfromtxt('control_master_hourly.csv', usecols= (5), delimiter=',')

	# Parkinsons:
	parkinsons_data_array_x = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (x_axis), delimiter=',')
	# parkinsons_data_array_x = preprocessing.scale(parkinsons_data_array_x)
	# parkinsons_labels_array = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (5), delimiter=',')


	control_data_array_y = np.genfromtxt('control_master_hourly.csv', usecols= (y_axis), delimiter=',')
	# control_data_array_y = preprocessing.scale(control_data_array_y)

	# Parkinsons:
	parkinsons_data_array_y = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (y_axis), delimiter=',')
	# parkinsons_data_array_y = preprocessing.scale(parkinsons_data_array_y)

	# Master of control and parkinsons:
	# master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	# master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 

	#Unknown variable for testing:
	# variable_data_array = np.genfromtxt('variable_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')

	# master_data_array = preprocessing.scale(master_data_array_unscaled)


	plt.plot(control_data_array_x, control_data_array_y, 'bo')

	plt.plot(parkinsons_data_array_x, parkinsons_data_array_y, 'ro')
	plt.axis([0, SCALE, 0, SCALE])
	plt.show()


generate_numpy_array()