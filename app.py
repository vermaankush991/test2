import numpy as np
import streamlit as st
import pickle

model = pickle.load(open('CustomerData.mdl','rb'))
st.title("Customer Segmentation")

age = float(st.text_input("Enter Age: ","18"))
salary = float(st.text_input("Enter Salary: ","10000"))

featureInput = np.array([[age,salary]])

sal = model.predict(featureInput)

st.write(f'Hello, *World!* :sunglasses: . Customer Group : {sal} ')