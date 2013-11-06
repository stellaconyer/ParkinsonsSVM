import sys
import shutil
import os

def main():
	path = sys.argv[1]
	for a_file in os.listdir(path):
		if fnmatch.fnmatch(path,"\'HumDynLog_CHERRY_LGE_LGE_A000002872F302_20120122_080000_*"):
			print a_file

	    # shutil.copyfile(".", "newdir")


#     path = sys.stdin
#     # path = r'csv_files'

#     for dir_entry in os.listdir(path):
#         my_tar = os.path.join(path, dir_entry)
#         return my_tar
# main()


# HumDynLog_CHERRY_LGE_LGE_A000002872F302_20120122_080000_*

# find extracted  -name "HumDynLog_CHERRY_LGE_LGE_A000002872F302_20120122_080000_*" | python sort_tar_files.py
# find extracted  -name "*.csv" |head -5| python parse_csv.py


# find flox_extracted -name "*.csv"| python ~/hackbright/ParkinsonsSVM/parse_csv.py flox