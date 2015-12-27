from PIL import Image, ImageDraw, ImageFont

#is

global fontPath 
fontPath = '/Library/Fonts/Futura.ttc'
def addNumber(imgPath,number):
	txt = str(number)
	img = Image.open(imgPath)
	txtfont = ImageFont.truetype(fontPath,20)
	size = img.size
	draw = ImageDraw.Draw(img)
	draw.text((size[0]-20,size[1]/4),txt,fill=(250,0,0),font=txtfont)
	print(img.format,img.size,img.mode)
	img.show()
	img.save('pic.jpg')

addNumber('012627202.jpg',1)

