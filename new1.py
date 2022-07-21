import pymongo

client = pymongo.MongoClient("mongodb+srv://vnasyj:1234@cluster0.9c089qo.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d= {
    "name":"vikash",
    "surname":"Gupta",
    "email":"vnasyj@gmail.com"

}
db1=client['mongotest']
coll= db1['test']
coll.insert_one(d)