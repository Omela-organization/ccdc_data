import asyncio
from enum import auto
import time
from pydantic import BaseModel
import requests
import aiohttp
from strenum import StrEnum
from constant import AUTH_TOKEN_URL, CCDC_API_URL
from typesBody.Brightness import  getBodyBrightness
from typesBody.NDVI import  getBodyNDVI
from typesBody.NPV import  getBodyNPV
from typesBody.SWIR1 import getBodySWIR1
from typesBody.Wetness import  getBodyWetness
from typesBody.Greenness import  getBodyGreenness


class TypeFetch(StrEnum):
    Greenness = auto()
    Brightness = auto()
    Wetness = auto()
    NDVI = auto()
    NPV = auto()
    SWIR1 = auto()


def getAuth() -> str:
    url = AUTH_TOKEN_URL
    response = requests.get(url)
    response.text
    string = response.text

    auth_start = string.find('"authToken":') + len('"authToken":')

    auth_value = string[auth_start:]
    auth_value = auth_value.strip()
    auth_value = auth_value.strip(",")
    auth_value = auth_value.strip('"')
    auth_value = auth_value.split('"')[0]

    return auth_value


class ParsedData(BaseModel):
    count: int = None
    break_points: list[str] = None
    type: str = None
    x: float = None
    y: float = None


def parseData(array, type, x, y):
    count = 0
    break_points = []
    for i in array:
        if i[2] != None and count < 1:
            count = 1
            break_points.append(i[0])
        if i[3] != None and count < 2:
            count = 2
            break_points.append(i[0])
        if i[4] != None and count < 3:
            count = 3
            break_points.append(i[0])
        if i[5] != None and count < 4:
            count = 4
            break_points.append(i[0])
        if i[6] != None and count < 5:
            count = 5
            break_points.append(i[0])
        if i[7] != None and count < 6:
            count = 6
            break_points.append(i[0])
    parsed_data = ParsedData()
    parsed_data.count = count
    parsed_data.break_points = break_points
    parsed_data.type = type
    parsed_data.x = x
    parsed_data.y = y
    return parsed_data


async def getData(x: float, y: float, authToken: str, session, typeFetch: TypeFetch):
    if typeFetch == TypeFetch.Brightness:
        body = getBodyBrightness(x, y)
    elif typeFetch == TypeFetch.NDVI:
        body = getBodyNDVI(x, y)
    elif typeFetch == TypeFetch.NPV:
        body = getBodyNPV(x, y)
    elif typeFetch == TypeFetch.Greenness:
        body = getBodyGreenness(x, y)
    elif typeFetch == TypeFetch.SWIR1:
        body = getBodySWIR1(x, y)
    elif typeFetch == TypeFetch.Wetness:
        body = getBodyWetness(x, y)
    else:
        raise Exception("asdf")

    headers = {"authorization": "Bearer " + authToken}

    async with session.post(CCDC_API_URL, data=body, headers=headers) as resp:
        data = await resp.json()
        data = data["result"]
        return parseData(data, str(typeFetch), x, y)


async def getArrayOfData(array, typeFetch: TypeFetch):
    authToken = getAuth()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(len(array)):
            tasks.append(
                asyncio.ensure_future(
                    getData(array[i][0], array[i][1], authToken, session, typeFetch)
                )
            )

        original_pokemon = await asyncio.gather(*tasks)

    return original_pokemon
