from PIL import Image
import glob


def getName(picPath):
	namePath = picPath + '/*.jpg'
	names = glob.glob(namePath)
	return names

def resizeaPic(picName,num):
	img = Image.open(picName)
	img5 = img.resize((1136,640))
	name = 'pic/name'+str(num)+'.jpg'
	img5.save(name)
	img.close()
	


names = getName('./pic')
num = 0
for name in names:
	resizeaPic(name,num)
	num += 1
	