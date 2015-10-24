__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
from pymongo import MongoClient
from MongoDB import Connect

class Horaire:

    def __init__(self, db, date = "0", idSalle = "0", idPresentation = "0", heureDebut = "0", id = "0"):

        self.collection = db.Horaire    # collection Batiment dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.date = date
        self.idSalle = idSalle
        self.idPresentation = idPresentation
        self.heureDebut = heureDebut

    def InsertHoraire(self):
        item = {"_id" : self.id, "date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut }
        #print item
        item_id = self.collection.insert_one(item).inserted_id
        #print item_id
        return item_id


    def ReturnHoraire(self):
        result = []
        for data in self.collection.find():
            result.append(data)
        return result

    def ReturnHoraireid(self, id):
        result = []
        for data in self.collection.find({"_id": id }):
            result.append(data)
        return result

    def UpdateHoraire(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut  })
        return

    def DeleteHoraire(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return




