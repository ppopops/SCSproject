# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from flask import Blueprint
from flask import Flask
from pymongo import MongoClient
from MongoDB import Connect
from Salle.Salle import Salle
from Presentation.Presentation import Presentation
from Cedule import *

db= Connect()


cedule_app = Blueprint('cedule_app', __name__)


@cedule_app.route('/Cedule')
def index():
    return "Cedule"

@cedule_app.route('/SCSproject/api/setcedule', methods=['POST'])
def create_cedule():
    content = request.get_json(force = True)
    print content

    ceduleTemp = content.get("cedule")
    cedule= ceduleTemp[0]
    date =  cedule.get ("date","")
    idSalle =  cedule.get ("idSalle","")
    idPresentation =  cedule.get ("idPresentation","")
    heureDebut =  cedule.get ("heureDebut","")
    minuteDebut =  cedule.get ("minuteDebut","")
    heureFin =  cedule.get ("heureFin","")
    minuteFin =  cedule.get ("minuteFin","")
    statut =  cedule.get ("statut","")
    id = "0"   #contructor will set id
    cedule = Cedule( db, date ,idSalle, idPresentation, heureDebut,minuteDebut, heureFin, minuteFin,statut, id )
    itemId = cedule.InsertCedule(db)
    #print itemId

    return jsonify(cedule={"_id": itemId})
    #return jsonify(result={"status": 200})


@cedule_app.route('/SCSproject/api/getcedule', methods=['GET'])
def get_cedule():
    result = Cedule.GetAllCedule(db)

    i=0
    for s in result:
        #salle = Salle(db)
        #idSalle = salle.ReturnSalleid(s["idSalle"])
        idSalle = Salle.GetIdSalle(db, s["idSalle"])
        result[i]["idSalle"] = idSalle

        #presentation = Presentation(db)
        #idPresentation = presentation.ReturnPresentationid(s["idPresentation"])
        idPresentation = Presentation.GetIdPresentation(db, s["idPresentation"])
        result[i]["idPresentation"] = idPresentation
        i = i +1


    return jsonify ({'cedule' : result})


@cedule_app.route('/SCSproject/api/getceduleid/<string:cedule_id>', methods=['GET'])
def get_cedule_id(cedule_id):
    return jsonify({'cedule': Cedule.GetIdcedule(db, cedule_id)})

@cedule_app.route('/SCSproject/api/updatecedule', methods=['POST'])
def update_cedule():
    print 'abd'
    content = request.get_json(force = True)
    print content

    ceduleTemp = content.get("cedule")
    cedule= ceduleTemp[0]
    date =  cedule.get ("date","")
    idSalle =  cedule.get ("idSalle","")
    statut = cedule.get("statut")
    id = cedule.get ("_id")
    cedule = Cedule( db, date ,idSalle, statut, id )
    cedule.UpdateCedule()

    return jsonify(result={"status": 200})

@cedule_app.route('/SCSproject/api/deletecedule', methods=['POST'])
def delete_cedule():
    content = request.get_json(force = True)
    print content

    ceduleTemp = content.get("cedule")
    cedule= ceduleTemp[0]
    date =  cedule.get ("date","")
    idSalle =  cedule.get ("idSalle","")
    idPresentation =  cedule.get ("idPresentation","")
    heureDebut =  cedule.get ("heureDebut","")
    minuteDebut =  cedule.get ("minuteDebut","")
    statut = cedule.get("statut")
    id = cedule.get ("_id")
    cedule = Cedule( db, date ,idSalle, idPresentation, heureDebut, minuteDebut, statut, id )
    cedule.DeleteCedule()

    return jsonify(result={"status": 200})


@cedule_app.route('/SCSproject/api/testcedule', methods=['POST'])
def test_cedule():
    result = Cedule.FindCeduleNonDisponible(db,20151225,"693ea319-a992-43cb-9bc6-48033f33ed2d")
    print result
    return jsonify(result={"status": "ok"})

@cedule_app.route('/SCSproject/api/testcedule2', methods=['POST'])
def test_cedule2():
    result = Cedule.FindCeduleDisponible(db,20151225,"693ea319-a992-43cb-9bc6-48033f33ed2d")
    print result
    return jsonify(result={"status": "ok"})