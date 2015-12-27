import string
import random
from PIL import Image,ImageDraw,ImageFont,ImageFilter

ImageBgcolor = (200,200,200)
ImageColorMode = 'RGB'
fontPath = '/Library/Fonts/Futura.ttc'

def randomString(randomlength):
	return ''.join(random.sample(string.ascii_letters+string.digits,randomlength))

def radomColorNum():
	return random.randint(20,150)

def radomNum():
	return random.randint(10,300)

def creatImage(text):
	img = Image.new(ImageColorMode,(400,300),ImageBgcolor)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype(fontPath,50)
	strPosition = (125,125)
	draw.text(strPosition,text,(radomColorNum(),radomColorNum(),radomColorNum()),font)
	lines = random.randint(2,5)
	for line in xrange(lines):
		lineBeginPoint = (radomNum(),radomNum())
		lineEndPoint = (radomNum(),radomNum())
		draw.line([lineBeginPoint,lineEndPoint],(radomColorNum(),radomColorNum(),radomColorNum()))
	chance = random.randint(0,50)
	for w in xrange(400):
		for h in xrange(300):
			tmp = random.randint(0,50)
			if tmp > 60 - chance:
				draw.point((w,h),(radomColorNum(),radomColorNum(),radomColorNum()))
	img = img.filter(ImageFilter.BLUR)
	img.save('codePic.jpg')

text = randomString(4)
creatImage(text)