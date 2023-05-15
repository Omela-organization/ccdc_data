from fastapi import FastAPI, Body, HTTPException, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from worker.fetch_ccdc import getArrayOfData,TypeFetch

from bson import ObjectId
import motor.motor_asyncio
import numpy as np
from dotenv import dotenv_values

config = dotenv_values(".env") 

app = FastAPI()
client = motor.motor_asyncio.AsyncIOMotorClient(config['MONGO_CONNECT_STRING'])
db = client.ccdc

MAX_THREAD=30

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




class QueryModelRequest(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    type: str = Field(...)
    xStart: float = Field(...)
    yStart: float = Field(...)
    yEnd: float = Field(...)
    xEnd: float = Field(...)
    delta: float = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "type": "Jane Doe",
                "xStart": "44.63926321849154",
                "yStart": "38.46138012991604",
                "yEnd": "38.56138012991604",
                "xEnd": "44.73926321849154",
                "delta": "0.00001",
            }
        }

class QueryModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
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




@app.post("/create-query", response_description="Add new query", response_model=QueryModel)
async def create_query(query: QueryModelRequest = Body(...)):
    xPoints = []
    yPoints = []
    try:
        TypeFetch(query.type)
    except:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,content=query.type+'is bad type')
    xCurrent = query.xStart
    yCurrent = query.yStart
    while xCurrent <= query.xEnd:
        xPoints.append(xCurrent)
        xCurrent += query.delta
    while yCurrent <= query.yEnd:
        yPoints.append(yCurrent)
        yCurrent += query.delta
    decart_mul =  np.transpose([np.tile(xPoints, len(yPoints)), np.repeat(yPoints, len(xPoints))])
    save_data = []
    result = []
    for i in decart_mul:
        if len(save_data) < MAX_THREAD:
            save_data.append(i.tolist())
        else:
            save_data.append(i.tolist())
            result_item = QueryModel()
            result_item.points = save_data
            result_item.type = query.type
            result.append(result_item)
            save_data = []
    if len(save_data) > 0:
        result_item = QueryModel()
        result_item.points = save_data
        result_item.type = query.type
        result.append(result_item)

    result = jsonable_encoder(result)
    saved_query = await db["query"].insert_many(result)
    return JSONResponse(status_code=status.HTTP_201_CREATED,content=saved_query.inserted_ids)

# @app.get(
#     "/", response_description="List all students", response_model=List[StudentModel]
# )
# async def list_students():
#     students = await db["students"].find().to_list(1000)
#     return students


# @app.get(
#     "/{id}", response_description="Get a single student", response_model=StudentModel
# )
# async def show_student(id: str):
#     if (student := await db["students"].find_one({"_id": id})) is not None:
#         return student

#     raise HTTPException(status_code=404, detail=f"Student {id} not found")





# @app.delete("/{id}", response_description="Delete a student")
# async def delete_student(id: str):
#     delete_result = await db["students"].delete_one({"_id": id})

#     if delete_result.deleted_count == 1:
#         return Response(status_code=status.HTTP_204_NO_CONTENT)

#     raise HTTPException(status_code=404, detail=f"Student {id} not found")
