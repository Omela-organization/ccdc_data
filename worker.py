import random
import motor
import schedule
import time
import asyncio
from worker.query_processing import processQuery
from datetime import datetime
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
    
myMutex = False

loop = asyncio.get_event_loop()


async def main():
    global myMutex
    if myMutex:
        return
    # res =  await getArrayOfData([[23 + random.random(), 23 + random.random()] for i in range(2)])
    # res = await getArrayOfData([[ 38.418249300187135,44.78450006793644],[ 35.418249300187135,44.78450006793644], [ 38.418249300187135,44.78460006793644], [ 38.418259300187135,44.78460006793644],[31.39072948258994,26.72065099958095]], TypeFetch.Brightness)
    # print(res)
    
    try:
        await processQuery()
    except Exception as e:
        print('_____')
        print(e)
        print('_____')
        time.sleep(random.randint(5, 37))
        myMutex = False
    myMutex = False


def job():
    loop.run_until_complete(main())
    now = datetime.now()
    print("end work", now)


schedule.every(1).second.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
