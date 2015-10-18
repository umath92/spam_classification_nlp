import sys
from decimal import *
import math
import copy
import random

true=sys.argv[1]
imdbORspam=sys.argv[2]

if imdbORspam=="IMDB":

	testFile= open("megamImdbCompare", 'w')
	with open(true, "r") as f:
		for line in f:		
			if(int(line.split(" ")[0]))==0:
				testFile.write("NEGATIVE\n");
			if(int(line.split(" ")[0]))==1:
				testFile.write("POSITIVE\n");

if imdbORspam=="SPAM":

	testFile= open("megamSpamCompare", 'w')
	with open(true, "r") as f:
		for line in f:		
			if(int(line.split(" ")[0]))==0:
				testFile.write("HAM\n");
			if(int(line.split(" ")[0]))==1:
				testFile.write("SPAM\n");
