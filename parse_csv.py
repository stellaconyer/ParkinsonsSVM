import os
import sys
import tarfile
from datetime import datetime

#Take in a CSV from CLI
#Choose to write to file or print to standard output
# -----------




#extract the accel file from the tarball
def extract_accel_tar(a_tar):
    match = ["accel", ".csv"]
    with tarfile.open(a_tar) as tar:
        subdir_and_files = [
            tarinfo for tarinfo in tar.getmembers()
            if all(x in tarinfo.name for x in match)
            ]
        tar.extractall(path="extracted", members=subdir_and_files)

#extract files
#path is currently set to csv_files
def extract_from_path():
    path = r'csv_files'

    for dir_entry in os.listdir(path):
        my_tar = os.path.join(path, dir_entry)
        extract_accel_tar(my_tar)


def parse_lines(lines_in_file):
    with open("master_hourly.csv", 'ab') as master_file:
        master_file.write(lines_in_file)

#open all files to parse out lines
#rootdir currently assigned to extracted
#TO DO: make this more efficient! 
def open_files():
    rootdir = "extracted"
    for root, subFolders, files in os.walk(rootdir):
        for a_file in files:
            with open(os.path.join(root, a_file), 'r') as file_to_read:
                for lines in file_to_read:
                    parse_lines(lines)


#initial RMS calculation
#Not sure if this should be using the CSV module 
test_file="extracted/HumDynLog_CHERRY_LGE_LGE_A000002872F302_20120122_080000_20120122_090000/hdl_accel_CHERRY_20120122_080000.csv"

def calculate_RMS(a_file):
    startTime = datetime.now()
    x_abs = 0
    x_1hz = 0
    x_3hz = 0
    x_6hz = 0
    x_10hz = 0
    length = 0

    with open(a_file,'r') as csv_file:
        csv_file.next()
        for line in csv_file:
            length +=1
            line = line.split(",")
            x_abs += float(line[2])
            x_1hz += float(line[6])
            x_3hz += float(line[7])
            x_6hz += float(line[8])
            x_10hz += float(line[9])
    x_abs_avg = (x_abs/length)
    x_1hz_avg = (x_1hz/length)
    x_3hz_avg = (x_3hz/length)
    x_6hz_avg = (x_6hz/length)
    x_10hz_avg = (x_10hz/length)
    print x_abs_avg, x_1hz_avg, x_3hz_avg, x_6hz_avg, x_10hz_avg
    print(datetime.now()-startTime)

calculate_RMS(test_file)

# Average absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis over one hour (or length of file if shorter than one hour) (eg x_abs, x_1hz, x_3hz, x_6hz, x_10hz)
#take root mean square of the x,y,z values to come up with rms_abs, rms_1, rms_3, rms_6, rms_10
#append data to master_hourly.CSV



# master_file = open(master_hourly.CSV,'ab')
# master_file.write()