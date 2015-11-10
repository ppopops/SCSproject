__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
#from Presentation import *
from Presentation import Presentation
import datetime

class Cedule:

    def __init__(self, db, date = 0, idSalle = "0", idPresentation = "0", heureDebut = 0, minuteDebut = 0, heureFin = 0, minuteFin = 0,statut = "0", id = "0"):

        self.collection = db.Cedule    # collection Batiment dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.date = date
        self.idSalle = idSalle
        self.idPresentation = idPresentation
        self.heureDebut = heureDebut
        self.minuteDebut = minuteDebut
        self.heureFin = heureFin
        self.minuteFin = minuteFin
        self.statut = statut

    def InsertCedule(self, db):
        #item = {"_id" : self.id, "date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut, "heureMinute" : self.heureMinute,"statut" : self.statut }

        #result = Cedule.FindCedule(db,self.date,self.idSalle )

        getCedule = Cedule.FindCedule(db,self.date,self.idSalle )
        #create new document
        if getCedule[0]== '':
            item = {"_id" : self.id, "date" : self.date ,"idSalle" : self.idSalle, "horaire": [ {"idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut, "minuteDebut" : self.minuteDebut, "heureFin" : self.heureFin, "minuteFin" : self.minuteFin}],"statut" : self.statut }
            item_id = self.collection.insert_one(item).inserted_id
            return item_id
        else: #document exist, add new schedule
             self.collection.update(
                { "date": self.date, "idSalle" : self.idSalle },
                { "$push" : {"horaire": {"heureDebut" : self.heureDebut, "minuteDebut": self.minuteDebut, "idPresentation": self.idPresentation, "heureFin": self.heureFin, "minuteFin": self.minuteFin}  }}
             )
             return getCedule[0]['_id']



    #def ReturnHoraire(self):
    #    result = []
    #    for data in self.collection.find():
    #        result.append(data)
    #    return result

    #def ReturnHoraireid(self, id):
    #    result = []
    #    for data in self.collection.find({"_id": id }):
    #        result.append(data)
    #    return result

    @staticmethod
    def GetAllCedule(db):
        result = []
        for data in db.Cedule.find():
            result.append(data)
        return result

    @staticmethod
    def GetIdCedule(db, id):
        result = []
        for data in db.Cedule.find({"_id": id }):
            result.append(data)
        return result

    @staticmethod
    def FindCedule(db, date = 0, idSalle = ""):
        result = []
        for data in db.Cedule.find({"date" : date, "idSalle" : idSalle}):
            result.append(data)
        return result

    @staticmethod
    def FindCeduleNonDisponible(db, date = 0, idSalle = ""):
        result = []
        for data in db.Cedule.find({"date" : date, "idSalle" : idSalle}):
            result.append(data)

        arrayAvailableTime = []

        for s in result[0]['horaire'] :
            tempDebut = datetime.time(s['heureDebut'], s['minuteDebut'])
            tempFin = datetime.time(s['heureFin'], s['minuteFin'])
            arrayAvailableTime.append({tempDebut,tempFin } )
        #result = result[0]['horaire'][0]
        return arrayAvailableTime


    def UpdateCedule(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        #self.collection.update({"_id" : self.id}, {"date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut ,"minuteDebut" : self.minuteDebut, "statut" : self.statut })
        self.collection.update({"_id" : self.id}, {"date" : self.date ,"idSalle" : self.idSalle, "statut" : self.statut })
        return

    def DeleteCedule(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return




