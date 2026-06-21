from sqlalchemy import Column, Integer, Float, String
from database import Base

class DemandForecast(Base):
    __tablename__ = "demand_forecasts"

    id = Column(Integer, primary_key=True, index=True)
    customer_segment = Column(String, nullable=False)
    product_category = Column(String, nullable=False)
    historical_sales = Column(Float, nullable=False)
    inventory_level = Column(Float, nullable=False)
    marketing_spend = Column(Float, nullable=False)
    discount_rate = Column(Float, nullable=False)
    product_price = Column(Float, nullable=False)
    festival_season = Column(Integer, nullable=False)
    currency_exchange_rate = Column(Float, nullable=False)
    tariff_rate = Column(Float, nullable=False)
    predicted_demand = Column(Float, nullable=True)