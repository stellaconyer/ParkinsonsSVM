import os
import sys
import tarfile
from datetime import datetime
from numpy import mean, sqrt, arange, array
import csv


##############################################################

# CREATE AVERAGED CSV FILE 

# Use """ find folder_name -name "*.csv"| parse_csv_avg_all.py 0_or_1 """ to run from command line
#Data_set_codes:
# 0: Control
# 1: Parkinsons

# Average absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis over one hour 

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
            patient = file_name[2]

            csv_file.next() #skip the headeR

            for line in csv_file:

                line = line.split(",")
                total_abs = (float(line[3]) + float(line[11]) + float(line[19]))/3
                x_1hz = line[6]
                x_3hz = line[7]
                x_6hz = line[8]
                x_10hz = line[9]

                y_1hz = line[14]
                y_3hz = line[15]
                y_6hz = line[16]
                y_10hz = line[17]

                z_1hz = line[22]
                z_3hz = line[23]
                z_6hz = line[24]
                z_10hz = line[25]

                time = line[26].strip().replace("\"", '')

                #Append to master file for control or parkinsons dataset
                filename = "%s_test_total.csv" % data_set  
                with open(filename, 'ab') as csvfile:
                    linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    linewriter.writerow([patient, group, total_abs, x_1hz, x_3hz, x_6hz, x_10hz, y_1hz, y_3hz, y_6hz, y_10hz, z_1hz, z_3hz, z_6hz, z_10hz, time])




calculate_avg()

# python /Users/StellaCotton/hackbright/ParkinsonsSVM/parse_csv_per_user.py


# find parkinsons -name "*.csv" | python /Users/StellaCotton/hackbright/ParkinsonsSVM/parse_csv_per_user.py
