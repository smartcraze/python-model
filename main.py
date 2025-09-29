from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_utils import predict_outbreak

app = FastAPI(title="Outbreak Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # change to ["http://localhost:3000"] in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Outbreak Prediction API is running"}

@app.get("/predict")
def get_prediction(date: str):
    result = predict_outbreak(date)
    return result
