from fastapi import FastAPI
from pydantic import  BaseModel
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

loaded_model = load('../model/classifier.joblib')
loaded_scaler = load('../model/scaler.joblib')
reference_table = pd.read_csv('../model/cutoff_table.csv')


def get_prediction(data, duration):
    print('start prediction ----------------------')
    return apply_model(data, duration)


def apply_model(data, duration, model=loaded_model, scaler=loaded_scaler, reference=reference_table):
    # apply scaler & model to new meeting
    data_scaled = scaler.transform(data)
    predicted_cluster = model.predict(data_scaled)[0]
    # subset reference & rank new meeting duration
    print(int(predicted_cluster))
    print(reference_table.cluster)
    if int(duration) > int(reference_table[reference_table.cluster == int(predicted_cluster)].cutoff):
        show_alert = True
    else:
        show_alert = False
    return show_alert


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/predict/{param1}/{param2}/{param3}/{param4}/{param5}/{param6}/{param7}/{param8}/{param9}/{param10}/{param11}/{param12}/{param13}/{param14}")
def predict(param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14):
    data = [[param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14]]
    pred = get_prediction(data, param8)

    return pred
