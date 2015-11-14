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
from Horaire import *

db= Connect()


horaire_app = Blueprint('horaire_app', __name__)


@horaire_app.route('/horaire')
def index():
    return "Horaire"

@horaire_app.route('/SCSproject/api/sethoraire', methods=['POST'])
def create_horaire():
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    minuteDebut =  horaire.get ("minuteDebut","")
    statut =  horaire.get ("statut","")
    id = "0"   #contructor will set id
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut,minuteDebut,statut, id )
    itemId = horaire.InsertHoraire()
    #print itemId

    return jsonify(horaire={"_id": itemId})
    #return jsonify(result={"status": 200})


@horaire_app.route('/SCSproject/api/gethoraire', methods=['GET'])
def get_horaire():
    #horaire = Horaire(db)
    result = Horaire.GetAllHoraire(db)

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

    #test
    #testResult = Horaire.FindHoraire(db, "18/12/2015","")
    #print testResult
    #
    return jsonify ({'horaire' : result})
    #return jsonify({'horaire': horaire.ReturnHoraire()})

@horaire_app.route('/SCSproject/api/gethoraireid/<string:horaire_id>', methods=['GET'])
def get_horaire_id(horaire_id):
    #horaire = Horaire(db)
    return jsonify({'horaire': Horaire.GetIdHoraire(db, horaire_id)})

@horaire_app.route('/SCSproject/api/updatehoraire', methods=['POST'])
def update_horaire():
    print 'abd'
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    minuteDebut =  horaire.get ("minuteDebut","")
    statut = horaire.get("statut")
    id = horaire.get ("_id")
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut, minuteDebut, statut, id )
    horaire.UpdateHoraire()

    return jsonify(result={"status": 200})

@horaire_app.route('/SCSproject/api/deletehoraire', methods=['POST'])
def delete_horaire():
    content = request.get_json(force = True)
    print content

    horaireTemp = content.get("horaire")
    horaire= horaireTemp[0]
    date =  horaire.get ("date","")
    idSalle =  horaire.get ("idSalle","")
    idPresentation =  horaire.get ("idPresentation","")
    heureDebut =  horaire.get ("heureDebut","")
    minuteDebut =  horaire.get ("minuteDebut","")
    statut = horaire.get("statut")
    id = horaire.get ("_id")
    horaire = Horaire( db, date ,idSalle, idPresentation, heureDebut, minuteDebut, statut, id )
    horaire.DeleteHoraire()

    return jsonify(result={"status": 200})


@horaire_app.route('/SCSproject/api/testhoraire', methods=['POST'])
def test_horaire():
    result = Horaire.FindHoraireNonDisponible(db,20151218,"2fb73f84-5e01-4203-8abb-abf24f015678")
    print result
    return jsonify(result={"status": "ok"})

@horaire_app.route('/SCSproject/api/testhoraire2', methods=['POST'])
def test_horaire2():
    result = Horaire.FindHoraireDisponible(db,20151218,"2fb73f84-5e01-4203-8abb-abf24f015678")
    print result
    return jsonify(result={"status": "ok"})