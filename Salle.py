import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
from pymongo import MongoClient
from MongoDB import Connect

class Salle:

    def __init__(self, db, numeroSalle = "0", etageSalle = "0", capaciteSalle="0", equipmentSalle = "0", idBatiment = "0",id = "0"):

        self.collection = db.Salle    # collection Salle dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.capaciteSalle = capaciteSalle
        self.equipementSalle = equipmentSalle
        self.etageSalle = etageSalle
        self.numeroSalle = numeroSalle
        self.idBatiment = idBatiment

    def InsertSalle(self):
        item = {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        print item
        item_id = self.collection.insert_one(item).inserted_id
        return item_id

    #retourber toutes les salles
    def ReturnSalle(self):
        result = []
        for data in self.collection.find():
            result.append(data)
        return result

    def ReturnSalleid(self, id):
        result = []
        for data in self.collection.find({"_id": id }):
            result.append(data)
        return result

    def UpdateSalle(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment })
        return

    def DeleteSalle(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return


    '''

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
'''