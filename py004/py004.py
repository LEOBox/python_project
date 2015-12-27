
def readFile(filePath):
	files = open(filePath,'r')
	fileText = files.read()
	files.close()
	return fileText

def countNumber():
	fileText = readFile('READ.txt')
	fileList = fileText.split(' ')
	print fileList
	number = len(fileList)
	print number

countNumber()
