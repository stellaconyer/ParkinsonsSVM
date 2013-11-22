import os
import sys
import tarfile
from datetime import datetime
from numpy import mean, sqrt, arange, array
import csv


##############################################################

# CREATE TOTAL CSV

# Use """ find folder_name -name "*.csv"| python parse_csv_per_user.py 0/1 """ to run from command line
#Data_set_codes:
# 0: Control
# 1: Parkinsons

# Create file with all points as absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis 

def calculate_avg():

    group = int(sys.argv[1])

    if group == 1:
        data_set = "parkinsons"
    elif group == 0:
        data_set = "control"
    print data_set

    for line in sys.stdin: 
        a_file = line.strip()

        with open(a_file,'r') as csv_file:
            path_name = a_file.split("/")
            file_name = path_name[3].replace(".", "_").split("_")
            patient = file_name[1]



            csv_file.next() #skip the headeR

            for line in csv_file:

                line = line.split(",")
                total_abs = (float(line[3]) + float(line[11]) + float(line[19]))/3
                total_1hz = line[6] + line[14] + line[22]
                total_3hz = line[7] + line[15] + line[23]
                total_6hz = line[8] + line[16] + line[24]
                total_10hz = line[9] + line[17] + line[25]


                time = line[26].strip().replace("\"", '')

            #     #Append to master file for control or parkinsons dataset
                filename = "%s_total_values.csv" % data_set  
                with open(filename, 'ab') as csvfile:
                    linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    linewriter.writerow([patient, group, total_abs, total_1hz, total_3hz, total_6hz, total_10hz, time])




calculate_avg()
