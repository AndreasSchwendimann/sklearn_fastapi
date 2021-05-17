from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import List

from joblib import load
from pandas import read_csv


app = FastAPI()

loaded_model = load("../model/classifier.joblib")
loaded_scaler = load("../model/scaler.joblib")
reference_table = read_csv("../model/cutoff_table.csv")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def apply_model(
    data, duration, model=loaded_model, scaler=loaded_scaler, reference=reference_table
):
    # apply scaler & model to new meeting
    data_scaled = scaler.transform([data])
    predicted_cluster = model.predict(data_scaled)[0]
    # subset reference & rank new meeting duration
    if int(duration) >= int(
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
    meeting_data: List[str] = Query([12,8,
                                     0.1774193548387097,0.45161290322580644,0.3709677419354839,0,
                                     62,17100,
                                     0,1,0,0,0,0])
):

    data = list(map(float, meeting_data[0].split(",")))
    duration = data[7]
    kwargs = {"data": data, "duration": duration}
    print(kwargs)

    pred = apply_model(data, duration)
    return pred
