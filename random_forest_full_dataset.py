import numpy as np
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

LABEL = 0
ABS = 2
LOW = 3
MID = 4
HIGHMID = 5
HIGH = 6


park_file = "/Users/StellaCotton/hackbright/ParkinsonsSVM/random_files/PARK_PATIENT_DATA_CHRISTIAN_3.csv"
control_file = "/Users/StellaCotton/hackbright/ParkinsonsSVM/random_files/CONTROL_PATIENT_DATA_CHRISTIAN_3.csv"

def generate_numpy_array():
	# Control:
	control_data_array = np.genfromtxt(control_file, usecols= (LOW, MID, HIGHMID, HIGH), delimiter=',')
	control_labels_array = np.genfromtxt(control_file, usecols= (LABEL), delimiter=',')

	# Parkinsons:
	parkinsons_data_array = np.genfromtxt(park_file, usecols= (LOW, MID, HIGHMID, HIGH), delimiter=',')
	parkinsons_labels_array = np.genfromtxt(park_file, usecols= (LABEL), delimiter=',')

	# Master of control and parkinsons:
	master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 

	# master_data_array = preprocessing.scale(master_data_array_unscaled)

	X_train, X_test, y_train, y_test = train_test_split(master_data_array_unscaled, master_labels_array, test_size=0.2, random_state=42)

	clf = RandomForestClassifier(n_estimators=150, min_samples_split=2, n_jobs=-1).fit(X_train, y_train)
	print clf.score(X_test, y_test)

	y_true, y_pred = y_test, clf.predict(X_test)
	print(classification_report(y_true, y_pred))




generate_numpy_array()



