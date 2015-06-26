import sys

if (len(sys.argv) != 2):
	print("Usage : python ReadFile.py filename")
	sys.exit()

scriptname = sys.argv[0]
filename = sys.argy[1]

file = open(scriptname, "r")
lines = file.readlines()
file.close()

for line in lines:
	print(line)
