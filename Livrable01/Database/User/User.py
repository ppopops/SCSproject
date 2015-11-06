__author__ = 'Hong'
import uuid
from flask import Flask, jsonify, render_template, request, redirect

class User:

    def __init__(self, db, userid = "0", firstName = "0", lastName="0", email = "0", userRole = "0", password = "0", id = "0"):

        self.collection = db.User    # collection User dans MongoDB
        if  id == "0":
            uniqueid= uuid.uuid4()
            self.id = str(uniqueid)
        else :
            self.id = id
        self.userid = userid
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userRole = userRole
        self.password = password

    def InsertUser(self):
        item = {"_id" : self.id, "userid" : self.userid ,"firstName" : self.firstName, "lastName" : self.lastName, "email" : self.email, "userRole" : self.userRole, "password" : self.password }
        item_id = self.collection.insert_one(item).inserted_id
        return item_id

    #retourber tous les user
    @staticmethod
    def GetAllUser(db):
        result = []
        for data in db.User.find():
            result.append(data)
        return result

    #retourner 1 user par userid et password
    @staticmethod
    def GetUser(db,userid,password):
        returnData = ""
        result = []
        for data in db.User.find({"userid": userid, "password" : password }):
            result.append(data)
        return result
        #if result == []:
        #    returnData = "Authentification not accepted"
        #else:
        #    returnData = "Authentification accepted"
        #return returnData

    #retourber 1 user par id
    @staticmethod
    def GetIdUser(db,id):
        result = []
        for data in db.User.find({"_id": id }):
            result.append(data)
        return result

    def UpdateUser(self):
        self.collection.update({"_id" : self.id}, {"userid" : self.userid ,"firstName" : self.firstName, "lastName" : self.lastName, "email" : self.email, "userRole" : self.userRole, "password" : self.password })
        return

    def DeleteUser(self):
        self.collection.remove({"_id" : self.id})
        return





