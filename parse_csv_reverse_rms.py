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
            rms_abs = 0
            rms_1hz = 0
            rms_3hz = 0
            rms_6hz = 0
            rms_10hz = 0

            length = 0

            # print a_file
            csv_file.next() #skip the header
            for line in csv_file:
                length +=1
                line = line.split(",")

                line_abs_rms = array([float(line[3]), float(line[11]), float(line[19])])
                rms_abs += sqrt(mean(line_abs_rms**2))

                line_1hz_rms = array([float(line[6]), float(line[14]), float(line[22])])
                rms_1hz += sqrt(mean(line_1hz_rms**2))
                
                line_3hz_rms = array([float(line[7]), float(line[15]), float(line[23])])
                rms_3hz += sqrt(mean(line_3hz_rms**2))

                line_6hz_rms = array([float(line[8]), float(line[16]), float(line[24])])
                rms_6hz += sqrt(mean(line_6hz_rms**2))

                line_10hz_rms = array([float(line[9]), float(line[17]), float(line[25])])
                rms_10hz += sqrt(mean(line_10hz_rms**2))

            if length > 600:

            # Calculate RMS for 5 dimensions
                total_abs_avg = rms_abs/length
                # print "rms abs", total_abs_avg

                total_1hz_avg = rms_1hz/length
                # print "rms 1hz", total_1hz_avg

                total_3hz_avg = rms_3hz/length
                # print "rms 3hz", total_3hz_avg

                total_6hz_avg = rms_6hz/length
                # print "rms 6hz",total_6hz_avg

                total_10hz_avg = rms_10hz/length
                # print "rms 10hz",total_10hz_avg

                label_id = 1

            # append data to master_hourly.CSV
            ## CHANGE SO IT TAKES THE FILENAME AND LABEL ID OF CONTROL OR PARKINSONS
                filename = "test2_parkinsons_master_hourly.csv"    
                with open(filename, 'ab') as csvfile:
                    linewriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
                    linewriter.writerow([total_abs_avg, total_1hz_avg, total_3hz_avg, total_6hz_avg, total_10hz_avg, label_id,a_file]) 

calculate_RMS()


