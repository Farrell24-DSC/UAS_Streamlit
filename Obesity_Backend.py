#!/usr/bin/env python
# coding: utf-8

# In[3]:


from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np


# In[4]:


try:
    with open("model_obesity.pkl", "rb") as f:
        model = pickle.load(f)
    with open("label_encoder.pkl", "rb") as f:
        label_encoder = pickle.load(f)
    print("Model dan encoder berhasil dimuat.")
except Exception as e:
    raise RuntimeError(f"Gagal memuat model atau encoder: {e}")


# In[5]:


# Define API
app = FastAPI(title="Obesity Prediction API")

# Define input schema
class ObesityInput(BaseModel):
    Gender: str
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: str
    FAVC: str
    FCVC: float
    NCP: float
    CAEC: str
    SMOKE: str
    CH2O: float
    SCC: str
    FAF: float
    TUE: float
    CALC: str
    MTRANS: str


# In[6]:


@app.get("/")
def root():
    return {"message": "Obesity classification API is running"}

@app.post("/predict")
def predict(input_data: ObesityInput):
    try:
        data = np.array([[
            input_data.Gender, input_data.family_history_with_overweight, input_data.FAVC,
            input_data.CAEC, input_data.SMOKE, input_data.SCC, input_data.CALC, input_data.MTRANS,
            input_data.Age, input_data.Height, input_data.Weight, input_data.FCVC,
            input_data.NCP, input_data.CH2O, input_data.FAF, input_data.TUE
        ]])

        df = np.array(data).reshape(1, -1)
        pred = model.predict(df)[0]
        pred_label = label_encoder.inverse_transform([pred])[0]
        return {"prediction": pred_label}

    except Exception as e:
        return {"error": str(e)}


# In[ ]:




