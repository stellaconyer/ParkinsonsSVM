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

# /Users/StellaCotton/Downloads/MJFF-Data/extracted/control_raw_data_10min.csv

def plot_numpy_array():

	x_axis =  HIGHMID
	y_axis = HIGH




	array = [0.79397623257292449, 0.47522821761787826, 0.29310619390531145, 1.2647319686369869, 0.60675005394298342, 0.43239052568645464, 0.56943934600060986, 0.0806352176614831, 0.70114457621271309, 0.2415444947619281, 0.24855550151819705, 0.12679694512938167, 13.022426812327259, 19.735206633021956, 6.2591200477799855, 8.0723571227549122, 19.691835013697666, 12.275757419918344, 7.9030217810738463, 7.6598119026118887, 18.383836317677574, 11.479979602713868, 9.205954539239082, 8.3728413087719762, 23.377451918511134, 17.580718959462779, 11.712809868405863, 0.45420005950833142, 15.55709541958519, 6.4655545663196419, 7.5172179157301597, 3.4052780883143638, 7.7238226417434106, 18.138006010966624, 9.4792263731945781, 16.356881882136406, 15.483028672673962, 15.936518643289041, 6.7652777498317231, 2.7953312602668809, 22.893593032051147, 12.633981703517454, 18.083910178123414, 25.076236028052861, 41.322079827502577, 13.572896818477785, 19.40989570972182, 7.0538720257754921, 19.695601439159546, 40.353511232707014, 13.317404663806629, 5.4707719093103009, 24.764578729682114, 44.346115641005724, 17.224742842093395, 1.1057204498373503, 32.53976041159747, 11.659832758964395, 37.292920569622694, 14.726284110570347, 9.3615958475757601, 11.45547879953709, 3.3847648529226801, 4.4077328551322248]

	# one_hz_total = []
	# three_hz_total = []
	# six_hz_total = []
	# ten_hz_total = []

	# for items in array:
	# 	one_hz = items[0]
	# 	three_hz = items[1]
	# 	six_hz = items[2]
	# 	ten_hz = items[3]

	# 	one_hz_total.append(one_hz)
	# 	three_hz_total.append(three_hz)
	# 	six_hz_total.append(six_hz)
	# 	ten_hz_total.append(ten_hz)




	# X AXIS
	control_data_array_x = range(len(array))
	# parkinsons_data_array_x = np.genfromtxt('/Users/StellaCotton/Downloads/MJFF-Data/extracted/parkinsons_raw_data_10min.csv', usecols= (x_axis), delimiter=',')

	# print len(parkinsons_data_array_x)

	#Y AXIS
	control_data_array_y = array
	# parkinsons_data_array_y = np.genfromtxt('/Users/StellaCotton/Downloads/MJFF-Data/extracted/parkinsons_raw_data_10min.csv', usecols= (y_axis), delimiter=',')

	# Master of control and parkinsons:
	# master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	# master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 


	#Plot in Matplot

	plt.bar(control_data_array_x, array, width=0.8, bottom=None, hold=None)

	plt.axis([0, SCALE, 0, SCALE])
	plt.autoscale(enable=True)
	plt.show()


plot_numpy_array()
