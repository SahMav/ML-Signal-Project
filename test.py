import csv
import numpy as np

predictions_1 = np.array([[64.40028, 107.83399], [ 60.47024, 99.70935], [ 62.571354, 95.35052 ]])
predictions_2 = np.array([[ 64.44086, 112.17663], [ 63.337936, 109.73628 ], [ 64.828384, 117.491714]])
predictions_3 = np.array([[ 64.95834,  118.718994], [ 61.129658 ,104.46549 ], [ 61.338158, 104.085815]])
predictions_4 = np.array([[ 62.63371, 118.32076], [ 61.59244, 113.74617], [ 63.903725, 129.49338 ]])
predictions_5 = np.array([[ 71.899666, 160.52858 ],[ 66.75427, 134.87366 ], [ 66.75427, 134.87366 ]])
predictions_6 = np.array([[ 66.8972,  138.58952 ], [ 63.168167, 129.25092 ], [ 65.5746, 136.80557  ]])

real_1 = np.array([[55, 115], [60, 114]])
real_2 = np.array([[65, 92], [61, 94]])
real_3 = np.array([[65, 103], [69, 108]])
real_4 = np.array([[72, 91], [57, 88]])
real_5 = np.array([[73, 106], [77, 102]])
real_6 = np.array([[87, 136], [86, 122]])

error_1_0 = abs(predictions_1 - real_1[0])
error_2_0 = abs(predictions_2 - real_2[0])
error_3_0 = abs(predictions_3 - real_3[0])
error_4_0 = abs(predictions_4 - real_4[0])
error_5_0 = abs(predictions_4 - real_4[0])
error_6_0 = abs(predictions_6 - real_6[0])

errors_0 = np.concatenate((error_1_0, error_2_0, error_3_0, error_4_0, error_5_0, error_6_0), axis= 0)
mean_error_0 = np.mean(errors_0, axis=0)
std_0 = np.std(errors_0, axis=0)


error_1_1 = abs(predictions_1 - real_1[1])
error_2_1 = abs(predictions_2 - real_2[1])
error_3_1 = abs(predictions_3 - real_3[1])
error_4_1 = abs(predictions_4 - real_4[1])
error_5_1 = abs(predictions_4 - real_4[1])
error_6_1 = abs(predictions_6 - real_6[1])

errors_1 = np.concatenate((error_1_1 ,error_2_1, error_3_1, error_4_1, error_5_1, error_6_1), axis = 0)
mean_error_1 = np.mean(errors_1, axis=0)
std_1 = np.std(errors_1, axis=0)


print(mean_error_0)
print(std_0)
print(mean_error_1)
print(std_1)