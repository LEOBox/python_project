import uuid

def creatID(num):	
	while num > 0:
		theCode = uuid.uuid4()
		print theCode
		num -= 1
		

creatID(200)