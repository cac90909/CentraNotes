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

#userData = DBOperations.Finds.FindUserData("user55", collection)
#print(len(userData))
#userData = DBOperations.Finds.FindUserData("user5", collection)
#print(len(userData))
#print(userData)
fieldData = DBOperations.Finds.FindDataField("user5", collection, "data.days.summer.haha")
print(fieldData)
fieldData = DBOperations.Finds.FindDataField("user5", collection, "data.days.summer")
print(fieldData)
#DBOperations.Updates.UpdateFieldValue(collection, "user5", "data.days.winter.snow", False)
#DBOperations.Updates.UpdateFieldName(collection, "user5", "data.days.winter.snow", "data.days.winter.test")

#Want to test the bulk update method jsut wrote
#Want to create and test a method for finding in bulk (this will help the logging of above statement)
#Wwant to create af unction to reorder the userids (goes through and make sure it goes 1->2->3->4) as they are currently out of order

Util.Session.endMongoSession(mongoClient)


