import os
import urllib
from bs4 import BeautifulSoup
from urlparse import urlsplit

def getPic(url):
	html = urllib.urlopen(url)
	bsp = BeautifulSoup(html,'html.parser')
	pics = bsp.find_all('img',{'class':'BDE_Image'})
	for picurl in pics:
		downloadPic(picurl['src'])

def downloadPic(picurl):
	
	img = urllib.urlopen(picurl).read()
	fileName = os.path.basename(urlsplit(picurl)[2])
	fileWrite = open(fileName,'wb')
	fileWrite.write(img)
	fileWrite.close()

if __name__ == '__main__':
	getPic('http://tieba.baidu.com/p/2166231880')