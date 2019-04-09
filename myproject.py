from flask import Flask, render_template, request, url_for, redirect, session
from flask_bootstrap import Bootstrap
import pymongo

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
#def hello():
	#return "<h1 style='color:blue'>Hello World2!</h1>"

@app.route('/')
def homepage():
    client = pymongo.MongoClient('mongodb://localhost:27017')
    db = client.dust
    collection = db.recent
    results = collection.find()
    client.close()
    return render_template('main.html', recentData=results)


@app.route("/about")
def about():
	return render_template('about.html', title='About')

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
	return render_template('get.html')
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

@app.route('/login')
def login_form():
	return render_template('login.html')

@app.route('/login', methods = ['POST'])

def login():
    if request.method == 'POST':
        if(request.form['id'] == 'admin' and request.form['pw'] == 'admin123'):
            session['logged'] = True
            #session['user'] = request.form['id']
            #return 'Hi, ' + request.form['id']
            return render_template('logout.html')#수은 수정 logout.html
        else:
            return """<script>alert("wrong!");location.href='/login';</script>"""
    else:
        return """<script>alert("not allowd!");location.href='/login';</script>"""

@app.route('/logout')#수은 수정 logout 구현
def logout():
	session.clear()
	return redirect(url_for('login'))
	#return index()


app.secret_key = 'sample_secret'

if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True)
