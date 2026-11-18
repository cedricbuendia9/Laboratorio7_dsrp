import os
import pandas as pd
import joblib

def init():

    global model

    model_dir = os.environ["AZUREML_MODEL_DIR"]

    print("AZUREML_MODEL_DIR =", model_dir)

    for root, dirs, files in os.walk(model_dir):

        print("DIRECTORIO:", root)
        print("ARCHIVOS:", files)

        for file in files:

            if file.endswith(".pkl"):

                model_path = os.path.join(root, file)

                print("MODELO ENCONTRADO:", model_path)

                model = joblib.load(model_path)

                return

    raise Exception("No se encontró ningún archivo .pkl")

def run(mini_batch):

    results = []

    for file in mini_batch:

        df = pd.read_csv(file)

        print("======================")
        print(df.columns.tolist())
        print(df.head())
        print(df.dtypes)
        print("======================")

        pred = model.predict(df)

        df["prediction"] = pred

        results.append(df)

    return pd.concat(results)