import os
import sys
import tarfile

#Take in a CSV from CLI
#Choose to write to file or print to standard output
# -----------


# TO APPEND TO CSV
# my_file = open("data.csv", "ab")


# path = r'/csv_files'
# data = {}

# for dir_entry in os.listdir(path):
#     dir_entry_path = os.path.join(path, dir_entry)
#     with open(dir_entry_path, 'r') as my_file:
#         data[dir_entry] = my_file.read()



#extract the accel file from the tarball
def extract_accel_tar(a_tar):
    match = ["accel", ".csv"]
    with tarfile.open(a_tar) as tar:
        subdir_and_files = [
            tarinfo for tarinfo in tar.getmembers()
            if all(x in tarinfo.name for x in match)
            ]
        tar.extractall(path="extracted", members=subdir_and_files)

#path is currently set to csv_files
def extract_from_path():

    path = r'csv_files'

    for dir_entry in os.listdir(path):
        my_tar = os.path.join(path, dir_entry)
        extract_accel_tar(my_tar)


#look in each tar file
# path = r'/csv_files'
# data = {}
# for dir_entry in os.listdir(path):
#     dir_entry_path = os.path.join(path, dir_entry)
#     with open(dir_entry_path, 'r') as my_file:
#         data[dir_entry] = my_file.read()




# with open('output.txt','w') as fout:
#     for root, subFolders, files in os.walk(rootdir):
#         if 'data.txt' in files:
#             with open(os.path.join(root, 'data.txt'), 'r') as fin:
#                 for lines in fin:
#                     dosomething()


def parse_lines(text):
    with open("master_hourly", "ab") as master_file:
        master_file.write(text)

#ASSIGN ROOTDIR TO OPEN AND PARSE FILES
def open_files():
    rootdir = "extracted"
    for root, subFolders, files in os.walk(rootdir):
        for a_file in files:
            with open(os.path.join(root, a_file), 'r') as file_to_read:
                for lines in file_to_read:
                    parse_lines(lines)


open_files()


# Average absolute.deviation, and PSD at 1, 3, 6, and 10hz for each axis over one hour (or length of file if shorter than one hour) (eg x_abs, x_1hz, x_3hz, x_6hz, x_10hz)
#take root mean square of the x,y,z values to come up with rms_abs, rms_1, rms_3, rms_6, rms_10
#append data to master_hourly.CSV





# master_file = open(master_hourly.CSV,'ab')
# master_file.write()