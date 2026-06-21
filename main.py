from fastapi import FastAPI
from database import engine
from models import Base
from routers import demandforecast

app = FastAPI(
    title="Demand Forecast API",
    description="API para predicción de demanda en e-commerce transfronterizo",
    version="1.0.0"
)

app.include_router(demandforecast.router)

@app.get("/")
def index():
    return {
        "title": "DEMAND FORECAST API VERSION 1.0",
        "message": "Bienvenido a mi API"
    }

Base.metadata.create_all(engine)