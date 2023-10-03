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
from typesBody.Blue import  getBodyBlue
from typesBody.EVI import  getBodyEVI
from typesBody.EVI2 import  getBodyEVI2
from typesBody.Green import  getBodyGreen
from typesBody.GV import  getBodyGV
from typesBody.NBR import  getBodyNBR
from typesBody.NDFI import getBodyNDFI
from typesBody.NIR import getBodyNIR
from typesBody.Red import getBodyRED
from typesBody.Shade import getBodyShade
from typesBody.Soil import  getBodySoil
from typesBody.SWIR2 import  getBodySWIR2



class TypeFetch(StrEnum):
    Greenness = auto()
    Brightness = auto()
    Wetness = auto()
    NDVI = auto()
    NPV = auto()
    SWIR1 = auto()
    Blue = auto()
    Green = auto()
    Red = auto()
    NIR = auto()
    SWIR2 = auto()
    NBR = auto()
    EVI = auto()
    EVI2 = auto()
    NDFI = auto()
    GV = auto()
    Shade = auto()
    Soil = auto()


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
    elif typeFetch == TypeFetch.Blue:
        body = getBodyBlue(x, y)
    elif typeFetch == TypeFetch.EVI:
        body = getBodyEVI(x, y)
    elif typeFetch == TypeFetch.EVI2:
        body = getBodyEVI2(x, y)
    elif typeFetch == TypeFetch.Green:
        body = getBodyGreen(x, y)
    elif typeFetch == TypeFetch.GV:
        body = getBodyGV(x, y)
    elif typeFetch == TypeFetch.NBR:
        body = getBodyNBR(x, y)
    elif typeFetch == TypeFetch.NDFI:
        body = getBodyNDFI(x, y)
    elif typeFetch == TypeFetch.NIR:
        body = getBodyNIR(x, y)
    elif typeFetch == TypeFetch.Red:
        body = getBodyRED(x, y)
    elif typeFetch == TypeFetch.Shade:
        body = getBodyShade(x, y)
    elif typeFetch == TypeFetch.Soil:
        body = getBodySoil(x, y)
    elif typeFetch == TypeFetch.SWIR2:
        body = getBodySWIR2(x, y)
    else:
        raise Exception("Bad type")
    headers = {"authorization": "Bearer " + authToken}

    async with session.post(CCDC_API_URL, data=body, headers=headers) as resp:
        data = await resp.json()
        data = data["result"]
        return parseData(data, str(typeFetch), x, y)


async def getArrayOfData(array, typeFetch: TypeFetch):

    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(len(array)):
            authToken = getAuth()
            tasks.append(
                asyncio.ensure_future(
                    getData(array[i][0], array[i][1], authToken, session, typeFetch)
                )
            )

        original_pokemon = await asyncio.gather(*tasks)

    return original_pokemon
