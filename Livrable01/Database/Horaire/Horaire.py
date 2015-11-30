__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect
import os
import datetime
from datetime import timedelta,date,timedelta,time
from Presentation.Presentation import Presentation

class Horaire:

    def __init__(self, db, date = 0, idSalle = "0", idPresentation = "0", heureDebut = 0, heureMinute = 0, statut = "0", id = "0"):

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
        self.heureMinute = heureMinute
        self.statut = statut

    def InsertHoraire(self):
        item = {"_id" : self.id, "date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut, "minuteDebut" : self.heureMinute,"statut" : self.statut }
        #print item
        item_id = self.collection.insert_one(item).inserted_id
        #print item_id
        return item_id


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
    def GetAllHoraire(db):
        result = []
        for data in db.Horaire.find():
            result.append(data)
        return result

    @staticmethod
    def GetIdHoraire(db, id):
        result = []
        for data in db.Horaire.find({"_id": id }):
            result.append(data)
        return result

    @staticmethod
    def FindHoraire(db, date = "", heure = 0, heureMinute = 0):
        result = []
        for data in db.Horaire.find({"date" : date, "heureDebut" : heure, "heureMinute" : heureMinute}):
            result.append(data)
        return result

    def UpdateHoraire(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.update({"_id" : self.id}, {"date" : self.date ,"idSalle" : self.idSalle, "idPresentation" : self.idPresentation, "heureDebut" : self.heureDebut ,"heureMinute" : self.heureMinute, "statut" : self.statut })
        return

    def DeleteHoraire(self):
        #print {"_id" : self.id, "numeroSalle" : self.numeroSalle ,"etageSalle" : self.etageSalle, "capaciteSalle" : self.capaciteSalle, "equipementSalle" : self.equipementSalle, "idBatiment" : self.idBatiment }
        self.collection.remove({"_id" : self.id})
        return


    @staticmethod
    def FindHoraireNonDisponible(db, date = 0, idSalle = ""):
        result = []
        for data in db.Horaire.find({"date" : date, "idSalle" : idSalle}):
            result.append(data)

        arrayNonAvailableTime = []

        for s in result :
            #print s
            tempDebut = datetime.time(s['heureDebut'], s['minuteDebut'])
            presentation = Presentation.GetIdPresentation(db,s['idPresentation'])
            tempFin = (datetime.datetime.combine(datetime.date.today(),tempDebut) + timedelta(hours = presentation[0]['dureeHeure'] ,minutes=presentation[0]['dureeMinute'])).time()
            arrayNonAvailableTime.append([tempDebut,tempFin ] )

        return arrayNonAvailableTime

    @staticmethod
    def FindHoraireDisponible(db, date = 0, idSalle = ""):
        arrayNonAvailableTime = Horaire.FindHoraireNonDisponible(db, date, idSalle)

        arrayAvailableTime = []
        premier = True
        temp=datetime.time(0,0)
        count = len(arrayNonAvailableTime)
        i=1
        for s in arrayNonAvailableTime:
            if premier:
                tempDebut = datetime.time(8,30)
                tempFin = s[0]
                arrayAvailableTime.append([tempDebut,tempFin ])
                temp = s[1]
                premier = False
                i=i+1
            elif count ==i :
                tempDebut = temp
                tempFin = s[0]
                arrayAvailableTime.append([tempDebut,tempFin ])
                tempDebut = s[1]
                tempFin = datetime.time(18,0)
                arrayAvailableTime.append([tempDebut,tempFin ])
            else :
               tempDebut = temp
               tempFin = s[0]
               temp = s[1]
               arrayAvailableTime.append([tempDebut,tempFin ])

        return arrayAvailableTime

    @staticmethod
    def isDisponible(db, date, idSalle, heureDebut, minuteDebut, dureeHeure, dureeMinute):

        tempsDebut = datetime.time(heureDebut, minuteDebut)
        tempsFin = (datetime.datetime.combine(datetime.date.today(),tempsDebut) + timedelta(hours = dureeHeure ,minutes=dureeMinute)).time()

        #temp de debut et de fin de journee
        tempsDebutJournee = datetime.time(8, 30)
        tempsFinJournee = datetime.time(18, 0)

        #Heure de lunch
        tempsDebutLunch = datetime.time(12, 0)
        tempsFinLunch = datetime.time(13, 0)

        horaireNonDisponible=[]
        horaireNonDisponible = Horaire.FindHoraireNonDisponible(db, date,idSalle )
        #horaireNonDisponible = Horaire.FindHoraireNonDisponible(db,20151218,"2fb73f84-5e01-4203-8abb-abf24f015678")

        #Validation debut de journee
        if tempsDebut < tempsDebutJournee:
            print "Trop tot!"
            return False
        #Validation fin de journee
        if tempsFin > tempsFinJournee:
            print "Trop tard!"
            return False

        #Validation Heure de lunch
        if ( (tempsDebut > tempsDebutLunch) and (tempsDebut < tempsFinLunch)):
            print "Debut de la presentation pendant lunch!"
            return False
        if ( (tempsFin > tempsDebutLunch) and (tempsFin < tempsFinLunch)):
            print "Fin de la presentation pendant lunch!"
            return False

        #Validation horaire disponible
        for s in horaireNonDisponible:
            # ajouter 20 min avant et apres presentation
            nonDispoDebut = (datetime.datetime.combine(datetime.date.today(),s[0]) - timedelta(hours = 0 ,minutes=20)).time()
            nonDispoFin = (datetime.datetime.combine(datetime.date.today(),s[1]) + timedelta(hours = 0 ,minutes=20)).time()
            #print nonDispoDebut
            #print nonDispoFin
            if ( (tempsDebut > nonDispoDebut) and (tempsDebut < nonDispoFin) or (tempsFin > nonDispoDebut) and (tempsFin < nonDispoFin) ) :
                print "Plage horaire prise!"
                return False

        #print horaireNonDisponible

        #print tempsDebut
        #print tempsFin
        #print tempsDebutJournee
        #print tempsFinJournee
        return True