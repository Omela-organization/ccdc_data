from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from datetime import datetime
from worker.fetch_ccdc import TypeFetch

from bson import ObjectId
import motor.motor_asyncio
import numpy as np
from dotenv import dotenv_values

config = dotenv_values(".env") 

client = motor.motor_asyncio.AsyncIOMotorClient(config['MONGO_CONNECT_STRING'])
db = client.ccdc

MAX_THREAD=20

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")





class QueryModel(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    type: str = None
    points: list[list[float]] = None
    createdAt: datetime = datetime.now()

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "type": "NDVI",
                "xStart": "44.63926321849154",
                "yStart": "38.46138012991604",
                "yEnd": "38.56138012991604",
                "xEnd": "44.73926321849154",
                "delta": "0.00001",
            }
        }




async def add_all_types(decart_mul):
    types = list(TypeFetch)[6::]
    for type in types:
        result = []
        save_data = []
        for i in decart_mul:
            if len(save_data) < MAX_THREAD:
                save_data.append(i)
            else:
                save_data.append(i)
                result_item = QueryModel()
                result_item.points = save_data
                result_item.type = type
                result.append(result_item)
                save_data = []
        if len(save_data) > 0:
            result_item = QueryModel()
            result_item.points = save_data
            result_item.type = type
            result.append(result_item)

        result = jsonable_encoder(result)
        await db["query"].insert_many(result)

