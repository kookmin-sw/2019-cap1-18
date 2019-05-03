

from flask import Flask,flash, render_template, request, url_for, redirect, session, abort
from flask_bootstrap import Bootstrap
import pymongo
import os

app = Flask(__name__)
Bootstrap(app)


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
	if not session.get('logged_in'): #로그인 되어 있지 않으면 로그인 페이지로 이동
		return render_template('login.html')
	else:
		#return render_template('logout.html') #임시
		return homepage()




@app.route('/main')
def homepage():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.dust
    collection = db.recent
    results = collection.find()
    client.close()
    return render_template('main.html', recentData=results, menu=1)


@app.route('/testimage')
def test_image2():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.dust
    ecollection = db.externaldust
    eresults = ecollection.find() 
    client.close()
    return render_template('test_image.html', testData=eresults)


@app.route('/details')
def test_chart():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.dust
    icollection = db.internaldust
    ecollection = db.externaldust
    iresults = icollection.find()
    eresults = ecollection.find() 
    client.close()
    return render_template('details.html', iData=iresults, eData=eresults, title='Details', menu=2)


"""@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
##-------------------------

@app.route('/test', methods = ['GET'])
def test():

      user = request.args.get('myName')
      return redirect(url_for('success', name = user))

if __name__ == '__main__':
   app.run(debug = True)	
"""
@app.route('/test')
def form():
	return render_template('get.html', menu=3)

@app.route('/join')
def join():
	return render_template('join.html', menu=4)

@app.route('/joinus', methods=['POST'])
def joinus():

	newuserid = request.form['id']
	newuserpw = request.form['pw']
	newidnum = request.form['idnum']

	client = pymongo.MongoClient('mongodb://localhost:27017')
	db = client.dust
	collection = db.account

	collection.insert({"id":newuserid, "pw":newuserpw, "idnum":newidnum})
	client.close()

	return render_template('joinus.html', firstname=newuserid)
#form action
@app.route('/hello', methods=['GET'] )
def action():
	temp1 = request.args.get('firstname')
	temp2 = request.args.get('lastname')
	temp3 = request.args.get('email')
	##firstname = request.form['firstname']
	##lastname = request.form['lastname']
	##email = request.form['email']
	return render_template('action.html', firstname=temp1, lastname=temp2, email=temp3)

#@app.route('/login')
#def login_form():
	#return render_template('login.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
	#폼에서 넘어온 데이터를 가져와 정해진 유저네임과 암호를 비교하고 참이면 세션을 저장한다.
	#회원정보를 DB구축해서 추출하서 비교하는 방법으로 구현 가능 - 여기서는 바로 적어 줌
	client = pymongo.MongoClient('mongodb://localhost:27017')
	db = client.dust
	collection = db.account
	
	#found = collection.find({"$and":[{"id":request.form['username']}, {"password":request.form['password'] }]})
	found = collection.find()
	for doc in found:
		li = list(doc.values())
		if li[1] == request.form['username'] and li[2] == request.form['password'] :
			session['logged_in'] = True

	flash('유저네임이나 암호가 맞지 않습니다.')
	return index()

@app.route('/logout')
def logout():
	session.clear()
	#return redirect(url_for('index'))
	return index()

if __name__ == '__main__':
	app.secret_key = os.urandom(24) #좀 더 알아 볼것. 시크릿키는 세션등의 기능을 위해 반드시 필요하다.
	app.run(debug=True, host='0.0.0.0')
app.secret_key = 'sample_secret'

#if __name__=="__main__":
	#app.run(host='0.0.0.0', debug=True)
