import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import datetime
import os

st.set_page_config(page_title="Empleos Cali 2025")

st.title("Generador de imágenes de empleo")
st.caption("Empleos Cali 2026")

cargo = st.text_input("Cargo")
ciudad = st.text_input("Ciudad")
contrato = st.text_input("Tipo de contrato (opcional)")

if st.button("Generar imagen"):
    if cargo and ciudad:
        img = Image.open("plantilla.png.PNG
").convert("RGB")
        draw = ImageDraw.Draw(img)

        texto = f"{cargo}\n{ciudad}"
        if contrato:
            texto += f"\n{contrato}"

        draw.text((100, 350), texto, fill="black")

        nombre = f"{cargo}_{ciudad}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        ruta = os.path.join("temp", nombre)

        os.makedirs("temp", exist_ok=True)
        img.save(ruta)

        st.image(img, caption="Imagen generada")
        st.success("Imagen generada correctamente")
    else:
        st.error("Por favor escribe al menos el cargo y la ciudad")
