import string
import random
import getpass

def new_password(size=6, chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size)) #tuple comprehension
def new_user(user_id):
	user='team'+str(user_id)
	return user


sender_id=raw_input('Enter sender Email ID:')
password=getpass.getpass(prompt='Enter Email Password[ Will not be visible while typing ]:')
