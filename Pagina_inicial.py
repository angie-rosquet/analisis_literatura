import streamlit as st
import os
from PIL import Image

st.title("Proyecto Narrativa en Datos")

# Vizualización introductoria
st.subheader("Tenemos todo un listado de curiosidades analíticas para indagar. Si te apasiona la lectura y como esta se desenvuelve en el mundo actual, esto te interesa.")
st.markdown("Esta app une el poder de la **Ciencia de Datos** con la pasión por la **literatura**.")
st.markdown("Aquí podrás:")
st.markdown(" ► Explorar una colección de libros ordenada por autores y títulos.")
st.markdown(" ► Buscar, filtrar y descargar obras literarias.")
st.markdown(" ► Observar gráficos interactivos que revelan información sobre la literatura actual.")

# Crear el sidebar
st.sidebar.title("Navegación en la app")

# Agregos al sidebar
st.sidebar.markdown("Síguenos en Instagram: ")
st.sidebar.markdown("[@narrativa_en_datos](https://www.instagram.com/narrativa_en_datos/)")
    
# Imagen decorativa
imagen_1 = Image.open("imagenes/1.png")
st.image(imagen_1)