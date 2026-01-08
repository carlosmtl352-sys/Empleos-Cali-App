import streamlit as st

st.set_page_config(page_title="Empleos Cali 2025")

st.title("Generador de imágenes de empleo")
st.write("Empleos Cali 2025")

st.text_input("Cargo")
st.text_input("Ciudad")
st.text_input("Tipo de contrato (opcional)")

st.button("Generar imagen")
