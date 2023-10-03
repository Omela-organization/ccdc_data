import motor.motor_asyncio
from datetime import datetime
import time

from worker.fetch_ccdc import getArrayOfData, TypeFetch
from fastapi.encoders import jsonable_encoder
from dotenv import dotenv_values
import random

config = dotenv_values(".env") 
config['MONGO_CONNECT_STRING']
uri = "mongodb+srv://<username>:<password>@cluster0.j3qun1f.mongodb.net/?retryWrites=true&w=majority"

client = motor.motor_asyncio.AsyncIOMotorClient(config['MONGO_CONNECT_STRING'])
db = client.ccdc


async def processQuery():
    # some = await db["query"].find_one()
    now = datetime.now()

    print("now =", now)
    cursor = db["query"].find().sort("createdAt", 1)
    for document in await cursor.to_list(length=1):
        print(document["_id"])
        data = await getArrayOfData(document["points"], document["type"])
        saved_query = await db["info"].insert_many(jsonable_encoder(data))
        deleted = await db["query"].find_one_and_delete({"_id": document["_id"]})
        print(saved_query.inserted_ids)
        print(deleted)



    # print(some)
