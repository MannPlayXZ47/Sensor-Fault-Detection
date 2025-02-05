from pymongo.mongo_client import MongoClient
import pandas as pd
import json
from urllib.parse import quote_plus

uri = "mongodb+srv://Mann:gKBCZ5SA7uAWVvR@cluster0.kjgwx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

DATABASE_NAME = "project"
COLLECTION_NAME = "sensorfault"

df=pd.read_csv("C:\Users\KIIT\Desktop\Projects\sensor fault detection\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0", axis = 1)

json_record = list(json.loads(df.T.to_json()).values())

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)