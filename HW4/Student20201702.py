import sys
import kNN
import numpy as np
from os import listdir
import sys

    
trainfile = sys.argv[1]
testfile = sys.argv[2]

test = listdir(testfile)
m = len(test)
reList = []
error = 0
errorList = []
hwLabels, trainingMat = kNN.trainMat(trainfile)
for k in range(1,21):
	for testtxt in test:
		result = (kNN.hwClassifier(trainingMat, hwLabels, testfile, testtxt, k))
		testtxt_name = testtxt.split('.')[0]
		testtxt_num = int(testtxt_name.split('_')[0])
		if result != testtxt_num:
			error += 1
	errorList.append(int(error/m*100))
	

for i in errorList:
	print(i)


