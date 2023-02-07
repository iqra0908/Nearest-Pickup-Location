from fastapi import FastAPI
import uvicorn
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

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000)
