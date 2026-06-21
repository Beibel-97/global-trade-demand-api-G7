from pydantic import BaseModel, Field

class DemandForecastCreate(BaseModel):
    customer_segment: str = Field(..., example="Retail")
    product_category: str = Field(..., example="Electronics")
    historical_sales: float = Field(..., example=500)
    inventory_level: float = Field(..., example=1200)
    marketing_spend: float = Field(..., example=3000)
    discount_rate: float = Field(..., example=0.15)
    product_price: float = Field(..., example=49.99)
    festival_season: int = Field(..., example=1)
    currency_exchange_rate: float = Field(..., example=3.85)
    tariff_rate: float = Field(..., example=0.08)

class DemandForecastPredictionResponse(BaseModel):
    message: str
    predicted_demand: float

class DemandForecastResponse(BaseModel):
    id: int = Field(..., example=1)
    customer_segment: str = Field(..., example="Retail")
    product_category: str = Field(..., example="Electronics")
    historical_sales: float = Field(..., example=500)
    inventory_level: float = Field(..., example=1200)
    marketing_spend: float = Field(..., example=3000)
    discount_rate: float = Field(..., example=0.15)
    product_price: float = Field(..., example=49.99)
    festival_season: int = Field(..., example=1)
    currency_exchange_rate: float = Field(..., example=3.85)
    tariff_rate: float = Field(..., example=0.08)
    predicted_demand: float = Field(..., example=171.75)