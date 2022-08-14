import streamlit as st
import joblib
model = joblib.load('JOB_ROLE & SALARY')
st.title("JOB_ROLE & SALARY")
ip = st.text_input('Enter the job role:')
op = model.predict([ip])
if st.button('Enter'):
  st.title(op[0])
