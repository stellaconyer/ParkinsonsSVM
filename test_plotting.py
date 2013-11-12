import numpy as np
import matplotlib.pyplot as plt

#SCALE IF NOT AUTO SCALING
SCALE = 40

#PSD VALUES
ABS = 0
LOW = 1
MID = 2
HIGHMID = 3
HIGH = 4


def plot_numpy_array():

	x_axis =  HIGHMID
	y_axis = HIGH

	# X AXIS
	control_data_array_x = np.genfromtxt('control_master_hourly.csv', usecols= (x_axis), delimiter=',')
	parkinsons_data_array_x = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (x_axis), delimiter=',')

	# print len(parkinsons_data_array_x)

	#Y AXIS
	control_data_array_y = np.genfromtxt('control_master_hourly.csv', usecols= (y_axis), delimiter=',')
	parkinsons_data_array_y = np.genfromtxt('parkinsons_master_hourly.csv', usecols= (y_axis), delimiter=',')

	# Master of control and parkinsons:
	# master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	# master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 


	#Plot in Matplot

	plt.plot(control_data_array_x, control_data_array_y, 'bo')

	plt.plot(parkinsons_data_array_x, parkinsons_data_array_y, 'ro')
	plt.axis([0, SCALE, 0, SCALE])
	# plt.autoscale(enable=True)
	plt.show()


plot_numpy_array()