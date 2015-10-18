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

labelVoc = open("labelVocabTest", 'w')

# doinf spam files
enron=["spam_or_ham_test"]

for en in enron:	
	listdir=os.listdir(en)
	listdir.sort();
	for dirs in listdir:
		if(dirs!=".DS_Store"):
			dV={}
			#print(dirs)
			# open dirs and
			# open the file. split it using \n. for each in that. split using " ". search tokens in vocab; 
			with open(en+"/"+dirs, "r",encoding="latin1") as f:
				for line in f:
					line=line.split("\n")[0].split()
					for spaceSplitLine in line:
						if dVocab[spaceSplitLine] not in dV.keys():
							dV[dVocab[spaceSplitLine]]=1
						else:
							dV[dVocab[spaceSplitLine]]=dV[dVocab[spaceSplitLine]]+1

			
			#print(dV)
			#print("\n")
			d=1
			for key in dV:
				if(d==1):
					labelVoc.write(str(key)+":"+str(dV[key]))
					d=2
				else:
					labelVoc.write(" "+str(key)+":"+str(dV[key]))
			labelVoc.write("\n")

		
				

					


		
