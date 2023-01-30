from fastapi import FastAPI
from Service import Service 

app = FastAPI()
service = Service('directory.csv')

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/nearestStarbucks/")
async def getNearestStarbucks(country_code: str = '', zip_code: str = ''):
    return service.getNearestStarbucks(country_code,zip_code)