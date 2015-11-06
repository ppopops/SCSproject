# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from pymongo import MongoClient
from MongoDB import Connect
from flask import Blueprint
from flask import Flask
from flask import jsonify
from Batiment.Batiment import Batiment
from Salle import *


salle_app = Blueprint('salle_app', __name__)


db= Connect()

@salle_app.route('/salle')
def index():
	salle = Salle(db)
	return jsonify({'salle': salle.ReturnSalle()})

@salle_app.route('/SCSproject/api/getsalle', methods=['GET'])
def get_salle():
    #salle = Salle(db)
    #result = salle.ReturnSalle()
    result = Salle.GetAllSalle(db)
    #print result
    i = 0
    for s in result :
        #batiment = Batiment(db)
        batimentDocument = Batiment.GetIdBatimentid(db, s["idBatiment"])
        result[i]["idBatiment"] = batimentDocument
        i = i+ 1

    return jsonify({'salle': result})

@salle_app.route('/SCSproject/api/setsalle', methods=['POST'])
def create_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numero","")
    etageSalle =  salle.get ("etage","")
    capaciteSalle =  salle.get ("capacite","")
    equipementSalle =  salle.get ("equipement","")
    idBatiment =  salle.get ("idBatiment","")
    statut =  salle.get ("statut","")
    description =  salle.get ("description","")
    id = "0"   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, statut, description, id )
    itemID = salle.InsertSalle()

    return jsonify(salle={"_id": itemID})
    #return jsonify(result={"status": 200})


@salle_app.route('/SCSproject/api/getsalleid/<string:salle_id>', methods=['GET'])
def get_salle_id(salle_id):
    #salle = Salle(db)
    result = Salle.GetIdSalle(db,salle_id)

    print result[0].get ("idBatiment")
    #batiment = Batiment(db)
    batimentDocument = Batiment.GetIdBatimentid(db, result[0].get("idBatiment"))
    result[0]["idBatiment"] = batimentDocument

    return jsonify({'salle': result})

@salle_app.route('/SCSproject/api/updatesalle', methods=['POST'])
def update_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numero","")
    etageSalle =  salle.get ("etage","")
    capaciteSalle =  salle.get ("capacite","")
    equipementSalle =  salle.get ("equipement","")
    idBatiment =  salle.get ("idBatiment","")
    statut =  salle.get ("statut","")
    description =  salle.get ("description","")
    id = salle.get ("_id")
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, statut, description, id )
    salle.UpdateSalle()

    return jsonify(result={"status": 200})

@salle_app.route('/SCSproject/api/deletesalle', methods=['POST'])
def delete_salle():
    content = request.get_json(force = True)
    print content

    sallei = content.get("salle")
    salle= sallei[0]
    numeroSalle =  salle.get ("numeroSalle","")
    etageSalle =  salle.get ("etageSalle","")
    capaciteSalle =  salle.get ("capacite","")
    equipementSalle =  salle.get ("equipement","")
    idBatiment =  salle.get ("idBatiment","")
    statut = salle.get ("statut","")
    description =  salle.get ("description","")
    id = salle.get("_id")   #contructor will set id
    salle = Salle( db, numeroSalle ,etageSalle, capaciteSalle, equipementSalle ,idBatiment, statut, description, id )
    salle.DeleteSalle()

    return jsonify(result={"status": 200})