import sys

def main():
	filename = "../" +sys.argv[1]+ "_master_hourly.csv"
	print filename
	with open(filename, 'r') as csvfile:
		for lines in csvfile:
			print lines

main()
