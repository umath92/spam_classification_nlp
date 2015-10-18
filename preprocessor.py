import sys
from decimal import *
import math
import copy

imdbTrainFile=sys.argv[1]
newFile="imdbInput"
outFile = open(newFile, 'w')
s="";

with open(imdbTrainFile, "r") as f:
	for line in f:
		line1=line.split(" ")
		if(int(line1[0])>=7):
			outFile.write("POSITIVE")
			for y in range (1, len(line1)):
				outFile.write(" "+line1[y]);
		elif(int(line1[0])<=4):
			outFile.write("NEGATIVE")
			for y in range (1, len(line1)):
				outFile.write(" "+line1[y]);


outFile.write(s)
outFile.close()