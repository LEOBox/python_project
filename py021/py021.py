import os
from hashlib import sha256
from hmac import HMAC

def encrypyPassword(password,salt = None):
	if salt is None:
		salt = os.urandom(8)

	assert 8 == len(salt)
	assert isinstance(salt,str)
	if isinstance(password,unicode):
		password = password.encode('utf-8')
	assert isinstance(password,str)

	for i in xrange(10):
		password = HMAC(password,salt,sha256).digest()

	print salt+password
	return salt+password


def validataPassword(hashed, password):
	return hashed == encrypyPassword(password,salt = hashed[:8])
if __name__ == '__main__':
	hashed = encrypyPassword('dxz1992095')
	password = raw_input()
	if validataPassword(hashed,password):
		print "OK"
	else:
		print "Wrong"