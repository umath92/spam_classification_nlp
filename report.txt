What each file does:

# 75/25 split: 75% data for training and 25% for testing.
# 25/75 split : 25% data for training and 75% for testing.

preprecessor.py: preprecesses labeledBow.fest
	python3 preprocessor.py <labeledBow.fest like formatted file>

preprecessorVocab.py: scans through enron1...enron5 and produces a file in Project Data format. produces a file named called 'labelVocab'
	python3 preprocessorVocab.py

preprecessorTestVocab.py: scans through spam_or_ham_test and produces the file in right format. produces a file names called 'labelVocabTest'
	python3 preprocessorTestVocab.py

splitData.py : intermediate function used for splitting into 75/25 and vice versa
	python3 splitData.py <formated input file> <split vale= % training> <trainig file> <testing file with removed labels> <testing file with labels (true file)>

nblearn.py : the nb learn program
	nblearn.py <training file> <model file>

nbclassify.py : the nb classififer
	nblearn.py <model file> <test file>

calculatePrecisionRecall.py : calculates precession, reacall and fscore given true data and output of classifier
	python3 calculatePrecisionRecall.py <true> <predicted> <POSITVE | SPAM> <NEGATIVE | HAM>

megamModel.py: the is using to preprocess files for svm and/or megama. like it will generate 'sentiment.svm.test' and 'sentiment.svm.train' for sentiment analysis for svm.
	python3 megamModel.py <svm | megam> <IMDM | SPAM> <training file in project data format> <testing file in project data format>

postScript.py : used for postprecessing files for megam and svm so that the files are in proper format before they go to calculatePrecisionRecall.py
	python3 postScript.py <svm | megam> <IMDB | SPAM> <megam.out or svm.out file from classifier> <the outputput file which we want> (required for svm)<true data> <true data filtered (by changing first line)>


megamPost.py: used for postprecessing files for megam so that the files are in proper format before they go to calculatePrecisionRecall.py
	python3 mrgamPosy.py <true result from split> <IMDB|SVM>




(1)
NAIVE BAYES:

	Edge case:
		if P(+)=P(-) then I add it to (+) set.
	Sentiment Analysis:
		How to run:
			Preprocess the file (#need to do this only once for all parts!): 
				-Convert given data to POSITIVE|NEGATIVE (given by val>=7 or <=4)
				-python3 preprocessor.py labeledBow.feat (will prodce 'imdbInput' as the output file)
			#change 75 to 25 for the 25/75 split.
			-python3 splitData.py imdbInput 75 trainSplit75.in testSplit25.in true25.in
			-python3 nblearn.py trainSplit75.in modelSplit75.in
			-python3 nbclassify.py modelSplit75.in testSplit25.in
			-python3 calculatePrecisionRecall.py true25.in sentiment.nb.out POSITIVE NEGATIVE
		(1)
		Split using 75% training and 25% testing data:
			P= Positive | N = Negative
			1st run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8731471906239228 0.8283069573006868 0.814993564993565 0.8828771483131763 0.8430687302379762 0.8547219226621475

			2nd run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8721009549795361 0.8152501506931886 0.8066246056782335 0.8782467532467533 0.8380858734841036 0.8455767427321038

		(2)
		Split using 25% traning and 75% testing data:

			P= Positive | N = Negative
			1st run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8592900913400393 0.8065538065538066 0.7918176006818666 0.8700341734301581 0.8241752148599945 0.8370922167993836

			2nd run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8612855348784108 0.819337403663297 0.8069312225906514 0.8707584299542602 0.8332228849127457 0.8442656765676568

		Comments:
		We see that precesion and recall for the 25/75 split is less than that of 75/25 split. This is because we have less examples to train on and so we'd expect the precision to be less for the 25/75 case.

		(3)
		Run:
			Preprocess the file: 
				-Convert given data to POSITIVE|NEGATIVE (given by val>=7 or <=4)
				-python3 preprocessor.py labeledBow.feat (will prodce 'imdbInput' as the output file)
			-python3 nblearn.py imdbInput sentiment.nb.model
			-python3 nbclassify.py sentiment.nb.model sentiment_test.feat

	SPAM/HAM:
		How to run:
			#change 75 to 25 for the 25/75 split.
			-python3 preprocessorVocab.py (to scan through enron1...enron5 and get it in Project Data format. produces a file named called 'labelVocab')
			-python3 splitData.py labelVocab 75 trainSplit75.in testSplit25.in true25.in
			-python3 nblearn.py trainSplit75.in modelSplit75.in
			-python3 nbclassify.py modelSplit75.in testSplit25.in
			-python3 calculatePrecisionRecall.py true25.in spam.nb.out HAM SPAM
		(1)
		Split using 75% training and 25% testing data:
			P= HAM | N = SPAM
			1st run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.984017435524882 0.9817726947819871 0.9815217391304348 0.9842350412038696 0.9827680029022311 0.983002325997495

			2nd run:
			P= HAM | N = SPAM
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.991475166790215 0.9817735716789344 0.980931426475981 0.9918555240793201 0.9861751152073732 0.986788796899771

		(2)
		Split using 25% training and 75% testing data:
			P= HAM | N = SPAM
			1st run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.9812620889748549 0.9794773893330152 0.979249607914103 0.9814681970349115 0.980254815530463 0.980471782621678

			P= HAM | N = SPAM
			2nd run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.9818247909850963 0.9803571428571428 0.9800435413642961 0.9821109123434705 0.9809333575449427 0.9812332439678284

		(3)
		Run:
			-python3 preprocessorVocab.py (to scan through enron1...enron5 and get it in Project Data format. produces a file named called 'labelVocab')
			-python3 preprocessorTestVocab.py (to scan through spam_or_ham_test and get the test data in right format. produces a file names called 'labelVocabTest')
			-python3 nblearn.py labelVocab spam.nb.model
			-python3 nbclassify.py spam.nb.model labelVocabTest (produces a file called 'spam.nb.out')

		Comments: 
		We see that the precision, recall and f-score for spam/ham is higher than that of sentient analysis. Since our data is not biased (since we have many training examples) we get precision and recall to be almost the same for spam/ham.




SVM:
	Sentiment Analysis:
		Labeled/Unlabeled data:
			-python3 megamModel.py svm IMDB imdbInput sentiment_test.feat (to generate 'sentiment.svm.test' and 'sentiment.svm.train')
			-./svm_learn sentiment.svm.train sentiment.svm.model
			-./svm_classify sentiment.svm.test sentiment.svm.model sentiment.svm.unlabeled.out
			-python3 postScript.py svm IMDB sentiment.svm.unlabeled.out sentiment.svm.out


		75/25:
			-python3 megamModel.py svm IMDB imdbInput sentiment_test.feat (to generate 'sentiment.svm.test' and 'sentiment.svm.train')
			-python3 splitData.py sentiment.svm.train 75 trainSplitImdb75.in testSplitImdb25.in true25Imdb.in
			-./svm_learn trainSplitImdb75.in sentiment.svm.model.75
			-./svm_classify testSplitImdb25.in sentiment.svm.model.75 sentiment.svm.unlabeled.out.75
			-python3 postScript.py svm IMDB sentiment.svm.unlabeled.out.75 sentiment.svm.out.75 true25Imdb.in true25Imdb.in.filtered
			-python3 calculatePrecisionRecall.py true25Imdb.in.filtered sentiment.svm.out.75 POSITIVE NEGATIVE

			P=Positive | N=Negative
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8591065292096219 0.8678255165628075 0.872185220424992 0.8543752018082015 0.8655964746616304 0.8610478359908884

		25/75:
			-python3 megamModel.py svm IMDB imdbInput sentiment_test.feat (to generate 'sentiment.svm.test' and 'sentiment.svm.train')
			-python3 splitData.py sentiment.svm.train 25 trainSplitImdb75.in testSplitImdb25.in true25Imdb.in
			-./svm_learn trainSplitImdb75.in sentiment.svm.model.75
			-./svm_classify testSplitImdb25.in sentiment.svm.model.75 sentiment.svm.unlabeled.out.75
			-python3 postScript.py svm IMDB sentiment.svm.unlabeled.out.75 sentiment.svm.out.25 true25Imdb.in true25Imdb.in.filtered
			-python3 calculatePrecisionRecall.py true25Imdb.in.filtered sentiment.svm.out.25 POSITIVE NEGATIVE

			P=Positive | N=Negative
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.7922440338722094 0.871739650634123 0.8847931219774315 0.7714134462678666 0.8359648677463574 0.8185137336403977

			Comments: Again we see less precision and recall for the 25/75 split case.

	SPAM/HAM:
		Labeled/Unlabeled data:
			-python3 megamModel.py svm SPAM labelVocab labelVocabTest (to generate 'spam.svm.test' and 'spam.svm.train')
			-./svm_learn spam.svm.train spam.svm.model
			-./svm_classify spam.svm.test spam.svm.model spam.svm.unlabeled.out
			-python3 postScript.py svm SPAM spam.svm.unlabeled.out spam.svm.out

		75/25:
			-python3 megamModel.py svm SPAM labelVocab labelVocabTest (to generate 'spam.svm.test' and 'spam.svm.train')
			-python3 splitData.py spam.svm.train 75 trainSplitSpam75.in testSplitSpam25.in true25Spam.in
			-./svm_learn trainSplitSpam75.in spam.svm.model.75
			-./svm_classify testSplitSpam25.in spam.svm.model.75 spam.svm.unlabeled.out.75
			-python3 postScript.py svm SPAM spam.svm.unlabeled.out.75 spam.svm.out.75 true25Spam.in true25Spam.in.filtered
			-python3 calculatePrecisionRecall.py true25Spam.in.filtered spam.svm.out.75 SPAM HAM

			p=SPAM| n=HAM
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.9316666666666666 0.9925519404155233 0.9932480454868514 0.9251004749725977 0.9614723082215342 0.9576399394856278

		25/75:
			-python3 megamModel.py svm SPAM labelVocab labelVocabTest (to generate 'spam.svm.test' and 'spam.svm.train')
			-python3 splitData.py spam.svm.train 25 trainSplitSpam75.in testSplitSpam25.in true25Spam.in
			-./svm_learn trainSplitSpam75.in spam.svm.model.75
			-./svm_classify testSplitSpam25.in spam.svm.model.75 spam.svm.unlabeled.out.75
			-python3 postScript.py svm SPAM spam.svm.unlabeled.out.75 spam.svm.out.75 true25Spam.in true25Spam.in.filtered
			-python3 calculatePrecisionRecall.py true25Spam.in.filtered spam.svm.out.25 SPAM HAM

			P=SPAM | N=HAM
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8984722071730415 0.9893588362068966 0.9905626567913033 0.8868630765515576 0.9422727272727273 0.935311345982427

			Comments: Again we see less precision and recall for the 25/75 split case. And since we have more data for the spam/ham case, we get higher precision and recall this compared to sentimet analysis.


	
MegaM:
	Sentiment Analysis:
		Labeled/Unlabeled:
			-python3 megamModel.py megam IMDB imdbInput sentiment_test.feat
			-./megam_i686.opt -fvals binary sentiment.megam.train > sentiment.megam.model
			-./megam_i686.opt -fvals -predict sentiment.megam.model binary sentiment.megam.test > sentiment.megam.out.un
			-python3 postScript.py megam IMDB sentiment.megam.out.un sentiment.megam.out

		75/25:
			-python3 megamModel.py megam IMDB imdbInput sentiment_test.feat
			-python3 splitData.py sentiment.megam.train 75 trainSplitImdb75.in testSplitImdb25.in true25Imdb.in
			-./megam_i686.opt -fvals binary trainSplitImdb75.in > sentiment.megam.model.75
			-./megam_i686.opt -fvals -predict sentiment.megam.model.75 binary true25Imdb.in> sentiment.megam.out.75.1
			-python3 postScript.py megam IMDB sentiment.megam.out.75.1 sentiment.megam.75.out
			-python3 megamPost.py true25Imdb.in IMDB
			-python3 calculatePrecisionRecall.py megamImdbCompare sentiment.megam.75.out POSITIVE NEGATIVE

			P=Positive | N=Negative
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.8622417031934878 0.8720549738219895 0.8756756756756757 0.8582930756843801 0.8689067676289636 0.8651192988151275

		25/75:
			-python3 megamModel.py megam IMDB imdbInput sentiment_test.feat
			-python3 splitData.py sentiment.megam.train 25 trainSplitImdb75.in testSplitImdb25.in true25Imdb.in
			-./megam_i686.opt -fvals binary trainSplitImdb75.in > sentiment.megam.model.75
			-./megam_i686.opt -fvals -predict sentiment.megam.model.75 binary true25Imdb.in> sentiment.megam.out.75.1
			-python3 postScript.py megam IMDB sentiment.megam.out.75.1 sentiment.megam.75.out
			-python3 megamPost.py true25Imdb.in IMDB
			-python3 calculatePrecisionRecall.py megamImdbCompare sentiment.megam.75.out POSITIVE NEGATIVE

			P=Positive | N=Negative
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.5877209418524765 0.9795545819642205 0.9940840904289034 0.28899181387333045 0.7387054990775994 0.4463112367961407

	SPAM/HAM:
		Labeled/Unlabeled:
			-python3 megamModel.py megam SPAM labelVocab labelVocabTest
			-./megam_i686.opt -fvals binary spam.megam.train > spam.megam.model
			-./megam_i686.opt -fvals -predict spam.megam.model binary spam.megam.test > spam.megam.out.un
			-python3 postScript.py megam SPAM spam.megam.out.un spam.megam.out

		75/25:
			-python3 megamModel.py megam SPAM labelVocab labelVocabTest
			-python3 splitData.py spam.megam.train 75 trainSplitSpam75.in testSplitSpam25.in true25Spam.in
			-./megam_i686.opt -fvals binary trainSplitSpam75.in > spam.megam.model.75
			-./megam_i686.opt -fvals -predict spam.megam.model.75 binary true25Spam.in> spam.megam.out.75.1
			-python3 postScript.py megam SPAM spam.megam.out.75.1 spam.megam.75.out
			-python3 megamPost.py true25Spam.in SPAM
			-python3 calculatePrecisionRecall.py megamSpamCompare spam.megam.75.out SPAM HAM

			P=SPAM | N=HAM
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.9730569948186528 0.9935993975903614 0.9940014114326041 0.9712918660287081 0.9834176994239833 0.982319002419505

		25/75:
			-python3 megamModel.py megam SPAM labelVocab labelVocabTest
			-python3 splitData.py spam.megam.train 25 trainSplitSpam75.in testSplitSpam25.in true25Spam.in
			-./megam_i686.opt -fvals binary trainSplitSpam75.in > spam.megam.model.75
			-./megam_i686.opt -fvals -predict spam.megam.model.75 binary true25Spam.in> spam.megam.out.75.1
			-python3 postScript.py megam SPAM spam.megam.out.75.1 spam.megam.75.out
			-python3 megamPost.py true25Spam.in SPAM
			-python3 calculatePrecisionRecall.py megamSpamCompare spam.megam.75.out SPAM HAM
			
			P=SPAM | N=HAM
			#1 run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.644310776942356 0.7115902964959568 0.7694241589847959 0.5725301204819278 0.701331296377128 0.6345306449459207

			#2 run:
			(precisionP,precisionN,recallP,recallN,fP,fN)=0.9616051809876258 0.9911316512615538 0.991533508227999 0.9598403290189912 0.9763400457934597 0.975235051926504

			Comment: The precision and recall for the 25/75 split seems very unstable. It changes almost everytime with a run.

Gneral comment whith hold for all methods:
	-The precison and recall is higher for the 75/25 split then the 25/75 split. This is expected as there is more training data for the 75/25 split. 
	- Out of the three methods, Naive Bayes and SVM showed more consistant and higher f-score for both spam/ham and sentiment analysis. Performance vise Mega-M and Naive Byes took roughly the same time to run. SVM took a long to long to optimize.
Note: Please be aware that the output file NAMES (content will depend on what script we run) for 25/75 split are the same for 75/25 split (I did that so that I dont generate many files). The concepts remain the same and it runs perfectly.





