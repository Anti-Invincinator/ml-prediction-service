# 🏠 California Housing Price Prediction API

This project is a production-ready machine learning microservice that predicts median house prices using the [California Housing Dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_california_housing.html). It is built with **FastAPI**, trained using **scikit-learn**, and designed for modularity, scalability, and deployability — ideal for demonstrating full-stack AI engineering skills in platforms like JazzX.

---

## 🚀 Features

- 🔧 RESTful API using FastAPI
- 📊 ML model trained with Linear Regression (scikit-learn)
- 🧠 Real-world data from California housing dataset
- 🧾 Full API docs via Swagger UI (`/docs`)
- ✅ Modular code (training, inference, schemas)

---

## 📦 Tech Stack

- Python 3.11
- FastAPI
- scikit-learn
- Pydantic
- Uvicorn
- Joblib

---

## 🛠️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Anti-Invincinator/ml-prediction-service.git
cd ml-prediction-service
```
### 2. Set up a virtual environment
```bash
python -m venv venv

venv\Scripts\activate    # On Windows
# source venv/bin/activate    # On macOS/Linux
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Train the model
```bash
python app/model/train.py
```
### 5. Run the API
```bash
uvicorn app.main:app --reload
```
### 6. Testing the API
Use the endpoint to access via SwaggerUI
👉 http://127.0.0.1:8000/docs
or use Postman POST http://127.0.0.1:8000/predict

## 📌 Next Steps
 🐳 Add Dockerfile and containerization support

 ☁️ Deploy to AWS (Lambda / EC2)

 🔁 Add model versioning & retraining hooks

 📈 Add logging, monitoring, and metrics
