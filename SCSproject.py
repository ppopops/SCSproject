__author__ = 'Hong'
from flask import Flask
from MongoDB import Connect
from Salle import *
from Batiment import *
app = Flask(__name__)

db = Connect()


@app.route('/SCSproject/api/getsalle', methods=['GET'])
def get_salle():
    salle = Salle(db)
    result = salle.ReturnSalle()

    i = 0
    for s in result :
        batiment = Batiment(db)
        batimentDocument = batiment.ReturnBatimentid(s["idBatiment"])
        result[i]["idBatiment"] = batimentDocument
        i = i+ 1

    return jsonify({'salle': result})

@app.route('/SCSproject/api/setsalle', methods=['POST'])
def create_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = "0"   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    itemID = salle.InsertSalle()

    return jsonify(salle={"_id": itemID})
    #return jsonify(result={"status": 200})


@app.route('/SCSproject/api/getsalleid/<string:salle_id>', methods=['GET'])
def get_salle_id(salle_id):
    salle = Salle(db)
    result = salle.ReturnSalleid(salle_id)
    return jsonify({'salle': result})

@app.route('/SCSproject/api/updatesalle', methods=['POST'])
def update_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = salle.get ("_id")
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    salle.UpdateSalle()

    return jsonify(result={"status": 200})

@app.route('/SCSproject/api/deletesalle', methods=['POST'])
def delete_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    id = salle.get("_id")   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, id )
    salle.DeleteSalle()

    return jsonify(result={"status": 200})
##################################################################################################################

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