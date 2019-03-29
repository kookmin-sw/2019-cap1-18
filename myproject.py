from flask import Flask, render_template, request, url_for, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
#def hello():
	#return "<h1 style='color:blue'>Hello World2!</h1>"

@app.route('/')
def bootstrap():
    return render_template('main.html')


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


if __name__=="__main__":
	app.run(host='0.0.0.0', debug=True)
