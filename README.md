
# 🚀 Disease Outbreak Prediction API

This project provides a **FastAPI service** that predicts outbreak risk for a given date using a trained **LightGBM model**.

---

## 📦 Requirements

* Python **3.12** (recommended)
* [pip](https://pip.pypa.io/en/stable/) or [uv](https://github.com/astral-sh/uv) for dependency management
* A working internet connection for installing packages

---

## ⚙️ Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-username/python-model.git
   cd python-model
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # on Linux/Mac
   venv\Scripts\activate      # on Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Check installed versions**

   ```bash
   pip show lightgbm scikit-learn fastapi uvicorn pandas
   ```

   > Make sure `lightgbm` and `scikit-learn` match the versions used during training.

---

## ▶️ Running the API

Start the server with:

```bash
uvicorn main:app --reload
```

The API will run at:
👉 `http://127.0.0.1:8000`

Interactive API docs available at:
👉 `http://127.0.0.1:8000/docs`

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

