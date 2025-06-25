#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import requests


# In[2]:


st.set_page_config(page_title="Obesity Prediction", layout="centered")
st.title("Prediksi Tingkat Obesitas")


# In[3]:


with st.form("obesity_form"):
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=5.0, max_value=100.0, step=1.0)
    height = st.number_input("Height (m)", min_value=1.0, max_value=2.5, step=0.01)
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=250.0, step=1.0)
    family_history = st.selectbox("Family History with Overweight", ["yes", "no"])
    favc = st.selectbox("Frequent High Calorie Food", ["yes", "no"])
    fcvc = st.slider("Vegetable Consumption (1–3)", 1.0, 3.0, 2.0)
    ncp = st.slider("Main Meals per Day", 1.0, 4.0, 3.0)
    caec = st.selectbox("Snacks Between Meals", ["no", "Sometimes", "Frequently", "Always"])
    smoke = st.selectbox("Do you Smoke?", ["yes", "no"])
    ch2o = st.slider("Water Intake (1–3)", 1.0, 3.0, 2.0)
    scc = st.selectbox("Monitor Calorie Consumption?", ["yes", "no"])
    faf = st.slider("Physical Activity (0–3)", 0.0, 3.0, 1.0)
    tue = st.slider("Technology Use (0–3)", 0.0, 3.0, 1.0)
    calc = st.selectbox("Alcohol Consumption", ["no", "Sometimes", "Frequently", "Always"])
    mtrans = st.selectbox("Transportation", ["Walking", "Bike", "Motorbike", "Public_Transportation", "Automobile"])

    submitted = st.form_submit_button("Predict")


# In[5]:


if submitted:
    payload = {
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }

    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        if "prediction" in result:
            st.success(f"Prediksi Obesitas: {result['prediction']}")
        else:
            st.error(f"Gagal prediksi: {result}")
    except Exception as e:
        st.error(f"Error menghubungi API: {e}")


# In[ ]:




