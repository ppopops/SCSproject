from flask import Flask, render_template, request, flash,redirect, url_for
from forms import ContactForm, Authentification
from pymongo import MongoClient

app = Flask(__name__) 
 
app.secret_key = 'development key'

#connection a la BD
def Connect():
    connection = MongoClient("ds027789.mongolab.com",27789)
    handle = connection["machincon"]
    handle.authenticate("admin","root")
    return handle


def CreateCollection(db,name):
	db.countries.insert({"id":"1","name":name,"Language":"French"})

def DisplayAllElement(db):
	for result in db.countries.find():
		print(result)

def UpdateElement(db):
	db.countries.update({"name","Canada"},{"$set":{"Language":"Englishs"}}) 

def DeleteElement(db,name):
	db.countries.delete_one({"name":"Canada"})

def FindUser(db,login,password):
	cursor = db.users.find({"login": login},{"password":password})
	for document in cursor:
		return document


db = Connect()

@app.route('/contact', methods=['GET','POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
  	if form.validate() == False:
  		flash('All fields are required.')
  		return render_template('contact.html',form=form)
  	else:
  		CreateCollection(db,form.name.data)
  		return form.name.data 
  		#return redirect(url_for('home'))

  elif request.method=='GET':	
  	return render_template('contact.html', form=form)

@app.route('/')
def home():
  return render_template('home.html')
  
@app.route('/about')
def about():
  return render_template('about.html')
 
@app.route('/login', methods=['GET','POST'])
def login():
  form = Authentification()

  if request.method == 'POST':
  	if form.validate() == False:
  		flash('All fields are required.')
  		return render_template('login.html',form=form)
  	else:
  		test = FindUser(db,form.login.data,form.password.data)
  		return test
  		#return redirect(url_for('home'))

  elif request.method=='GET':	
  	return render_template('login.html', form=form)


if __name__ == '__main__':
  app.run(debug=True)