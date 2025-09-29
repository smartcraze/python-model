from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_utils import (
    predict_outbreak,
    data_fe,
    model_lgbm,
    model_features_order
)
import pandas as pd

app = FastAPI(title="Outbreak Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Outbreak Prediction API is running"}

# single date prediction
@app.get("/predict")
def get_prediction(date: str):
    result = predict_outbreak(date)
    return result


# prediction over a date range
@app.get("/predict-range")
def get_prediction_range(start_date: str, end_date: str):
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    df_range = data_fe[(data_fe['date'] >= start_date) & (data_fe['date'] <= end_date)]

    if df_range.empty:
        return {"error": "No data found for this date range"}

    preds = []
    for _, row in df_range.iterrows():
        df_input = row[model_features_order].to_frame().T.copy()

        # Fix dtypes
        for col in df_input.columns:
            if col == "area":
                df_input[col] = df_input[col].astype("category")
            else:
                df_input[col] = pd.to_numeric(df_input[col], errors="coerce")

        pred = float(model_lgbm.predict(df_input)[0])
        preds.append({
            "date": row['date'].strftime("%Y-%m-%d"),
            "prediction": pred,
            "reported_cases": int(row['reported_cases']),
            "true_cases": int(row['true_cases'])
        })

    return {"predictions": preds}


# time series data for water quality vs cases
@app.get("/water-vs-cases")
def water_vs_cases():
    df = data_fe[['date', 'water_ph_avg', 'water_turbidity_avg',
                  'contamination_avg', 'reported_cases', 'true_cases']].copy()

    records = df.to_dict(orient="records")
    return {"water_cases_data": records}


# feature importance
@app.get("/feature-importance")
def feature_importance():
    importance = model_lgbm.feature_importances_
    importance_dict = dict(zip(model_features_order, importance))

    sorted_features = sorted(
        [(str(k), int(v)) for k, v in importance_dict.items()],
        key=lambda x: x[1],
        reverse=True
    )[:10]

    return {"feature_importance": sorted_features}

# area-wise trends
@app.get("/area-trends")
def area_trends():
    df = data_fe.groupby("area").agg({
        "true_cases": "sum",
        "reported_cases": "sum",
        "population": "mean"
    }).reset_index()

    return {"area_stats": df.to_dict(orient="records")}
