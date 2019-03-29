import pymongo
from bson.json_util import dumps


dburi = "mongodb+srv://root:root@meu-food-truck-db-kspfc.mongodb.net/test?retryWrites=true"
dbcollectionname = "messages"
	
def saveCadastro(item):
	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]
	itemid = dbcollection.insert_one(item).inserted_id
	return str(itemid)


def listCadastro():	
	client = pymongo.MongoClient(dburi)
	db = client.test	
	dbcollection = db[dbcollectionname]	
	cursor = dbcollection.find().sort("timestamp", -1).limit(10) 
	return dumps(cursor)