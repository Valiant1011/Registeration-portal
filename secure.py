import string
import random
def new_password(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size)) #tuple comprehension
def new_user(user_id):
	user='team'+str(user_id)
	return user
send_id=raw_input('Enter sender Email ID:')
password=raw_input('Enter Email password:')
