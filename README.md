🌐 Global Trade Demand Forecast API

API REST de Machine Learning para predecir la demanda futura de productos en cadenas de suministro de e-commerce transfronterizo.


📌 Descripción

Este proyecto implementa un pipeline completo de Data Science — desde el análisis exploratorio de datos (EDA) hasta el despliegue de un modelo de ML vía API REST. Dado un conjunto de variables operativas y de comercio internacional, la API predice la demanda esperada para el siguiente periodo.

Variable objetivo: Demand_Next_Period (unidades)

Dataset: Cross-Border E-Commerce Supply Chain Dataset — Kaggle


🗂️ Estructura del proyecto

global-trade-demand-api-G7/
├── model/                  # Archivos del modelo entrenado (.pkl)
│   ├── model.pkl
│   ├── scaler_X.pkl
│   └── scaler_y.pkl
├── routers/
│   ├── __init__.py
│   └── demandforecast.py   # Endpoints de la API
├── docker/
│   └── postgres/
│       └── init.sql        # Script de inicialización de la base de datos
├── main.py                 # Punto de entrada de la API
├── database.py             # Configuración de SQLAlchemy
├── models.py               # Modelo ORM de la tabla demand_forecasts
├── schemas.py              # Esquemas Pydantic (validación de datos)
├── ml_model.py             # Lógica de predicción con el modelo entrenado
├── ml-test.py              # Script de prueba del modelo en local
├── docker-compose.yml      # Configuración de Docker (PostgreSQL)
├── requirements.txt        # Dependencias del proyecto
└── .env                    # Variables de entorno (no incluido en el repo)


🧠 Modelo de Machine Learning

El modelo fue entrenado y evaluado en Google Colab usando los siguientes notebooks:

NotebookDescripción1_EDA_DATASET_E-COMMERCE_SUPPLY_CHAIN.ipynbAnálisis exploratorio, limpieza de datos y tratamiento de outliers2_ML_E-COMMERCE_SUPPLY_CHAIN.ipynbEntrenamiento y comparación de 6 modelos de regresión

Modelos evaluados:


Linear Regression
Lasso
Ridge
KNN Regressor
SVR
Random Forest Regressor ← mejor modelo (seleccionado por R²)


Variables de entrada del modelo:

VariableTipoDescripcióncustomer_segmentstringSegmento del cliente (Retail / Wholesale)product_categorystringCategoría del producto (Beauty, Electronics, Fashion, Home, Sports)historical_salesfloatVentas históricasinventory_levelfloatNivel de inventario actualmarketing_spendfloatGasto en marketingdiscount_ratefloatTasa de descuento aplicadaproduct_pricefloatPrecio del productofestival_seasonintTemporada festiva (0 = No, 1 = Sí)currency_exchange_ratefloatTipo de cambio de la monedatariff_ratefloatTasa arancelaria


🛠️ Tecnologías utilizadas


FastAPI — Framework para la API REST
SQLAlchemy — ORM para la base de datos
PostgreSQL — Base de datos relacional
Docker — Contenedor para la base de datos
scikit-learn — Entrenamiento del modelo de ML
joblib — Serialización del modelo
python-decouple — Gestión de variables de entorno



⚙️ Instalación y configuración

1. Clonar el repositorio

bashgit clone https://github.com/Beibel-97/global-trade-demand-api-G7.git
cd global-trade-demand-api-G7

2. Crear y activar el entorno virtual

bashpython -m venv venv
source venv/Scripts/activate  # Windows

3. Instalar dependencias

bashpip install -r requirements.txt

4. Configurar variables de entorno

Crear un archivo .env en la raíz del proyecto:

envPOSTGRES_DB=demandforecast
POSTGRES_USER=demandforecast
POSTGRES_PASSWORD=demandforecast
DATABASE_URL=postgresql://demandforecast:demandforecast@localhost:5442/demandforecast

5. Levantar la base de datos con Docker

bashdocker compose up -d

6. Correr la API

bashuvicorn main:app --reload

7. Abrir la documentación interactiva

http://127.0.0.1:8000/docs


📡 Endpoints disponibles

MétodoEndpointDescripciónGET/Bienvenida a la APIPOST/demand/predictPredice la demanda sin guardar en BDPOST/demand/Predice y guarda el registro en BDGET/demand/Obtiene todos los registrosGET/demand/{id}Obtiene un registro por IDPUT/demand/{id}Actualiza un registroDELETE/demand/{id}Elimina un registro


🧪 Ejemplo de uso

Request:

jsonPOST /demand/predict
{
  "customer_segment": "Retail",
  "product_category": "Electronics",
  "historical_sales": 500,
  "inventory_level": 1200,
  "marketing_spend": 3000,
  "discount_rate": 0.15,
  "product_price": 49.99,
  "festival_season": 1,
  "currency_exchange_rate": 3.85,
  "tariff_rate": 0.08
}

Response:

json{
  "message": "demanda predicha",
  "predicted_demand": 171.75
}


👤 Autor

Beibel — Data Science Student @ TECSUP

Combinando Negocios Internacionales y Data Science para soluciones de comercio global.

GitHub: @Beibel-97