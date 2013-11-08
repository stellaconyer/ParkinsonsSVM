import sys


for line in sys.stdin: 
	filename = line.strip()
	length = 0

	with open(filename, 'r') as csvfile:
		for line in csvfile:
			length += 1
		print length