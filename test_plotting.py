import numpy as np
import matplotlib.pyplot as plt

#SCALE IF NOT AUTO SCALING
SCALE = 8

#patient, group, total_abs, total_1hz, total_3hz, total_6hz, total_10hz, time

#PSD VALUES
ABS = 2
LOW = 3
MID = 4
HIGHMID = 5
HIGH = 6



park_file = "/Users/StellaCotton/Downloads/MJFF-Data/extracted/parkinsons_total_values.csv"
control_file = "/Users/StellaCotton/Downloads/MJFF-Data/extracted/control_total_values.csv"


def plot_numpy_array():

	x_axis = MID
	y_axis = HIGHMID

	# X AXIS
	control_data_array_x = np.genfromtxt(control_file, usecols= (x_axis), delimiter=',')
	# parkinsons_data_array_x = np.genfromtxt(park_file, usecols= (x_axis), delimiter=',')

	# print len(parkinsons_data_array_x)

	#Y AXIS
	control_data_array_y = np.genfromtxt(control_file, usecols= (y_axis), delimiter=',')
	# parkinsons_data_array_y = np.genfromtxt(park_file, usecols= (y_axis), delimiter=',')

	# Master of control and parkinsons:
	# master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	# master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 


	#Plot in Matplot

	plt.plot(control_data_array_x, control_data_array_y, 'bo')

	# plt.plot(parkinsons_data_array_x, parkinsons_data_array_y, 'ro')
	plt.axis([0, SCALE, 0, SCALE])
	# plt.autoscale(enable=True)
	plt.show()


plot_numpy_array()