__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
from pymongo import MongoClient
from MongoDB import Connect

class Batiment:

    def __init__(self, db, nomBatiment = "0", adresseBatiment = "0", faculteBatiment="0", CampusBatiment = "0", id = "0"):

        self.collection = db.Batiment    # collection Batiment dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.nomBatiment = nomBatiment
        self.adresseBatiment = adresseBatiment
        self.faculteBatiment = faculteBatiment
        self.CampusBatiment = CampusBatiment

    def InsertBatiment(self):
        item = {"_id" : self.id, "nomBatiment" : self.nomBatiment ,"adresseBatiment" : self.adresseBatiment, "faculteBatiment" : self.faculteBatiment, "CampusBatiment" : self.CampusBatiment }
        print item
        item_id = self.collection.insert_one(item).inserted_id
        print item_id
        return item_id


    def ReturnBatiment(self):
        result = []
        for data in self.collection.find():
            result.append(data)
        return result

    def ReturnBatimentid(self, id):
        result = []
        for data in self.collection.find({"_id": id }):
            result.append(data)
        return result

    def UpdateBatiment(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"nomBatiment" : self.nomBatiment ,"adresseBatiment" : self.adresseBatiment, "faculteBatiment" : self.faculteBatiment, "CampusBatiment" : self.CampusBatiment })
        return

    def DeleteBatiment(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return



