import string
import random
user_id=1

def new_password(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))

def new_user():
	user='team'+str(user_id)
	user_id=user_id+1
	print 'user=',user
	return user





















password='qwer12#$new1'
