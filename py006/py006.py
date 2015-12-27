import glob
import re

def getFile(filePath):
	fileNames = filePath + '/*.txt'
	return glob.glob(fileNames)

def getWords(fileName):
	fileContent = open(fileName,'r')
	texts = fileContent.read()
	words = re.findall(r'[A-Za-z]+',texts.lower())
	return words

def wordsCount(words):
	number = {}
	for wordM in words:
		if wordM in number:
			number[wordM] += 1
		else:
			number[wordM] = 1	
	return number

def count(number):
 	most = sorted(number.items(),key = lambda d: d[1])
 	print number
 	print "the most import word is%s" %(most[-1][0])

fileNames = getFile('./txt')
for fileName in fileNames:
	 count(wordsCount(getWords(fileName)))