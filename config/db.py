from time import monotonic
from pymongo import MongoClient

# conn = MongoClient()
conn = MongoClient("mongodb+srv://vtu15933:gaCLmpYxNtdNFE0Z@cluster0.x1cscsv.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS = 3000)
