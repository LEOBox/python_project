from PIL import Image
import glob

iPhone = {'5':(1136,640),'6':(1134,750),'6P':(2208,1242)}

def getName(picPath):
	namePath = picPath + '/*.jpg'
	names = glob.glob(namePath)
	return names

def resizeaPic(picName,num,iPhoneType):
	img = Image.open(picName)
	size = iPhone[iPhoneType]
	img5 = img.resize(size)
	name = 'pic/name'+str(num)+'.jpg'
	img5.save(name)
	img.close()
	


names = getName('./pic')
num = 0
for name in names:
	resizeaPic(name,num,'6')
	num += 1