import sys
from decimal import *
import math
import copy

trainFile=sys.argv[1]
modelFile=sys.argv[2]

# Do the following if the training file is for SENTIMENT!

countPositive=0
countNegative=0
'''
Get maximum no of words from file first.
'''
identifier=""
with open(trainFile, "r") as C:
	identifier=C.readline().split(" ")[0]

if(identifier=="POSITIVE" or identifier=="NEGATIVE"):
	# change this to a set
	maxUniq={}
	with open(trainFile, "r") as f1:
		for l in f1:
			l=l.split("\n")[0].split(" ")[1:]
			#print l
			for i in range(0,len(l)):
				key=int(l[i].split(":")[0])
				if key not in maxUniq.keys():
					maxUniq[key]=int(l[i].split(":")[1])
				i=i+1
		f1.close()	
	#maxUniq=maxUniq+1

	print(len(maxUniq))
	#maxUniq=89527

	indexWordsPositive={}
	indexWordsNegative={}

	with open(trainFile, "r") as f:
		for line in f:
			words=line.split("\n")[0].split(" ")
			if words[0]=="POSITIVE":
				countPositive=countPositive+1
				for box in words[1:]:
					colWords1=int(box.split(":")[0])
					colWords2=int(box.split(":")[1])
					if colWords1 in indexWordsPositive.keys():
						indexWordsPositive[colWords1]=indexWordsPositive[colWords1]+colWords2
					else:
						indexWordsPositive[colWords1]=colWords2
			elif words[0]=="NEGATIVE":
				countNegative=countNegative+1
				for box in words[1:]:
					colWords1=int(box.split(":")[0])
					colWords2=int(box.split(":")[1])
					if colWords1 in indexWordsNegative.keys():
						indexWordsNegative[colWords1]=indexWordsNegative[colWords1]+colWords2
					else:
						indexWordsNegative[colWords1]=colWords2

	totalPos=0
	totalNeg=0
	for i in indexWordsPositive.keys():
		totalPos=totalPos+indexWordsPositive[i]
	for i in indexWordsNegative.keys():
		totalNeg=totalNeg+indexWordsNegative[i]


	print(countPositive,countNegative,totalPos,totalNeg)
	modelOut = open(modelFile, 'w')
	modelOut.write("POSITIVE\n");
	modelOut.write(str(countPositive/(countPositive+countNegative)))
	modelOut.write("\n")
	modelOut.write(str(countNegative/(countPositive+countNegative)))
	modelOut.write("\n")
	uniqK={}

	for key in indexWordsPositive.keys():
		uniqK[key]=1
		modelOut.write(str(key));
		modelOut.write(" ");
		modelOut.write(str((indexWordsPositive[key]+1)/(totalPos+len(maxUniq)))+" ")
		if key in indexWordsNegative:
			modelOut.write(str((indexWordsNegative[key]+1)/(totalNeg+len(maxUniq)))+"\n")
		else:
			modelOut.write(str(1/(totalNeg+len(maxUniq)))+"\n")

	for key in indexWordsNegative.keys():
		if key not in uniqK:
			uniqK[key]=1
			modelOut.write(str(key));
			modelOut.write(" ");
			modelOut.write(str((1)/(totalPos+len(maxUniq)))+" ")
			modelOut.write(str((indexWordsNegative[key]+1)/(totalNeg+len(maxUniq)))+"\n")



if(identifier=="HAM" or identifier=="SPAM"):
	# change this to a set
	maxUniq={}
	with open(trainFile, "r") as f1:
		for l in f1:
			l=l.split("\n")[0].split(" ")[1:]
			#print l
			for i in range(0,len(l)):
				key=int(l[i].split(":")[0])
				if key not in maxUniq.keys():
					maxUniq[key]=int(l[i].split(":")[1])
				i=i+1
		f1.close()	
	#maxUniq=maxUniq+1

	print(len(maxUniq))
	#maxUniq=89527

	indexWordsPositive={}
	indexWordsNegative={}

	with open(trainFile, "r") as f:
		for line in f:
			words=line.split("\n")[0].split(" ")
			if words[0]=="HAM":
				countPositive=countPositive+1
				for box in words[1:]:
					colWords1=int(box.split(":")[0])
					colWords2=int(box.split(":")[1])
					if colWords1 in indexWordsPositive.keys():
						indexWordsPositive[colWords1]=indexWordsPositive[colWords1]+colWords2
					else:
						indexWordsPositive[colWords1]=colWords2
			elif words[0]=="SPAM":
				countNegative=countNegative+1
				for box in words[1:]:
					colWords1=int(box.split(":")[0])
					colWords2=int(box.split(":")[1])
					if colWords1 in indexWordsNegative.keys():
						indexWordsNegative[colWords1]=indexWordsNegative[colWords1]+colWords2
					else:
						indexWordsNegative[colWords1]=colWords2

	totalPos=0
	totalNeg=0
	for i in indexWordsPositive.keys():
		totalPos=totalPos+indexWordsPositive[i]
	for i in indexWordsNegative.keys():
		totalNeg=totalNeg+indexWordsNegative[i]


	print(countPositive,countNegative,totalPos,totalNeg)
	modelOut = open(modelFile, 'w')
	modelOut.write("HAM\n");
	modelOut.write(str(countPositive/(countPositive+countNegative)))
	modelOut.write("\n")
	modelOut.write(str(countNegative/(countPositive+countNegative)))
	modelOut.write("\n")
	uniqK={}

	for key in indexWordsPositive.keys():
		uniqK[key]=1
		modelOut.write(str(key));
		modelOut.write(" ");
		modelOut.write(str((indexWordsPositive[key]+1)/(totalPos+len(maxUniq)))+" ")
		if key in indexWordsNegative:
			modelOut.write(str((indexWordsNegative[key]+1)/(totalNeg+len(maxUniq)))+"\n")
		else:
			modelOut.write(str(1/(totalNeg+len(maxUniq)))+"\n")

	for key in indexWordsNegative.keys():
		if key not in uniqK:
			uniqK[key]=1
			modelOut.write(str(key));
			modelOut.write(" ");
			modelOut.write(str((1)/(totalPos+len(maxUniq)))+" ")
			modelOut.write(str((indexWordsNegative[key]+1)/(totalNeg+len(maxUniq)))+"\n")

		
