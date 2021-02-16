# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:39:22 2021

@author: Praffulla
"""
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pickle_in = open('logisticRegr.pkl','rb')
classifier = pickle.load(pickle_in)

#Creating GUI
st.sidebar.header('Prediction Application')
select = st.sidebar.selectbox('Select Form',['Application 1'], key = '1')

if not st.sidebar.checkbox("Hide", False, key = '1'):
    st.title('Diabetes Prediction Application')
    name = st.text_input("Name:")
    pregnancy = st.number_input("Enter Number of pregnancy (put 0 for males):")
    glucose = st.number_input("Plasma Glucose Concentration:")
    bp = st.number_input("Blood pressure (in mm Hg):")
    skin = st.number_input("Triceps skin fold thickness (in mm):")
    insulin = st.number_input("2-Hour serum insulin: ")
    bmi = st.number_input("Body mass index (weight in kg/(height in m)^2):")
    dpf = st.number_input("Diabetes Pedigree Function:")
    age = st.number_input("Age:")
    
submit = st.button('Press to Predict')

if submit:
    prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
    if prediction == 0:
        st.write('Congratulations ',name,' you are not diabetic')
    else:
        st.write('Sorry ',name,' you seem to be diabetic. Please take care')
        