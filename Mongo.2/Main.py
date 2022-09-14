import Util.Session


#userMongoSession = Util.Session.startMongoUserSession(userID = "user1", databaseName = "userdata")

mongoDatabaseObject = Util.Session.startMongoDatabase(databaseName = "userdata")