from flask import Flask, render_template, request, flash,redirect, url_for
from forms import ContactForm
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
 
if __name__ == '__main__':
  app.run(debug=True)