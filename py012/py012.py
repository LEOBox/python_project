def filt():
	f = open('filter_words.txt')
	filterList = f.read().split('\n')
	inputWords = raw_input()
	for word in filterList:
		if word in inputWords:
			inputWords = inputWords.replace(word,'*'*len(word))
	print inputWords

filt()