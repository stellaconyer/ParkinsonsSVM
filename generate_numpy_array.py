import numpy as np
from sklearn import preprocessing, svm

def generate_numpy_array():
	# Control:
	control_data_array = np.genfromtxt('control_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	control_labels_array = np.genfromtxt('control_master_hourly.csv', usecols= (5), delimiter=',')

	# Parkinsons:
	parkinsons_data_array = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	parkinsons_labels_array = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (5), delimiter=',')

	# Master of control and parkinsons:
	master_data_array = np.concatenate([control_data_array, parkinsons_data_array])
	master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 

	#Unknown variable for testing:
	variable_data_array = np.genfromtxt('variable_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')

	X_unscaled = master_data_array
	y = master_labels_array

	#Scale X data for mean at 0
	X = preprocessing.scale(X_unscaled)

	clf = svm.SVC()
	clf.fit(X, y)

	variable = variable_data_array[150]

	prediction = clf.predict([variable])
	print prediction

# 	SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0, degree=3,
# gamma=0.0, kernel='rbf', max_iter=-1, probability=False, random_state=None,
# shrinking=True, tol=0.001, verbose=False)

generate_numpy_array()




# Control
# apple
# dafodil


# crocus
# daisey
# daisy


# flox


