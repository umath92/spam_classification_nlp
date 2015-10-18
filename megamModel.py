import sys
from decimal import *
import math
import copy


runOn=sys.argv[1]
isd=sys.argv[2]
inputFile=sys.argv[3]
testFile=sys.argv[4]



if(runOn=="megam"):
	if isd=='IMDB':
		outFileP = open("sentiment.megam.train", 'w')
		outFileS = open("sentiment.megam.test", 'w')
		with open(inputFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				if(line1[0]=="POSITIVE"):
					outFileP.write("1")
					for y in range (1, len(line1)):
						s=line1[y].split(":")
						outFileP.write(" "+s[0]+" "+s[1]);
				elif(line1[0]=="NEGATIVE"):
					outFileP.write("0")
					for y in range (1, len(line1)):
						s=line1[y].split(":")
						outFileP.write(" "+s[0]+" "+s[1]);

		with open(testFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				outFileS.write("1")
				for y in range (0, len(line1)):
						s=line1[y].split(":")
						outFileS.write(" "+s[0]+" "+s[1]);	

					

	if isd=='SPAM': 
		outFileP = open("spam.megam.train", 'w')
		outFileS = open("spam.megam.test", 'w')
		with open(inputFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				if(line1[0]=="SPAM"):
					outFileP.write("1")
					for y in range (1, len(line1)):
						s=line1[y].split(":")
						outFileP.write(" "+s[0]+" "+s[1]);
				elif(line1[0]=="HAM"):
					outFileP.write("0")
					for y in range (1, len(line1)):
						s=line1[y].split(":")
						outFileP.write(" "+s[0]+" "+s[1]);

		with open(testFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				outFileS.write("1")
				for y in range (0, len(line1)):
						s=line1[y].split(":")
						outFileS.write(" "+s[0]+" "+s[1]);

elif (runOn=="svm"):
	if isd=='IMDB':
		outFileP = open("sentiment.svm.train", 'w')
		outFileTest = open("sentiment.svm.test", 'w')
		with open(inputFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				if(line1[0]=="POSITIVE"):
					outFileP.write("+1")
					for y in range (1, len(line1)):
						k=line1[y].split(":");
						outFileP.write(" "+str(int(k[0])+1)+":"+k[1]);
				elif(line1[0]=="NEGATIVE"):
					outFileP.write("-1")
					for y in range (1, len(line1)):
						k=line1[y].split(":");
						outFileP.write(" "+str(int(k[0])+1)+":"+k[1]);

		with open(testFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				outFileTest.write("+1")
				for y in range (0, len(line1)):
					k=line1[y].split(":");
					outFileTest.write(" "+str(int(k[0])+1)+":"+k[1]);


	if isd=="SPAM":
		outFileP = open("spam.svm.train", 'w')
		outFileTest = open("spam.svm.test", 'w')
		with open(inputFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				if(line1[0]=="HAM"):
					outFileP.write("-1")
					dic={}
					for y in range (1, len(line1)):
						k=line1[y].split(":");
						#outFileTest.write(" "+str(int(k[0])+1)+":"+k[1]);
						dic[int(k[0])]=k[1].split("\n")[0]
					l=[]
					for key in dic.keys():
						l.append(key)
					l.sort();
					for key in l:
						outFileP.write(" "+str(int(key)+1)+":"+dic[key]);
					outFileP.write("\n");
				elif(line1[0]=="SPAM"):
					outFileP.write("+1")
					dic={}
					for y in range (1, len(line1)):
						k=line1[y].split(":");
						#outFileTest.write(" "+str(int(k[0])+1)+":"+k[1]);
						dic[int(k[0])]=k[1].split("\n")[0]
					l=[]
					for key in dic.keys():
						l.append(key)
					l.sort();
					for key in l:
						outFileP.write(" "+str(int(key)+1)+":"+dic[key]);
					outFileP.write("\n");
		with open(testFile, "r") as f:
			for line in f:
				line1=line.split(" ")
				#print(line1[0])
				outFileTest.write("+1")
				dic={}
				for y in range (0, len(line1)):
					k=line1[y].split(":");
					#outFileTest.write(" "+str(int(k[0])+1)+":"+k[1]);
					dic[int(k[0])]=k[1].split("\n")[0]
				l=[]
				for key in dic.keys():
					l.append(key)
				l.sort();
				
				for key in l:
					outFileTest.write(" "+str(int(key)+1)+":"+dic[key]);
				outFileTest.write("\n");






