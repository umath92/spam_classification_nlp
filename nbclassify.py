import sys
from decimal import *
import math
import copy

pPos=0
pNeg=0

modelFile=sys.argv[1]
testFile=sys.argv[2]

num_lines = sum(1 for line in open(modelFile))

ramInputP={}
ramInputN={}
dic={}


typeFile="";
uniqW=0
with open(modelFile, "r") as f:
	# typeFile = POSITVE or SPAM. Telling us which file it is.
	typeFile=f.readline().split("\n")[0]
	pPos=f.readline().split("\n")[0]
	pNeg=f.readline().split("\n")[0]
	i=0

	for line in f:
		line.split("\n")[0].split(" ")
		key=int(line.split("\n")[0].split(" ")[0])
		if int(line.split("\n")[0].split(" ")[0]) not in dic:
			dic[key]=1
		ramInputP[key]=line.split("\n")[0].split(" ")[1]
		ramInputN[key]=line.split("\n")[0].split(" ")[2]
		i=i+1
	uniqW=(i/2)
	# uniqW is the number of unique words in model file. WE need to ingore others.
if(typeFile=="HAM"):
	outFile = open("spam.nb.out", 'w')
else:
	outFile = open("sentiment.nb.out", 'w')




with open(testFile, "r") as f:
	for line in f:
		line=line.split("\n")[0].split(" ")
		words=[]
		#print(line)
		for w in line:
			words=words+[(w.split(":")[0])]
			words=words+[(w.split(":")[1])]
		#print words
		pP=0
		pN=0
		# Jump through alternate stuff
		addvalP=0
		addvalN=0
		for i in range(0,len(words)):
			if(i%2==0):
				if int(words[i]) in dic:
					addvalP=addvalP+math.log(float(ramInputP[int(words[i])]))*float(words[i+1])
					addvalN=addvalN+math.log(float(ramInputN[int(words[i])]))*float(words[i+1])

		addvalP=addvalP+math.log(float(pPos))
		addvalN=addvalN+math.log(float(pNeg))

		if(typeFile=="POSITIVE"):
			if(addvalP>=addvalN):
				print("POSITIVE")
				outFile.write("POSITIVE")
				#outFile.write(str(addvalP))
				#outFile.write(" ")
				#outFile.write(str(addvalN))
				outFile.write("\n")
			else:
				print("NEGATIVE")
				outFile.write("NEGATIVE")
				#outFile.write(str(addvalP))
				#outFile.write(" ")
				#outFile.write(str(addvalN))
				outFile.write("\n")
		elif(typeFile=="HAM"):
			if(addvalP>=addvalN):
				print("HAM")				
				outFile.write("HAM")
				#outFile.write(str(addvalP))
				#outFile.write(" ")
				#outFile.write(str(addvalN))
				outFile.write("\n")
			else:
				print("SPAM")
				outFile.write("SPAM")
				#outFile.write(str(addvalP))
				#outFile.write(" ")
				#outFile.write(str(addvalN))
				outFile.write("\n")
				





