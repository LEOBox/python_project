import uuid
import pymysql

def creatID(num):
	con = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='test')
	cur = con.cursor()	
	while num > 0:
		theCode = uuid.uuid4()
		#print theCode
		cur.execute('insert into code values(%s)',str(theCode))
		num -= 1

	cur.close()
	con.close()
		

creatID(200)