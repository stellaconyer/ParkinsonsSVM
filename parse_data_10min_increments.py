import os
import sys
import tarfile
from datetime import datetime
from numpy import mean, sqrt, arange, array
import csv


##############################################################

# CREATE RAW DATA CSV FILE 

# Use """ find extracted -name "*.csv"| python parse_csv.py 0_or_1 """ to run from command line
#Data_set_codes:
# 0: Control
# 1: Parkinsons

# Average absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis over 10 minutes

def create_raw_data_file():

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

                x_abs = 0
                x_1hz = 0
                x_3hz = 0
                x_6hz = 0
                x_10hz = 0

                y_abs = 0
                y_1hz = 0
                y_3hz = 0
                y_6hz = 0
                y_10hz = 0

                z_abs = 0
                z_1hz = 0
                z_3hz = 0
                z_6hz = 0
                z_10hz = 0

                length = 0

                csv_file.next() #skip the header
                for line in csv_file:
                    length +=1
                    line = line.split(",")
                    x_abs += float(line[3])
                    x_1hz += float(line[6])
                    x_3hz += float(line[7])
                    x_6hz += float(line[8])
                    x_10hz += float(line[9])

                    y_abs += float(line[11])
                    y_1hz += float(line[14])
                    y_3hz += float(line[15])
                    y_6hz += float(line[16])
                    y_10hz += float(line[17])

                    z_abs += float(line[19])
                    z_1hz += float(line[22])
                    z_3hz += float(line[23])
                    z_6hz += float(line[24])
                    z_10hz += float(line[25])

                    if length > 9:
                        x_abs_avg = (x_abs/length)
                        x_1hz_avg = (x_1hz/length)
                        x_3hz_avg = (x_3hz/length)
                        x_6hz_avg = (x_6hz/length)
                        x_10hz_avg = (x_10hz/length)

                        y_abs_avg = (y_abs/length)
                        y_1hz_avg = (y_1hz/length)
                        y_3hz_avg = (y_3hz/length)
                        y_6hz_avg = (y_6hz/length)
                        y_10hz_avg = (y_10hz/length)

                        z_abs_avg = (z_abs/length)
                        z_1hz_avg = (z_1hz/length)
                        z_3hz_avg = (z_3hz/length)
                        z_6hz_avg = (z_6hz/length)
                        z_10hz_avg = (z_10hz/length)

                        filename = "%s_raw_data_10min.csv" % data_set   
                        with open(filename, 'ab') as csvfile:
                            linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                            linewriter.writerow([x_abs_avg, x_1hz_avg, x_3hz_avg, x_6hz_avg, x_10hz_avg, y_abs_avg, y_1hz_avg, y_3hz_avg, y_6hz_avg, y_10hz_avg, z_abs_avg, z_1hz_avg, z_3hz_avg, z_6hz_avg, z_10hz_avg, group, patient, recorded_date, recorded_start_and_stop_time]) 
                        length = 0
                        x_abs = 0
                        x_1hz = 0
                        x_3hz = 0
                        x_6hz = 0
                        x_10hz = 0

                        y_abs = 0
                        y_1hz = 0
                        y_3hz = 0
                        y_6hz = 0
                        y_10hz = 0

                        z_abs = 0
                        z_1hz = 0
                        z_3hz = 0
                        z_6hz = 0
                        z_10hz = 0




create_raw_data_file()



