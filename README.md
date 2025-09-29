

# 🚀 Disease Outbreak Prediction API

This project provides a **FastAPI** service for predicting disease outbreak risk using a trained **LightGBM** model. The API exposes multiple endpoints for predictions, analytics, and feature insights.

---

## 📦 Requirements

- Python **3.12** (recommended)
- [pip](https://pip.pypa.io/en/stable/) or [uv](https://github.com/astral-sh/uv) for dependency management
- A working internet connection for installing packages

---

## ⚙️ Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-model.git
   cd python-model
   ```
2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Check installed versions**
   ```bash
   pip show lightgbm scikit-learn fastapi uvicorn pandas
   ```
   > Ensure `lightgbm` and `scikit-learn` match the versions used during model training.

---

## ▶️ Running the API

Start the server with:
```bash
uvicorn main:app --reload
```
The API will run at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

Interactive API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📖 API Endpoints

### 1. Health Check
**GET /**

Returns a simple message to confirm the API is running.

**Response:**
```json
{ "message": "Outbreak Prediction API is running" }
```

---

### 2. Predict Outbreak for a Date
**GET /predict?date=YYYY-MM-DD**

Predicts outbreak risk for a specific date.

**Query Parameters:**
- `date` (str, required): Date in `YYYY-MM-DD` format.

**Example:**
```bash
curl "http://127.0.0.1:8000/predict?date=2025-09-29"
```

**Response:**
```json
{
  "prediction": 0.151,
  "metrics": {
    "population": 3000,
    "water_ph": 6.91,
    "turbidity": 3.66,
    "reported_cases_7d": 376,
    "true_cases_7d": 618
  }
}
```

---

### 3. Predict Outbreak for a Date Range
**GET /predict-range?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD**

Returns predictions for all dates in the specified range.

**Query Parameters:**
- `start_date` (str, required): Start date in `YYYY-MM-DD` format
- `end_date` (str, required): End date in `YYYY-MM-DD` format

**Example:**
```bash
curl "http://127.0.0.1:8000/predict-range?start_date=2025-05-01&end_date=2025-05-15"
```

**Response:**
```json
{
  "predictions": [
    {
      "date": "2025-05-01",
      "prediction": 0.0026,
      "reported_cases": 56,
      "true_cases": 79
    },
    ...
  ]
}
```

---

### 4. Water Quality vs Cases
**GET /water-vs-cases**

Returns time series data for water quality metrics and reported/true cases.

**Response:**
```json
{
  "water_cases_data": [
    {
      "date": "2025-01-01T00:00:00",
      "water_ph_avg": 7.12,
      "water_turbidity_avg": 1.84,
      "contamination_avg": 0.38,
      "reported_cases": 0,
      "true_cases": 14
    },
    ...
  ]
}
```

---

### 5. Feature Importance
**GET /feature-importance**

Returns the top 10 most important features used by the model.

**Response:**
```json
{
  "feature_importance": [
    ["water_ph_avg", 567],
    ["true_cases", 555],
    ...
  ]
}
```

---

### 6. Area-wise Trends
**GET /area-trends**

Returns aggregated statistics for each area.

**Response:**
```json
{
  "area_stats": [
    {
      "area": "Village_B",
      "true_cases": 60520,
      "reported_cases": 36348,
      "population": 3000
    },
    ...
  ]
}
```

---

## ⚠️ Common Issues

- **Unknown datetime string format**: Use `YYYY-MM-DD` for all date parameters.
- **'super' object has no attribute 'get_params'**: Version mismatch between `scikit-learn` / `lightgbm`. Fix by reinstalling:
  ```bash
  pip install scikit-learn==1.2.2 lightgbm==3.3.5
  ```
- **404 Not Found at `/favicon.ico`**: Ignore, this is just the browser requesting a favicon.

---

## 📂 Project Structure

```
python-model/
│── main.py           # FastAPI app
│── model_utils.py    # Prediction logic
│── lgbm_model.pkl    # Saved LightGBM model
│── requirements.txt  # Python dependencies
│── README.md         # Project guide
│── Village B.xls     # Input data
```

---

## 🛠️ Next Steps

- Add more input features (not just date)
- Deploy to cloud (Heroku, Render, or AWS)
- Improve error handling and logging

---

## 📡 Usage

Send a **GET request** to `/predict` with a date in `YYYY-MM-DD` format:

### Example

```bash
curl "http://127.0.0.1:8000/predict?date=2025-09-29"
```

### Response

```json
{
  "date": "2025-09-29",
  "prediction": 1
}
```

---

## ⚠️ Common Issues

* **❌ Error: `Unknown datetime string format`**
  → You passed the wrong date format. Use `YYYY-MM-DD`.

* **❌ Error: `'super' object has no attribute 'get_params'`**
  → Version mismatch between `scikit-learn` / `lightgbm`.
  Fix by reinstalling:

  ```bash
  pip install scikit-learn==1.2.2 lightgbm==3.3.5
  ```

* **❌ 404 Not Found at `/favicon.ico`**
  → Ignore, it’s just the browser asking for a favicon.

---

## 📂 Project Structure

```
python-model/
│── main.py           # FastAPI app
│── model_utils.py    # Prediction logic
│── lgbm_model.txt    # Saved LightGBM model
│── requirements.txt  # Python dependencies
│── README.md         # Project guide
```

---

## 🛠️ Next Steps

* Add more input features (not just date).
* Deploy to cloud (Heroku, Render, or AWS).
* Improve error handling and logging.

### testing 
METHOD: GET
http://127.0.0.1:8000/predict?date=2025-05-15
{
  "prediction": 0.151593423819415,
  "metrics": {
    "population": 3000,
    "water_ph": 6.91,
    "turbidity": 3.66,
    "reported_cases_7d": 376,
    "true_cases_7d": 618
  }
}

METHOD : GET 
http://127.0.0.1:8000/predict-range?start_date=2025-05-01&end_date=2025-05-15

{
  "predictions": [
    {
      "date": "2025-05-01",
      "prediction": 0.00268888628711173,
      "reported_cases": 56,
      "true_cases": 79
    },
    {
      "date": "2025-05-02",
      "prediction": 0.0281400203074281,
      "reported_cases": 0,
      "true_cases": 87
    },
    {
      "date": "2025-05-03",
      "prediction": 0.0885819585076607,
      "reported_cases": 93,
      "true_cases": 86
    },
    {
      "date": "2025-05-04",
      "prediction": 0.016915357503871,
      "reported_cases": 0,
      "true_cases": 77
    },
    {
      "date": "2025-05-05",
      "prediction": 0.23961426233591,
      "reported_cases": 54,
      "true_cases": 104
    },
    {
      "date": "2025-05-06",
      "prediction": 0.00849513622940134,
      "reported_cases": 86,
      "true_cases": 83
    },
    {
      "date": "2025-05-07",
      "prediction": 0.161241527588463,
      "reported_cases": 115,
      "true_cases": 90
    },
    {
      "date": "2025-05-08",
      "prediction": 0.0311815280869042,
      "reported_cases": 0,
      "true_cases": 83
    },
    {
      "date": "2025-05-09",
      "prediction": 0.0289256871023723,
      "reported_cases": 48,
      "true_cases": 77
    },
    {
      "date": "2025-05-10",
      "prediction": 0.21064421795157,
      "reported_cases": 50,
      "true_cases": 100
    },
    {
      "date": "2025-05-11",
      "prediction": 0.403750544659134,
      "reported_cases": 0,
      "true_cases": 117
    },
    {
      "date": "2025-05-12",
      "prediction": 0.0374616252297982,
      "reported_cases": 137,
      "true_cases": 70
    },
    {
      "date": "2025-05-13",
      "prediction": 0.0258458757068915,
      "reported_cases": 46,
      "true_cases": 74
    },
    {
      "date": "2025-05-14",
      "prediction": 0.0532013532409521,
      "reported_cases": 44,
      "true_cases": 84
    },
    {
      "date": "2025-05-15",
      "prediction": 0.151593423819415,
      "reported_cases": 51,
      "true_cases": 96
    }
  ]
}


METHOD GET

http://127.0.0.1:8000/water-vs-cases

{
  "water_cases_data": [
    {
      "date": "2025-01-01T00:00:00",
      "water_ph_avg": 7.12,
      "water_turbidity_avg": 1.84,
      "contamination_avg": 0.38,
      "reported_cases": 0,
      "true_cases": 14
    },
    {
      "date": "2025-01-02T00:00:00",
      "water_ph_avg": 6.84,
      "water_turbidity_avg": 1.8,
      "contamination_avg": 0.77,
      "reported_cases": 11,
      "true_cases": 24
    },
    {
      "date": "2025-01-03T00:00:00",
      "water_ph_avg": 7.1,
      "water_turbidity_avg": 3.71,
      "contamination_avg": 1.85,
      "reported_cases": 0,
      "true_cases": 14
    },
    {
      "date": "2025-01-04T00:00:00",
      "water_ph_avg": 6.66,
      "water_turbidity_avg": 2.26,
      "contamination_avg": 2.98,
      "reported_cases": 0,
      "true_cases": 23
    },
    {
      "date": "2025-01-05T00:00:00",
      "water_ph_avg": 7.05,
      "water_turbidity_avg": 1.43,
      "contamination_avg": 2.82,
      "reported_cases": 24,
      "true_cases": 16
    }
}

GET: http://127.0.0.1:8000/feature-importance
{
  "feature_importance": [
    [
      "water_ph_avg",
      567],
    [
      "true_cases",
      555],
    [
      "true_cases_roll_std_14",
      468],
    [
      "asha_symptoms_diarrhea",
      441],
    [
      "population",
      434],
    [
      "cases_7d_sum",
      322],
    [
      "spillover_cases",
      280],
    [
      "asha_symptoms_vomiting",
      272],
    [
      "contamination_avg_roll_std_14",
      259],
    [
      "rainfall_1d",
      258]
  ]
}


GET http://127.0.0.1:8000/area-trends


{
  "area_stats": [
    {
      "area": "Village_B",
      "true_cases": 60520,
      "reported_cases": 36348,
      "population": 3000
    }
  ]
}