import string
import random
user_id=1

def new_password(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size)) #tuple comprehension

def new_user():
	user='team'+str(user_id)
	user_id=user_id+1
	print 'user=',user
	return user

a=new_user()
print a
#send_id=raw_input('Enter sender Email ID:')
#password=raw_input('Enter Email password:')



