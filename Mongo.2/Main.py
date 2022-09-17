import Util.Session
import Util.MongoInfo
import pymongo
import DBOperations.Inserts
import DBOperations.Retrievals
import Util.Logging

mongoClient = Util.Session.getMongoClient(Util.Session.getMongoClientURI())
collection = mongoClient["userdata"]["allusers"]

userData = DBOperations.Retrievals.RetrieveUserData("user5", collection)


Util.Session.endMongoSession(mongoClient)


