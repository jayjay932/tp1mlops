from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("regression.joblib")

@app.get("/predict")
def predict_get(size: float, nb_rooms: int, garden: int):
    prediction = model.predict([[size, nb_rooms, garden]])
    return {"y_pred": prediction[0]}

@app.post("/predict")
def predict_post(size: float, nb_rooms: int, garden: int):
    prediction = model.predict([[size, nb_rooms, garden]])
    return {"y_pred": prediction[0]}