import joblib
import numpy as np

# Load the best model
model = joblib.load('./model/model.pkl')

# Load the scalers
scaler_X = joblib.load('./model/scaler_X.pkl')
scaler_y = joblib.load('./model/scaler_y.pkl')
print("Model and scalers loaded successfully!")

new_order_features = [
    1.0,    # Customer_Segment_Retail
    0.0,    # Customer_Segment_Wholesale
    0.0,    # Product_Category_Beauty
    1.0,    # Product_Category_Electronics
    0.0,    # Product_Category_Fashion
    0.0,    # Product_Category_Home
    0.0,    # Product_Category_Sports
    500,    # Historical_Sales
    1200,   # Inventory_Level
    3000,   # Marketing_Spend
    0.15,   # Discount_Rate
    49.99,  # Product_Price
    1,      # Festival_Season
    3.85,   # Currency_Exchange_Rate
    0.08    # Tariff_Rate
]

# Convert to numpy array and reshape for the scaler
new_order_data = np.array(new_order_features).reshape(1, -1)

# Scale the new data using the pre-fitted scaler_X
new_order_scaled = scaler_X.transform(new_order_data)

# Make a prediction with the loaded model
predicted_demand_scaled = model.predict(new_order_scaled)

# Inverse transform the predicted demand to the original scale
predicted_demand = scaler_y.inverse_transform(predicted_demand_scaled.reshape(-1, 1))

print(f"Predicted demand for the next period: {predicted_demand[0][0]:,.2f} units")