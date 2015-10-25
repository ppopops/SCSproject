# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from flask import Blueprint
from flask import Flask
from pymongo import MongoClient
from MongoDB import Connect
from Presentation import *

db= Connect()


presentation_app = Blueprint('presentation_app', __name__)


@presentation_app.route('/presentation')
def index():
    return "Presentation"

@presentation_app.route('/SCSproject/api/setpresentation', methods=['POST'])
def create_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = "0"   #contructor will set id
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree ,presentateur, id )
    itemId = presentation.InsertPresentation()
    #print itemId

    return jsonify(presentation={"_id": itemId})
    #return jsonify(result={"status": 200})

@presentation_app.route('/SCSproject/api/getpresentation', methods=['GET'])
def get_presentation():
    #presentation = Presentation(db)
    return jsonify({'presentation': Presentation.GetAllPresentation(db)})

@presentation_app.route('/SCSproject/api/getpresentationid/<string:presentation_id>', methods=['GET'])
def get_presentation_id(presentation_id):
    #presentation = Presentation(db)
    return jsonify({'salle': Presentation.GetIdPresentation(db,presentation_id)})

@presentation_app.route('/SCSproject/api/updatepresentation', methods=['POST'])
def update_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = presentation.get ("_id")
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree , presentateur, id )
    presentation.UpdatePresentation()

    return jsonify(result={"status": 200})

@presentation_app.route('/SCSproject/api/deletepresentation', methods=['POST'])
def delete_presentation():
    content = request.get_json(force = True)
    print content

    presentationTemp = content.get("presentation")
    presentation= presentationTemp[0]
    titre =  presentation.get ("titre","")
    nombreParticipants =  presentation.get ("nombreParticipants","")
    equipement =  presentation.get ("equipement","")
    duree =  presentation.get ("duree","")
    presentateur =  presentation.get ("presentateur","")
    id = presentation.get ("_id")
    presentation = Presentation( db, titre ,nombreParticipants, equipement, duree , presentateur, id )
    presentation.DeletePresentation()

    return jsonify(result={"status": 200})

