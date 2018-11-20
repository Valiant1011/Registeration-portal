from flask import Flask,render_template,redirect,request,url_for

app=Flask(__name__) 

#127.0.0.1:5000/

@app.route('/')	 
def index():
	return render_template("index.html",data='Registeration Portal')

@app.route('/register',methods=['POST'])
def register():
	if request.method=='POST':
		user=str(request.form['username'])
		email=str(request.form['email'])
		value=user+'+'+email
	try:
		#Do database push here


		#Send email here

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
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response
    #This is to disable browser caching in IE and Chrome

if __name__ == '__main__':
	app.run(debug=True)
