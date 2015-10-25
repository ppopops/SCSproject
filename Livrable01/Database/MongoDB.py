__author__ = 'Hong'

from pymongo import MongoClient

def Connect():
    connection = MongoClient("ds057862.mongolab.com",57862)
    handle = connection["mongodbhong"]
    handle.authenticate("admin","root")
    return handle