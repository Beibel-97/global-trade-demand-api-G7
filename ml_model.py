import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')


def predict_demand(customer_segment: str,
                    product_category: str,
                    historical_sales: float,
                    inventory_level: float,
                    marketing_spend: float,
                    discount_rate: float,
                    product_price: float,
                    festival_season: int,
                    currency_exchange_rate: float,
                    tariff_rate: float) -> float:

    # One-hot encoding manual para Customer_Segment
    customer_segment_retail = 1.0 if customer_segment == "Retail" else 0.0
    customer_segment_wholesale = 1.0 if customer_segment == "Wholesale" else 0.0

    # One-hot encoding manual para Product_Category
    product_category_beauty = 1.0 if product_category == "Beauty" else 0.0
    product_category_electronics = 1.0 if product_category == "Electronics" else 0.0
    product_category_fashion = 1.0 if product_category == "Fashion" else 0.0
    product_category_home = 1.0 if product_category == "Home" else 0.0
    product_category_sports = 1.0 if product_category == "Sports" else 0.0

    # El orden debe coincidir EXACTO con el de 'cols' usado al entrenar el modelo
    new_order_features = [
        customer_segment_retail,
        customer_segment_wholesale,
        product_category_beauty,
        product_category_electronics,
        product_category_fashion,
        product_category_home,
        product_category_sports,
        historical_sales,
        inventory_level,
        marketing_spend,
        discount_rate,
        product_price,
        festival_season,
        currency_exchange_rate,
        tariff_rate
    ]

    new_order_data = np.array(new_order_features).reshape(1, -1)
    new_order_scaled = scaler_X.transform(new_order_data)
    predicted_demand_scaled = model.predict(new_order_scaled)
    predicted_demand = scaler_y.inverse_transform(predicted_demand_scaled.reshape(-1, 1))
    demand = round(float(predicted_demand[0][0]), 2)
    return demand