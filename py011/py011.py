# -*- coding: utf-8 -*-
def filterRead():
	f = open('filter_words.txt')
	filterText = f.read()
	filterList = filterText.split('\n')
	return filterList

def filt(filterList):
	inputWord = raw_input()
	if inputWord in filterList:
		print 'F'
	else:
		print 'H'
#	jude = False
#	for word in filterList:
#		if inputWord == word:
#			jude = True
#
#	if jude == True:
#		print "F"
#	else:
#		print "H"
			

filterList = filterRead()
filt(filterList)


