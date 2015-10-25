__author__ = 'Hong'
from flask import Flask
from MongoDB import Connect
from Salle import *
from Batiment import *
from Presentation import *
from Horaire import *
app = Flask(__name__)

db = Connect()

##################################################################################################################

@app.route('/SCSproject/api/getbatiment', methods=['GET','POST'])
def get_batiment():
    batiment = Batiment(db)
    if request.method == 'POST':
        content = request.get_json(force = True)
        print content

        batimentTemp = content.get("batiment")
        batiment= batimentTemp[0]
        nomBatiment =  batiment.get ("nomBatiment","")
        adresseBatiment =  batiment.get ("adresseBatiment","")
        faculteBatiment =  batiment.get ("faculteBatiment","")
        CampusBatiment =  batiment.get ("CampusBatiment","")
        id = "0"   #contructor will set id
        batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment , id )
        itemId = batiment.InsertBatiment()
        #print itemId
        return jsonify({'batiment': batiment.ReturnBatiment()})

    elif request.method=='GET':
        batiment = Batiment(db)
        return jsonify({'batiment': batiment.ReturnBatiment()})


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


@app.route('/SCSproject/api/setbatiment', methods=['POST'])
def create_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = "0"   #contructor will set id
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment , id )
    itemId = batiment.InsertBatiment()
    #print itemId

    return jsonify(batiment={"_id": itemId})
    #return jsonify(result={"status": 200})

@app.route('/SCSproject/api/getbatiment', methods=['GET'])
def get_batiment():
    batiment = Batiment(db)
    return jsonify({'batiment': batiment.ReturnBatiment()})

@app.route('/SCSproject/api/getbatimentid/<string:batiment_id>', methods=['GET'])
def get_batiment_id(batiment_id):
    batiment = Batiment(db)
    return jsonify({'salle': batiment.ReturnBatimentid(batiment_id)})

@app.route('/SCSproject/api/updatebatiment', methods=['POST'])
def update_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = batiment.get ("_id")
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment , id )
    batiment.UpdateBatiment()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletebatiment', methods=['POST'])
def delete_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nomBatiment","")
    adresseBatiment =  batiment.get ("adresseBatiment","")
    faculteBatiment =  batiment.get ("faculteBatiment","")
    CampusBatiment =  batiment.get ("CampusBatiment","")
    id = batiment.get("_id")   #contructor will set id
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, CampusBatiment, id )
    batiment.DeleteBatiment()

    return jsonify(result={"status": 200})


if __name__ == '__main__':
    app.run(host='0.0.0.0')