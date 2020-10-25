import numpy as np
from typing import List
from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel


class ModelParams(BaseModel):
    sepal_length_cm: float
    sepal_width_cm: float


def extract_meta_single_pred_result(prob: list) -> dict:
    label_pred = int(np.argmax(prob))

    classes = {
        0: "setosa",
        1: "versicolor",
        2: "virginica",
    }
    class_pred = classes[label_pred]

    return {
        "label_pred": label_pred,
        "class_pred": class_pred,
        "probability": prob,
    }


def prediction_array(x: np.ndarray) -> List[dict]:
    prob = model.predict_proba(x)
    return [
        extract_meta_single_pred_result(prob[i, :].tolist())
        for i in range(prob.shape[0])
    ]


app = FastAPI()
model = load("model/model.joblib")


@app.get("/healthcheck", status_code=200)
async def healthcheck() -> str:
    return "API is ready to go!"


@app.get("/predict-singleton/{sepal_length_cm}/{sepal_width_cm}")
def predict_singleton(sepal_length_cm: float, sepal_width_cm: float) -> dict:
    x = [[sepal_length_cm, sepal_width_cm]]
    pred = prediction_array(x)
    return pred[0]


@app.post("/predict-post/")
async def predict_post(model_params: List[ModelParams]) -> List[dict]:
    x = [
        (model_param.sepal_length_cm, model_param.sepal_width_cm)
        for model_param in model_params
    ]
    pred = prediction_array(np.array(x))
    return pred
