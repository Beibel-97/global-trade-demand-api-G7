from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import DemandForecast
from ml_model import predict_demand

from schemas import (
    DemandForecastCreate,
    DemandForecastPredictionResponse,
    DemandForecastResponse
)

router = APIRouter(
    prefix="/demand",
    tags=["demand"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/predict", response_model=DemandForecastPredictionResponse)
def demand_prediction(data: DemandForecastCreate):
    demand = predict_demand(
        data.customer_segment,
        data.product_category,
        data.historical_sales,
        data.inventory_level,
        data.marketing_spend,
        data.discount_rate,
        data.product_price,
        data.festival_season,
        data.currency_exchange_rate,
        data.tariff_rate
    )

    return {
        "message": "demanda predicha",
        "predicted_demand": demand
    }

@router.post("/", response_model=DemandForecastResponse)
def create(data: DemandForecastCreate, db: Session = Depends(get_db)):
    demand = predict_demand(
        data.customer_segment,
        data.product_category,
        data.historical_sales,
        data.inventory_level,
        data.marketing_spend,
        data.discount_rate,
        data.product_price,
        data.festival_season,
        data.currency_exchange_rate,
        data.tariff_rate
    )

    new_data = DemandForecast(
        customer_segment = data.customer_segment,
        product_category = data.product_category,
        historical_sales = data.historical_sales,
        inventory_level = data.inventory_level,
        marketing_spend = data.marketing_spend,
        discount_rate = data.discount_rate,
        product_price = data.product_price,
        festival_season = data.festival_season,
        currency_exchange_rate = data.currency_exchange_rate,
        tariff_rate = data.tariff_rate,
        predicted_demand = demand
    )

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data

@router.get("/", response_model=list[DemandForecastResponse])
def get_all(db: Session = Depends(get_db)):
    return db.query(DemandForecast).all()

@router.get("/{id}", response_model=DemandForecastResponse)
def get_by_id(id: int, db: Session = Depends(get_db)):
    record = db.query(DemandForecast).filter(DemandForecast.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return record

@router.put("/{id}", response_model=DemandForecastResponse)
def update(
    id: int,
    data: DemandForecastCreate,
    db: Session = Depends(get_db)
):
    record = db.query(DemandForecast).filter(DemandForecast.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    demand = predict_demand(
        data.customer_segment,
        data.product_category,
        data.historical_sales,
        data.inventory_level,
        data.marketing_spend,
        data.discount_rate,
        data.product_price,
        data.festival_season,
        data.currency_exchange_rate,
        data.tariff_rate
    )

    record.customer_segment = data.customer_segment
    record.product_category = data.product_category
    record.historical_sales = data.historical_sales
    record.inventory_level = data.inventory_level
    record.marketing_spend = data.marketing_spend
    record.discount_rate = data.discount_rate
    record.product_price = data.product_price
    record.festival_season = data.festival_season
    record.currency_exchange_rate = data.currency_exchange_rate
    record.tariff_rate = data.tariff_rate
    record.predicted_demand = demand

    db.commit()
    db.refresh(record)

    return record

@router.delete("/{id}")
def delete(id: int, db: Session = Depends(get_db)):
    record = db.query(DemandForecast).filter(DemandForecast.id == id).first()

    if not record:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    db.delete(record)
    db.commit()

    return {"message": "Registro eliminado correctamente"}