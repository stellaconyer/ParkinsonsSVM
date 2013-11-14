import os
import sys
import tarfile
from datetime import datetime
from numpy import mean, sqrt, arange, array
import csv
import math


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
        file_array = open(a_file).readlines()
        if len(file_array) > 100:
            with open(a_file,'r') as csv_file:
                path_name = a_file.split("/")
                file_name = path_name[3].replace(".", "_").split("_")
                patient = file_name[2]
                recorded_date = datetime.strptime(file_name[3], "%Y%m%d")
                recorded_start_and_stop_time = file_name[4]
            
                avg_abs = []
                avg_1hz = []
                avg_3hz = []
                avg_6hz = []
                avg_10hz = []
                length = 0

                csv_file.next() #skip the header
                for line in csv_file:
                    length +=1
                    line = line.split(",")

                    line_abs_avg = [float(line[3]), float(line[11]), float(line[19])]
                    avg_abs.append(math.fsum(line_abs_avg)/3.0)

                    line_1hz_avg = [float(line[6]), float(line[14]), float(line[22])]
                    avg_1hz.append(math.fsum(line_1hz_avg)/3.0)
                    
                    line_3hz_avg = [float(line[7]), float(line[15]), float(line[23])]
                    avg_3hz.append(math.fsum(line_3hz_avg)/3.0)

                    line_6hz_avg = [float(line[8]), float(line[16]), float(line[24])]
                    avg_6hz.append(math.fsum(line_6hz_avg)/3.0)

                    line_10hz_avg = [float(line[9]), float(line[17]), float(line[25])]
                    avg_10hz.append(math.fsum(line_10hz_avg)/3.0)

                if length > 600:

                # Calculate average for 5 dimensions
                    total_abs_avg = math.fsum(avg_abs)/length * 1.0
                    # print "rms abs", total_abs_avg

                    total_1hz_avg = math.fsum(avg_1hz)/length * 1.0
                    # print "rms 1hz", total_1hz_avg

                    total_3hz_avg = math.fsum(avg_3hz)/length * 1.0
                    # print "rms 3hz", total_3hz_avg

                    total_6hz_avg = math.fsum(avg_6hz)/length * 1.0
                    # print "rms 6hz",total_6hz_avg

                    total_10hz_avg = math.fsum(avg_10hz)/length * 1.0
                    # print "rms 10hz",total_10hz_avg


                    #Append to master file for control or parkinsons dataset
                    filename = "%s_master_hourly.csv" % data_set   
                    with open(filename, 'ab') as csvfile:
                        linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                        linewriter.writerow([total_abs_avg, total_1hz_avg, total_3hz_avg, total_6hz_avg, total_10hz_avg, group, patient, recorded_date, recorded_start_and_stop_time]) 





calculate_avg()



