# -*- coding: utf-8 -*-
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)
from pymongo import MongoClient
from MongoDB import Connect
from flask import Blueprint
from flask import Flask
from User import User
from flask import jsonify, request


user_app = Blueprint('user_app', __name__)


db= Connect()


@user_app.route('/SCSproject/api/getuser', methods=['GET'])
def get_user():
    result = User.GetAllUser(db)
    return jsonify({'user': result})

@user_app.route('/SCSproject/api/setuser', methods=['POST'])
def create_user():
    content = request.get_json(force = True)
    print content

    useri = content.get("user")
    user= useri[0]
    userid =  user.get ("userid","")
    firstName =  user.get ("firstName","")
    lastName =  user.get ("lastName","")
    email =  user.get ("email","")
    userRole =  user.get ("userRole","")
    password =  user.get ("password","")
    id = "0"   #contructor will set id
    user = User( db, userid ,firstName, lastName, email ,userRole, password, id )
    itemID = user.InsertUser()

    return jsonify(user={"_id": itemID})
    return jsonify(result={"status": 200})


@user_app.route('/SCSproject/api/getuserid/<string:user_id>', methods=['GET'])
def get_user_id(user_id):
    result = User.GetIdUser(db,user_id)
    return jsonify({'user': result})

@user_app.route('/SCSproject/api/getuserid/<string:user_name>/<string:user_password>', methods=['GET'])
def get_user_name(user_name, user_password):
    result = User.GetUser(db,user_name,user_password)
    return jsonify({'user': result})

@user_app.route('/SCSproject/api/updateuser', methods=['POST'])
def update_user():
    content = request.get_json(force = True)
    print content

    useri = content.get("user")
    user= useri[0]
    userid =  user.get ("userid","")
    firstName =  user.get ("firstName","")
    lastName =  user.get ("lastName","")
    email =  user.get ("email","")
    userRole =  user.get ("userRole","")
    password =  user.get ("password","")
    id = user.get ("_id")
    user = User( db, userid ,firstName, lastName, email ,userRole, password, id )
    user.UpdateUser()

    return jsonify(result={"status": 200})

@user_app.route('/SCSproject/api/deleteuser', methods=['POST'])
def delete_user():
    content = request.get_json(force = True)
    print content
    useri = content.get("user")
    user= useri[0]
    userid =  user.get ("userid","")
    firstName =  user.get ("firstName","")
    lastName =  user.get ("lastName","")
    email =  user.get ("email","")
    userRole =  user.get ("userRole","")
    password =  user.get ("password","")
    id = user.get ("_id")
    user = User( db, userid ,firstName, lastName, email ,userRole, password, id )
    user.DeleteUser()

    return jsonify(result={"status": 200})