import streamlit as st

l = st.number_input("Enter Length")
w = st.number_input("Enter Width")

area = l*w

st.write(area)
