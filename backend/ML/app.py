from fastapi import FastAPI, Request, Response
from pydantic import BaseModel
import joblib
import uvicorn
from Frauddata import Frauddata

# Load the trained Random Forest Classifier model
model = joblib.load("fraudmodel.joblib")

app = FastAPI()


@app.post("/predict")
async def predict(data:Frauddata):
    data = data.dict()
    time=data['time']
    v1=data['v1']
    v2=data['v2']
    v3=data['v3']
    v4=data['v4']
    v5=data['v5']
    v6=data['v6']
    v7=data['v7']
    v8=data['v8']
    v9=data['v9']
    v10=data['v10']
    v11=data['v11']
    v12=data['v12']
    v13=data['v13']
    v14=data['v14']
    v15=data['v15']
    v16=data['v16']
    v17=data['v17']
    v18=data['v18']
    v19=data['v19']
    v20=data['v20']
    v21=data['v21']
    v22=data['v22']
    v23=data['v23']
    v24=data['v24']
    v25=data['v25']
    v26=data['v26']
    v27=data['v27']
    v28=data['v28']
    amount=data['amount']

    # prediction = model.predict([[time,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,amount]])
    prediction = model.predict([[0,-1.35,0.266,0.166,0.0414481,0.06,-0.082,-0.078,0.085,-0.255,-0.866,1.6127,1.065,0.489,-0.143,0.6355,0.463,-0.114,-0.1833,-0.145,-0.169,-0.225,-0.638,0.101,-0.3398,0.0647,-0.221,0.062,0.06145,123.5]])

    return {int(prediction[0])}

@app.get('/')
def index():
    return {'message':'Hello Strangerrrr'}

@app.get('/{name}')
def get_name(name: str):
    return {'Welcome': f'{name}'}

