import streamlit as st
import joblib

model = joblib.load("regression.joblib")

size = st.number_input("Taille (m²)", min_value=0.0, value=100.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=2, step=1)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0, step=1)

prediction = model.predict([[size, nb_rooms, garden]])

st.write("Prix prédit :", prediction[0])