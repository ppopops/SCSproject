# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from flask import Blueprint
from flask import Flask
from Batiment import *
from pymongo import MongoClient
from MongoDB import Connect


db= Connect()


batiments_app = Blueprint('batiments_app', __name__)


@batiments_app.route('/batiment')
def index():
    return db.batiment

@batiments_app.route('/SCSproject/api/getbatiment', methods=['GET'])
def get_batiment():
    batiment = Batiment(db)
    return jsonify({'batiment': batiment.ReturnBatiment()})


@batiments_app.route('/SCSproject/api/setbatiment', methods=['POST'])
def create_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nom","")
    adresseBatiment =  batiment.get ("adresse","")
    faculteBatiment =  batiment.get ("faculte","")
    campusBatiment =  batiment.get ("campus","")
    universite =  batiment.get ("universite","")
    id = "0"   #contructor will set id
    if Batiment.IsBatimentAlreadyExist(db,nomBatiment,universite)==False:
        batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, campusBatiment , universite, id )
        itemId = batiment.InsertBatiment()
        return jsonify(batiment={"_id": itemId})
    return "Already exist"
    #print itemId

@batiments_app.route('/SCSproject/api/getbatimentid/<string:batiment_id>', methods=['GET'])
def get_batiment_id(batiment_id):
    #batiment = Batiment(db)
    #return jsonify({'salle': batiment.ReturnBatimentid(batiment_id)})
    return jsonify({'batiment': Batiment.GetIdBatimentid(db,batiment_id)})

@batiments_app.route('/SCSproject/api/updatebatiment', methods=['POST'])
def update_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nom","")
    adresseBatiment =  batiment.get ("adresse","")
    faculteBatiment =  batiment.get ("faculte","")
    campusBatiment =  batiment.get ("campus","")
    universite =  batiment.get ("universite","")
    id = batiment.get ("_id")
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, campusBatiment , universite, id )
    batiment.UpdateBatiment()

    return jsonify(result={"status": 200})

@batiments_app.route('/SCSproject/api/deletebatiment', methods=['POST'])
def delete_batiment():
    content = request.get_json(force = True)
    print content

    batimentTemp = content.get("batiment")
    batiment= batimentTemp[0]
    nomBatiment =  batiment.get ("nom","")
    adresseBatiment =  batiment.get ("adresse","")
    faculteBatiment =  batiment.get ("faculte","")
    campusBatiment =  batiment.get ("campus","")
    universite =  batiment.get ("universite","")
    id = batiment.get("_id")   #contructor will set id
    batiment = Batiment( db, nomBatiment ,adresseBatiment, faculteBatiment, campusBatiment, universite, id )
    batiment.DeleteBatiment()

    return jsonify(result={"status": 200})