from fastapi import FastAPI
from Service import Service 
import json

app = FastAPI()
service = Service('directory.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nearestStarbucks/{country_code}/{zip_code}")
async def getNearestStarbucks(country_code: str = '', zip_code: str = ''):
    return json.loads(service.getNearestStarbucks(country_code,zip_code))