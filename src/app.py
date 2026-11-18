from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "artifacts", "model.pkl")

model = joblib.load(MODEL_PATH)

@app.route("/")
def home():
    return "Diabetes Prediction API"

@app.route("/predict", methods=["POST"])
def predict():

    try:

        data = request.json

        print("DATA RECIBIDA:", data)

        features = np.array(
            data["features"]
        ).reshape(1, -1)

        prediction = model.predict(features)

        return jsonify({
            "prediction": int(prediction[0])
        })

    except Exception as e:

        print("ERROR:", str(e))

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)