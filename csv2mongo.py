import ujson
import pandas
import pymongo

# setup import variables

basePath = './data/'
dbName = 'flaviobolsonaro-15550611312027597'  # filename without the extension
csvFilePath = ''.join([basePath, dbName, '.csv'])
jsonFilePath = ''.join([basePath, dbName, '.json'])

# setup the mongo client

mongoClient = pymongo.MongoClient()
database = mongoClient[dbName]
collection = database['tweets']

# load data from csv

dataFrame = pandas.read_csv(csvFilePath, encoding='UTF-8')

with open(jsonFilePath, 'w', encoding='utf-8') as jsonFile:  # ensures that our tweets are stored in UTF-8
    dataFrame.to_json(jsonFile, orient='records', lines=True, force_ascii=False)

with open(jsonFilePath, 'r') as data:
    tweets = data.readlines()

# insert data into database

for tweet in tweets:
    collection.insert_one(ujson.loads(tweet))

# close mongo client connection

mongoClient.close()
