from pymongo import MongoClient

def mongo_setup(pwd):
    uri = f'mongodb+srv://ahernes:{pwd}@cluster0.oiosk.mongodb.net/?retryWrites=true&w=majority'
    client = MongoClient(uri)

    try:
        client.admin.command('ping')
        print("Mongo connection successful!")
        db = client['role_bot']
        coll = db['servers']
        return db, coll
    except Exception as e:
        print(e)
        

        