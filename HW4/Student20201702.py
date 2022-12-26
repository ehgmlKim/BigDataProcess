from numpy import *
from os import listdir
import operator
import sys

def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount={}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]
  
def img2vector(filename):
    returnVect = zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32*i+j] = int(lineStr[j])
    return returnVect

def trainMat(trainfile):
    hwLabels = []
    trainingFileList = listdir(trainfile)
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('%s/%s' % (trainfile, fileNameStr))
    return hwLabels, trainingMat
   
def hwClassifier(trainingMat, hwLabels, test, testtxt, k):
    testData = img2vector('%s/%s' % (test, testtxt))
    classifierResult = classify0(testData, trainingMat, hwLabels, k)
    #print("Result: %d" % classifierResult)
    return classifierResult
   
trainfile = sys.argv[1]
testfile = sys.argv[2]

test = listdir(testfile)
m = len(test)
reList = []
error = 0
errorList = []
hwLabels, trainingMat = trainMat(trainfile)
for k in range(1,21):
	for testtxt in test:
		result = (hwClassifier(trainingMat, hwLabels, testfile, testtxt, k))
		testtxt_name = testtxt.split('.')[0]
		testtxt_num = int(testtxt_name.split('_')[0])
		if result != testtxt_num:
			error += 1
	errorList.append(int(error/m*100))
	

for i in errorList:
	print(i)


