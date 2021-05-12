from fastapi import FastAPI, Query
from typing import List

from pydantic import BaseModel
from joblib import load
import pandas as pd

# define model for post request. Not needed if just implementing get
class ModelParams(BaseModel):
    param1: int
    param2: int
    param3: float
    param4: float
    param5: float
    param6: float
    param7: int
    param8: int
    param9: float
    param10: float
    param11: float
    param12: float
    param13: float
    param14: float


app = FastAPI()

loaded_model = load("../model/classifier.joblib")
loaded_scaler = load("../model/scaler.joblib")
reference_table = pd.read_csv("../model/cutoff_table.csv")


def get_prediction(data, duration):
    print("start prediction ----------------------")
    return apply_model(data, duration)


def apply_model(
    data, duration, model=loaded_model, scaler=loaded_scaler, reference=reference_table
):
    # apply scaler & model to new meeting
    data_scaled = scaler.transform(data)
    predicted_cluster = model.predict(data_scaled)[0]
    # subset reference & rank new meeting duration
    if int(duration) > int(
        reference_table[reference_table.cluster == int(predicted_cluster)].cutoff
    ):
        show_alert = True
    else:
        show_alert = False
    return show_alert


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/predict/")
def predict(
    p8: float, params: List[str] = Query(["p1", "p2", "p3", "p4", "p5", "p6", "p7"])
):

    data = [list(map(float, params[0].split(",")))]
    kwargs = {"param8": p8, "data": data}
    print(kwargs)

    pred = get_prediction(data, p8)
    return pred
