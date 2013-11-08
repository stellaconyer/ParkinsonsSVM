import os
import sys
import tarfile
from datetime import datetime
from numpy import mean, sqrt, arange, array
import csv

#Take in a CSV from CLI
#Choose to write to file or print to standard output
# -----------

#Not using any more

#open all accel files to parse out lines
# def open_files():
#     rootdir = "extracted"
#     file_list = []
#     for root, subFolders, files in os.walk(rootdir):
#         for a_file in files:
#             file_name = os.path.join(root, a_file)
#             file_list.append(file_name)
#     return file_list


##############################################################

# Use """ find extracted -name "*.csv"| python parse_csv.py name_to_save_under """ to run from command line

#initial RMS calculation
# Average absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis over one hour (or length of file if shorter than one hour) (eg x_abs, x_1hz, x_3hz, x_6hz, x_10hz)
#take root mean square of the x,y,z values to come up with rms_abs, rms_1, rms_3, rms_6, rms_10
def calculate_RMS():
    for line in sys.stdin: 
        a_file = line.strip()
        with open(a_file,'r') as csv_file:
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

            print a_file
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

        if length > 600:
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

            # print "xavg: ",x_abs_avg, x_1hz_avg, x_3hz_avg, x_6hz_avg, x_10hz_avg
            # print "yavg: ",y_abs_avg, y_1hz_avg, y_3hz_avg, y_6hz_avg, y_10hz_avg
            # print "zavg: ",z_abs_avg, z_1hz_avg, z_3hz_avg, z_6hz_avg, z_10hz_avg

        # Calculate RMS for 5 dimensions
            total_abs_avg = array([x_abs_avg, y_abs_avg, z_abs_avg])
            rms_abs = sqrt(mean(total_abs_avg**2))
            print "rms abs",rms_abs

            total_1hz_avg = array([x_1hz_avg, y_1hz_avg, z_1hz_avg])
            rms_1hz = sqrt(mean(total_1hz_avg**2))
            print "rms 1hz",rms_1hz

            total_3hz_avg = array([x_3hz_avg, y_3hz_avg, z_3hz_avg])
            rms_3hz = sqrt(mean(total_3hz_avg**2))
            print "rms 3hz",rms_3hz

            total_6hz_avg = array([x_6hz_avg, y_6hz_avg, z_6hz_avg])
            rms_6hz = sqrt(mean(total_6hz_avg**2))
            print "rms 6hz",rms_6hz

            total_10hz_avg = array([x_10hz_avg, y_10hz_avg, z_10hz_avg])
            rms_10hz = sqrt(mean(total_10hz_avg**2))
            print "rms 10hz",rms_10hz

            label_id = 1

        # append data to master_hourly.CSV
        ### CHANGE SO IT TAKES THE FILENAME AND LABEL ID OF CONTROL OR PARKINSONS
            filename = "test_parkinsons_master_hourly.csv"    
            with open(filename, 'ab') as csvfile:
                linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                linewriter.writerow([rms_abs, rms_1hz, rms_3hz, rms_6hz, rms_10hz, label_id,a_file]) 

calculate_RMS()


