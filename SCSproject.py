from flask import Flask
from MongoDB import Connect
from Salle import *
app = Flask(__name__)

db = Connect()


@app.route('/SCSproject/api/getsalle', methods=['GET'])
def get_salle():
    salle = Salle(db)
    return jsonify({'salle': salle.ReturnSalle()})

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
    salle.InsertSalle()

    return jsonify(result={"status": 200})


@app.route('/SCSproject/api/getsalleid/<string:salle_id>', methods=['GET'])
def get_salle_id(salle_id):
    salle = Salle(db)
    result = salle.ReturnSalleid(salle_id)
    print result
#    result = [{u'idBatiment': 2, u'etageSalle': u'6', u'numeroSalle': u'214', u'capaciteSalle': u'12'}]
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')