__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect

class Salle:

    def __init__(self, db, numero = "0", etage = 0, capacite= 0, equipment = "0", idBatiment = "0", statut = "0", description = "0", id = "0"):

        self.collection = db.Salle    # collection Salle dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.capacite = capacite
        self.equipement = equipment
        self.etage = etage
        self.numero = numero
        self.idBatiment = idBatiment
        self.statut = statut
        self.description = description

    def InsertSalle(self):
        item = {"_id" : self.id, "numero" : self.numero ,"etage" : self.etage, "capacite" : self.capacite, "equipement" : self.equipement, "idBatiment" : self.idBatiment, "statut" : self.statut, "description" : self.description }
        print item
        item_id = self.collection.insert_one(item).inserted_id
        return item_id

    #retourber toutes les salles
    #def ReturnSalle(self):
    #    result = []
    #    for data in self.collection.find():
    #        result.append(data)
    #    return result

    #retourber toutes les salles
    @staticmethod
    def GetAllSalle(db):
        result = []
        for data in db.Salle.find():
            result.append(data)
        return result

    #retourber une salle
    @staticmethod
    def GetIdSalle(db,id):
        result = []
        for data in db.Salle.find({"_id": id }):
            result.append(data)
        return result

    #def ReturnSalleid(self, id):
    #    result = []
    #    for data in self.collection.find({"_id": id }):
    #        result.append(data)
    #    return result

    def UpdateSalle(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"numero" : self.numero ,"etage" : self.etage, "capacite" : self.capacite, "equipement" : self.equipement, "idBatiment" : self.idBatiment, "statut" : self.statut , "description" : self.description })
        return

    def DeleteSalle(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return
    
    def IsSalleAlreadyExist(db,salleNumber,idBatiment):
        if ((db.Salle.find({'numero': universityName}).count() > 0) and (db.Salle.find({'idBatiment': batimentName}).count() > 0)):
            return True

        return False


    '''

#static variable for idSalle
    def static_vars(**kwargs):
        def decorate(func):
            for k in kwargs:
                setattr(func, k, kwargs[k])
            return func
        return decorate

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

    '''




