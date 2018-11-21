from Security import*
from flask import Flask,render_template,redirect,request,url_for
from flask_mail import Mail,Message
import os
app=Flask(__name__) 
contest_name='Kodeathon'
user_id=1

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']=sender_id
app.config['MAIL_PASSWORD']=password
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)

@app.route('/')	 
def index():
	return render_template("index.html",data='Registeration Portal')

@app.route('/register',methods=['POST'])
def register():
	if request.method=='POST':
		try:
			erno=str(request.form['erno'])
			email=str(request.form['email'])
			value=erno+'+'+email
			user=new_user(user_id)
			user_password=new_password()
			#Email process
			msg=Message(contest_name,sender=send_id,recipients=[email])
			message="Hello! Thank you for your "+contest_name+" registeration. Here are your login credentials : \n Username: "+user+ "\n Password: "+user_password
			msg.body=message
			mail.send(msg)
			#Do database push here


			#till here
			user_id+=1#successful insertion locks the previous user name
			return redirect(url_for('success',data=value))
		except:
			return redirect(url_for('error',data=value))
		
@app.route('/success/<data>')
def success(data):
	user,email=data.split('+')
	return render_template('success.html',name=user,email_id=email)

@app.route('/error/<data>')
def error(data):
	user,email=data.split('+')
	return render_template('fail.html',name=user,email_id=email)

@app.after_request
def add_header(response):	#This is to disable browser caching in Chrome
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

if __name__ == '__main__':
	app.run(debug=False)
