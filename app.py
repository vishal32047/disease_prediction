import streamlit as st
from pred_app import show_predict_page
from explore_ import show_explore_page

page = st.sidebar.selectbox("Explore or Predict",("Prediction","Exploration"))
if page == 'Prediction':
    show_predict_page()
else:
    show_explore_page()