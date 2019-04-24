import pymongo

# setup export variables

basePath = './data/'
dbName = 'flaviobolsonaro-15550611312027597'  # filename without the extension
txtFilePath = ''.join([basePath, dbName, '.txt'])

# setup the mongo client

mongoClient = pymongo.MongoClient()
database = mongoClient[dbName]
collection = database['tweets']

# query all tweets from the specified db/collection asking only for their 'tweet' field

documents = collection.find({}, {'tweet': 1, '_id': 0})

# writes all tweets to a txt file as required by birdy

with open(txtFilePath, 'w', encoding='utf-8') as txtFile:
    for item in documents:
        txtFile.write(''.join([item['tweet'], '\n']))
