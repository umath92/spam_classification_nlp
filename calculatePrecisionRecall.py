import sys
from decimal import *
import math
import copy
import random

correct=sys.argv[1]
predict=sys.argv[2]
p=sys.argv[3]
n=sys.argv[4]
correctFile = open(correct, 'r')
predictFile = open(predict, 'r')


posCorrect=0
negCorrect=0

posPre=0
nedPre=0

posInter=0
negInter=0

count=0
with open(correct, "r") as f:
	for l in f:
		count=count+1

print(count)

for i in range(0,count):
	cc=correctFile.readline().split(" ")[0]
	cc=cc.split("\n")[0]
	pp=predictFile.readline().split("\n")[0]
	
	if cc==p:
		posCorrect=posCorrect+1
	else:
		negCorrect=negCorrect+1
	if pp==p:
		posPre=posPre+1
	else:
		nedPre=nedPre+1
	if(pp==cc and pp==p):
		posInter=posInter+1
	if(pp==cc and pp==n):
		negInter=negInter+1
	i=i+1

#print (posPre)
if(posPre==0):
	precisionP=0	
else:
	precisionP=float((posInter)/(posPre))

if(nedPre==0):
	precisionN=0
else:	
	precisionN=float((negInter)/(nedPre))

if(posCorrect==0):
	recallP=0
else:
	recallP=float((posInter)/(posCorrect))

if(negCorrect==0):	
	recallN=0
else:
	recallN=float((negInter)/(negCorrect))
if(precisionP+recallP==0):
	fP=0
else:
	fP=float(2*precisionP*recallP)/(precisionP+recallP)

if(precisionN+recallN==0):
	fN=0
else:
	fN=float(2*precisionN*recallN)/(precisionN+recallN)




print(precisionP,precisionN,recallP,recallN,fP,fN)

