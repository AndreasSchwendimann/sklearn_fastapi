from fastapi import FastAPI, Query
from typing import List

from joblib import load
from pandas import read_csv


app = FastAPI()

loaded_model = load("../model/classifier.joblib")
loaded_scaler = load("../model/scaler.joblib")
reference_table = read_csv("../model/cutoff_table.csv")


def apply_model(
    data, duration, model=loaded_model, scaler=loaded_scaler, reference=reference_table
):
    # apply scaler & model to new meeting
    data_scaled = scaler.transform([data+[duration]])
    predicted_cluster = model.predict(data_scaled)[0]
    # subset reference & rank new meeting duration
    if int(duration) > int(
        reference[reference.cluster == int(predicted_cluster)].cutoff
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
    duration: int, meeting_data: List[str] = Query(["documents", "members",
                                     "lvl0", "lvl1", "lvl2", "lvl3",
                                     "items",
                                     "cat1","cat2","cat3","cat4","cat5","cat6"])
):

    data = list(map(float, meeting_data[0].split(",")))
    kwargs = {"data": data, "duration": duration}
    print(kwargs)

    pred = apply_model(data, duration)
    return pred
