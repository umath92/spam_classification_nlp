import sys
from decimal import *
import math
import copy
import random

trainFile=sys.argv[1]
spl=sys.argv[2]
train75=sys.argv[3]
test=sys.argv[4]

count=0
with open(trainFile, "r") as f:
	for line in f:
		count+=1
	f.close()

test25=sys.argv[5]

numTrain={}
while(len(numTrain)<float((int(spl)/100))*count):
	le=random.randrange(0,count)
	if le not in numTrain:
		numTrain[int(le)]=1

numTest={}
for i in range(0,count):
	if i not in numTrain.keys():
		numTest[i]=1

print (count,len(numTrain),len(numTest))
#Need to pick lines and put in file
tain75File= open(train75, 'w')
test25File= open(test25, 'w')

countNum=0
with open(trainFile, "r") as f:
	for line in f:
		if countNum in numTrain.keys():
			tain75File.write(line)
		elif countNum in numTest.keys():
			#print(1234)
			test25File.write(line)
		countNum=countNum+1
tain75File.close()
test25File.close()
testFile= open(test, 'w')


with open(test25, "r") as f:
	for line in f:
		line1=line.split(" ")
		if(line1[0]=="+1" or line1[0]=="-1"):
			flag=0
			for y in range (0, len(line1)):
				if(flag==0):
					testFile.write(line1[y]);
					flag=1
				else:	
					testFile.write(" "+line1[y]);
		else:
			flag=0
			for y in range (1, len(line1)):
				if(flag==0):
					testFile.write(line1[y]);
					flag=1
				else:	
					testFile.write(" "+line1[y]);


	









