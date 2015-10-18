import sys
from decimal import *
import math
import copy

what=sys.argv[1]
isd=sys.argv[2]
inputFile=sys.argv[3]
OutptFile=sys.argv[4]
outFileP = open(OutptFile, 'w')


if what=="svm":
	if isd=='IMDB':
		flag=1
		with open(inputFile, "r") as f:
			for line in f:
				line=line.split("\n")[0];
				if float(line)>=0:
					if flag==1:
						outFileP.write("POSITIVE");
						flag=2;
					else:
						outFileP.write("\n"+"POSITIVE");
				if float(line)<0:
					if flag==1:
						outFileP.write("NEGATIVE");
						flag=2;
					else:
						outFileP.write("\n"+"NEGATIVE");

		if len(sys.argv)>5:
			inputTrue=sys.argv[5]
			OnputTrue=sys.argv[6]
			outFileP2=open(OnputTrue, 'w')
			with open(inputTrue, "r") as f:
				for line in f:
					line1=line.split(" ")
					#print(line1[0])
					if(line1[0]=="+1"):
						outFileP2.write("POSITIVE")
						for y in range (1, len(line1)):
							k=line1[y].split(":");
							outFileP2.write(" "+str(int(k[0])+1)+":"+k[1]);
					elif(line1[0]=="-1"):
						outFileP2.write("NEGATIVE")
						for y in range (1, len(line1)):
							k=line1[y].split(":");
							outFileP2.write(" "+str(int(k[0])+1)+":"+k[1]);

	if isd=='SPAM':
		flag=1
		with open(inputFile, "r") as f:
			for line in f:
				line=line.split("\n")[0];
				if float(line)>=0:
					if flag==1:
						outFileP.write("SPAM");
						flag=2;
					else:
						outFileP.write("\n"+"SPAM");
				if float(line)<0:
					if flag==1:
						outFileP.write("HAM");
						flag=2;
					else:
						outFileP.write("\n"+"HAM");

		if len(sys.argv)>5:
			inputTrue=sys.argv[4]
			OnputTrue=sys.argv[5]
			outFileP2=open(OnputTrue, 'w')
			with open(inputTrue, "r") as f:
				for line in f:
					line1=line.split(" ")
					#print(line1[0])
					if(line1[0]=="+1"):
						outFileP2.write("SPAM")
						for y in range (1, len(line1)):
							k=line1[y].split(":");
							outFileP2.write(" "+str(int(k[0])+1)+":"+k[1]);
					elif(line1[0]=="-1"):
						outFileP2.write("HAM")
						for y in range (1, len(line1)):
							k=line1[y].split(":");
							outFileP2.write(" "+str(int(k[0])+1)+":"+k[1]);

if what=="megam":
	if isd=='IMDB':
		with open(inputFile, "r") as f:
			for line in f:
				if(int(line.split("\t")[0])==1):
					outFileP.write("POSITIVE"+"\n")
				else:
					outFileP.write("NEGATIVE"+"\n")

	if isd=='SPAM':
		with open(inputFile, "r") as f:
			for line in f:
				if(int(line.split("\t")[0])==1):
					outFileP.write("SPAM"+"\n")
				else:
					outFileP.write("HAM"+"\n")

