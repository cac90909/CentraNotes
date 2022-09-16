import Util.Session
import Util.MongoInfo
import pymongo
import DBOperations.Inserts

mongoClient = Util.Session.getMongoClient(Util.Session.getMongoClientURI())
collection = mongoClient["userdata"]["allusers"]

DBOperations.Inserts.InsertNextUser(collection)

Util.Session.endMongoSession(mongoClient)


