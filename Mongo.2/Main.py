import Util.Session
import Util.MongoInfo
import pymongo
import DBOperations.Inserts
import DBOperations.Finds
import DBOperations.Updates
import DBOperations.Deletes
import Util.Logging

mongoClient = Util.Session.getMongoClient(Util.Session.getMongoClientURI())
collection = mongoClient["userdata"]["allusers"]

#userData = DBOperations.Finds.FindUserData("user5", collection)
#fieldData = DBOperations.Finds.FindDataField("user5", collection, "data.days.winter.snow")
#DBOperations.Updates.UpdateFieldWithValue(collection, "user5", "data.days.winter.snow", False)
DBOperations.Updates.UpdateFieldName(collection, "user5", "data.days.winter.snow", "data.days.winter.test")

Util.Session.endMongoSession(mongoClient)


