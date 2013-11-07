import numpy as np
from sklearn import preprocessing, svm

def generate_numpy_array():
	# Control:
	control_data_array = np.genfromtxt('control_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	control_labels_array = np.genfromtxt('control_master_hourly.csv', usecols= (5), delimiter=',')

	print len(control_data_array)
	# print control_labels_array

	# Parkinsons:
	parkinsons_data_array = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	parkinsons_labels_array = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (5), delimiter=',')

	print len(parkinsons_data_array)

	#Unknown variable
	variable_data_array = np.genfromtxt('variable_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')

	# Master:
	master_data_array = np.concatenate([control_data_array, parkinsons_data_array])
	master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 

	print master_data_array

	X = master_data_array
	y = master_labels_array



	X_scaled = preprocessing.scale(X)


	# print "X", X
	# print "Y", y

	print "X Scaled", X_scaled


generate_numpy_array()




# Control
# apple
# dafodil


# crocus
# daisey
# daisy


# flox


