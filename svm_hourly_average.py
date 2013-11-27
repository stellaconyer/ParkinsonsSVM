import numpy as np
from sklearn import preprocessing, svm
from sklearn import cross_validation, grid_search
from random import randint
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
import matplotlib.pyplot as plt


def generate_numpy_array():
	# Control:
	control_data_array = np.genfromtxt('old_datasets/avg_then_rms_dataset/control_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	control_labels_array = np.genfromtxt('old_datasets/avg_then_rms_dataset/control_master_hourly.csv', usecols= (5), delimiter=',')

	# Parkinsons:
	parkinsons_data_array = np.genfromtxt('old_datasets/avg_then_rms_dataset/parkinsons_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')
	parkinsons_labels_array = np.genfromtxt('old_datasets/avg_then_rms_dataset/parkinsons_master_hourly.csv', usecols= (5), delimiter=',')

	# Master of control and parkinsons:
	master_data_array_unscaled = np.concatenate([control_data_array, parkinsons_data_array])
	master_labels_array = np.concatenate([control_labels_array, parkinsons_labels_array]) 

	#Unknown variable for testing:
	# variable_data_array = np.genfromtxt('variable_master_hourly.csv', usecols= (0,1,2,3,4), delimiter=',')

	master_data_array = preprocessing.scale(master_data_array_unscaled)
	print len(master_data_array)

	X_train, X_test, y_train, y_test = train_test_split(master_data_array, master_labels_array, test_size=0.5, random_state=42)

	clf = svm.SVC(kernel='rbf', C=100)
	scores = cross_validation.cross_val_score(clf, master_data_array, master_labels_array, cv=5)
	print scores
	print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



	# Set the parameters by cross-validation


	# tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-2],
	#                      'C': [100]}]

	# scores = ['precision', 'recall']

	# for score in scores:
	#     print("# Tuning hyper-parameters for %s" % score)
	#     print()

	#     clf = GridSearchCV(SVC(C=1), tuned_parameters, cv=5, scoring=score)
	#     clf.fit(X_train, y_train)

	#     print("Best parameters set found on development set:")
	#     print()
	#     print(clf.best_estimator_)
	#     print()
	#     print("Grid scores on development set:")
	#     print()
	#     for params, mean_score, scores in clf.grid_scores_:
	#         print("%0.3f (+/-%0.03f) for %r"
	#               % (mean_score, scores.std() / 2, params))
	#     print()

	#     print("Detailed classification report:")
	#     print()
	#     print("The model is trained on the full development set.")
	#     print("The scores are computed on the full evaluation set.")
	#     print()
	#     y_true, y_pred = y_train, clf.predict(X_train)
	#     print(classification_report(y_true, y_pred))
	#     print()





	#SCALE YOUR TESTING DATA!!
	# variable_scaled = preprocessing.scale(variable_data_array)

	# X = preprocessing.scale(x_train)
	# y = master_labels_array

	#Scale X data for mean at 0


	# clf = svm.SVC()
	# status = clf.fit(X, y)
	# print status

	# counter = 0
	# while counter < 100:
	# 	random_test_num = randint(0, len(variable_data_array)-1)
	# 	variable = variable_scaled[random_test_num]
	# 	counter += 1
	# 	prediction = clf.predict([variable])
	# 	print prediction

generate_numpy_array()



