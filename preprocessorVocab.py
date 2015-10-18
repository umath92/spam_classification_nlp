import sys
from decimal import *
import math
import copy
import os.path


num_lines = sum(1 for line in open("enron.vocab",encoding="latin1"))
vocab=['']*num_lines

dVocab={}
dV={}

i=0
with open("enron.vocab", "r",encoding="latin1") as f:
	for l in f:
		vocab[i]=l.split("\n")[0]
		i=i+1
		#print(vocab[i])
	f.close()

i=0
for item in vocab:
	dVocab[item]=i
	
	i=i+1

#print(dVocab)

labelVoc = open("labelVocab", 'w')

# doinf spam files
enron=["enron1","enron2","enron4","enron5"]

for en in enron:
	labell=["ham","spam"]	
	for label in labell:
		listdir=os.listdir(en+"/"+label)
		listdir.sort();
		for dirs in listdir:
			if(dirs!=".DS_Store"):
				dV={}
				#print(dirs)
				# open dirs and
				# open the file. split it using \n. for each in that. split using " ". search tokens in vocab; 
				with open(en+"/"+label+"/"+dirs, "r",encoding="latin1") as f:
					for line in f:
						line=line.split("\n")[0].split()
						for spaceSplitLine in line:
							if dVocab[spaceSplitLine] not in dV.keys():
								dV[dVocab[spaceSplitLine]]=1
							else:
								dV[dVocab[spaceSplitLine]]=dV[dVocab[spaceSplitLine]]+1

				
				if(label=='ham'):
					labelVoc.write("HAM")
				else:
					labelVoc.write("SPAM")
				#print(dV)
				#print("\n")
				for key in dV:
					labelVoc.write(" "+str(key)+":"+str(dV[key]))
				labelVoc.write("\n")

		
				

					


		
