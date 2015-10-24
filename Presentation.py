__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
from pymongo import MongoClient
from MongoDB import Connect

class Presentation:

    def __init__(self, db, titre = "0", nombreParticipants = "0", equipement = "0", duree = "0", presentateur = "", id = "0"):

        self.collection = db.Presentation    # collection Batiment dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.titre = titre
        self.nombreParticipants = nombreParticipants
        self.equipement = equipement
        self.duree = duree
        self.presentateur = presentateur

    def InsertPresentation(self):
        item = {"_id" : self.id, "titre" : self.titre ,"nombreParticipants" : self.nombreParticipants, "equipement" : self.equipement, "duree" : self.duree, "presentateur" : self.presentateur }
        #print item
        item_id = self.collection.insert_one(item).inserted_id
        #print item_id
        return item_id


    #def ReturnPresentation(self):
    #    result = []
    #    for data in self.collection.find():
    #        result.append(data)
    #    return result

    #def ReturnPresentationid(self, id):
    #    result = []
    #    for data in self.collection.find({"_id": id }):
    #        result.append(data)
    #    return result

    @staticmethod
    def GetAllPresentation(db):
        result = []
        for data in db.Presentation.find():
            result.append(data)
        return result

    @staticmethod
    def GetIdPresentation(db, id):
        result = []
        for data in db.Presentation.find({"_id": id }):
            result.append(data)
        return result

    def UpdatePresentation(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"titre" : self.titre ,"nombreParticipants" : self.nombreParticipants, "equipement" : self.equipement, "duree" : self.duree , "presentateur" : self.presentateur  })
        return

    def DeletePresentation(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return




