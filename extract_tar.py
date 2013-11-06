import os
import tarfile
import sys

#Extracting tarballs
#############################################################

#extract an accel file from the tarball
def extract_accel_tar(a_tar):
    match = ["accel", ".csv"]
    with tarfile.open(a_tar) as tar:
        subdir_and_files = [
            tarinfo for tarinfo in tar.getmembers()
            if all(x in tarinfo.name for x in match)
            ]
        tar.extractall(path="extracted", members=subdir_and_files)

#Navigate to filepath, run extract_accel_tar function
def extract_from_path():
    path = sys.argv[1]
    # path = r'csv_files'
    for dir_entry in os.listdir(path):
        print dir_entry
        my_tar = os.path.join(path, dir_entry)
        extract_accel_tar(my_tar)

extract_from_path()