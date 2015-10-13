from flask import Flask, jsonify, render_template, request, redirect
import os
from pymongo import MongoClient

app = Flask(__name__)

# compteur pour id salle

#extraction de toutes les salles
result = []

#connection a la BD
def Connect():
    connection = MongoClient("ds057862.mongolab.com",57862)
    handle = connection["mongodbhong"]
    handle.authenticate("admin","root")
    return handle

#static variable for idSalle
def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars (idSalle= 0)
def InsertSalle(numeroSalle, etageSalle, capaciteSalle, equipementSalle, idBatiment):
    InsertSalle.idSalle += 1
    item = {"_id" : InsertSalle.idSalle , "numeroSalle" : numeroSalle,"etageSalle" : etageSalle, "capaciteSalle" : capaciteSalle, "equipementSalle" : equipementSalle, "idBatiment" : idBatiment }
    item_id = collection.insert_one(item).inserted_id
    return item_id


def ReturnSalle():
    with app.app_context():
        result = []
        for data in collection.find():
	        result.append(data)
        return result

def ReturnSalleid(id):
    with app.app_context():
        result = []
        for data in collection.find({"_id": id }):
	        result.append(data)
        return result
#        result =  collection.find({"_id": id })
#        print result
#        print result.next().numeroSalle
#        return result


def InsertNomFaculte2 (nomUniversite , nomFaculte):
    collection.update({"nomUniversite" : nomUniversite}, {"$addToSet":{"Faculte" : {"nomFaculte" : nomFaculte} } })

def InsertNomFaculte (nomUniversite , nomFaculte):
#    collection.update({"nomUniversite" : nomUniversite}, {"$set":{"Faculte.nomFaculte" : nomFaculte } })
    collection.update({"nomUniversite" : nomUniversite}, {"$set":{"Faculte." + nomFaculte : nomFaculte } })

def InsertBatiment2 (nomUniversite , nomFaculte, nomBatiment, adresseBatiment):
# add check nom existe pas deja
#    collection.update({"nomUniversite" : nomUniversite, "Faculte.nomFaculte": nomFaculte }, {"$push":{"(Faculte.1.nomFaculte)" : {"nomBatiment" : nomBatiment} } })
#    collection.update({"Faculte.nomFaculte": nomFaculte }, {"$push":{"(Faculte.1.nomFaculte)" : {"nomBatiment" : nomBatiment} } })
#    collection.update({"Faculte.nomFaculte": nomFaculte }, {"$push":{"Faculte" : { "Sciences" : { "nomBatiment" : nomBatiment} } } })
    collection.update({"Faculte.nomFaculte": nomFaculte }, {"$push":{"Faculte" : { "elemMatch" : { "$in":  [1] } }} })

def InsertBatiment (nomUniversite , nomFaculte, nomBatiment, adresseBatiment):
#    collection.update({"nomUniversite" : nomUniversite}, {"$set":{"Faculte.nomFaculte" : nomFaculte } })
    collection.update({"nomUniversite" : nomUniversite}, {"$set":{"Faculte." + nomFaculte + "." + nomBatiment : nomBatiment } })

####################DRIVER###############################################
db = Connect()
collection  = db.Salle


#Insert Salle
id = InsertSalle("214", "6", "12", "projecteur", 2)
id = InsertSalle("231", "12", "5", "", 2)
#id = InsertSalle("2432214", "5", "78", "", 2)
#id = InsertSalle("433", "6", "44", "projecteur", 8)
#id = InsertSalle("242214", "4", "25", "ordinateur", 10)


#ReturnSalle()

@app.route('/SCSproject/api/getsalle', methods=['GET'])
def get_salle():
    result = ReturnSalle()
    print result
#    result = [{u'idBatiment': 2, u'etageSalle': u'6', u'numeroSalle': u'214', u'capaciteSalle': u'12'}]
    return jsonify({'salle': result})

@app.route('/SCSproject/api/getsalleid/<int:salle_id>', methods=['GET'])
def get_salle_id(salle_id):
    result = ReturnSalleid(salle_id)
    print result
#    result = [{u'idBatiment': 2, u'etageSalle': u'6', u'numeroSalle': u'214', u'capaciteSalle': u'12'}]
    return jsonify({'salle': result})

@app.route('/SCSproject/api/setsalle', methods=['POST'])
def create_salle():
    as1 = ""
    content = request.get_json(force = True)

    print content
    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capaciteSalle","")
    equipementSalle =  salle.get ("equipementSalle","")
    idBatiment =  salle.get ("idBatiment","")
    InsertSalle(numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment )

    return jsonify(result={"status": 200})



if __name__ == '__main__':
    app.run(host='0.0.0.0')

#result = []
#result = [{'1': 1}, {'2': 2}]
#jsonify({'result': result})
#Insert Faculte
#InsertNomFaculte ("UdeS" , "Sciences")
#InsertNomFaculte ("UdeS" , "Math")

#insert Batiment
#InsertBatiment("UdeS", "Sciences", "Schulich", "425 Sherbrooke")

#print collection
#test = collection.find_one()
#print test