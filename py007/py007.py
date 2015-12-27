import glob

def getFile(dirPaht):
	filePaht = dirPaht + '/*.py'
	return glob.glob(filePaht)

def readFile(fileName):
	f = open(fileName,'r')
	codes = f.read()
	return codes

def count(codes):
	lines = codes.split('\n')
	num,numT,numB = 0,0,0
	for line in lines:
		if '#' in line:
			numT += 1
		elif line == '':
			numB += 1
		else:
			num += 1

	print numT
	print numB
	print num

time = 1
for name in getFile('./code'):
	print str(time)+'for'
	time += 1
	count(readFile(name))