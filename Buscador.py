import streamlit as st
import pandas as pd
import os

# Función para obtener el catálogo
route = "books_"
@st.cache_data
def get_cat():
    catlog = []
    for author in os.listdir(route):
        author_route = os.path.join(route,author)
        if os.path.isdir(author_route):
            for book in os.listdir(author_route):
                book_route = os.path.join(author_route,book)
                name,extension = os.path.splitext(book)
                catlog.append({"autor":author,"titulo":name,"extension":extension.lower(),"ruta":book_route})
    return catlog

catlog = get_cat()

# Definición en dependencia de la página seleccionada

st.title("Buscador de obras literarias")
    
# Filtro por autores
autores = sorted(set([item["autor"] for item in catlog]))
initials = sorted(set(x[0].upper() for x in autores))

initial_select = st.sidebar.selectbox("Seleccionar inicial del autor",["Todas"] + initials)

if initial_select == "Todas":
    filtered_authors = autores
    author_select = filtered_authors
else:
    filtered_authors = [a for a in autores if a.upper().startswith(initial_select)]

    author_select = st.sidebar.multiselect("Filtrar por autor",filtered_authors,default = filtered_authors)

# Filtro por extensión
extensions = sorted(set([item["extension"] for item in catlog]))
ext_select = st.sidebar.multiselect("Filtrar por extensión",extensions,default = extensions)

# Búsqueda por título
st.text("En caso de no encontrar el libro por su nombre, puede buscar mediante la inicial del autor en la barra lateral y filtrar autores.")
texto_busqueda = st.text_input("Buscar por título")

# Filtrar la búsqueda
results = [item for item in catlog if item["autor"] in author_select and item["extension"] in ext_select and texto_busqueda.lower() in item["titulo"].lower()]

if results:
    st.success(f"Se han encontrado {len(results)} libros.")
        
    for item in results:
        st.write(f"**Título:** {item['titulo']}| \n**Autor:** {item['autor']}| \n**Extensión:** {item['extension']}")
        
        if os.path.isfile(item["ruta"]):
            with open(item["ruta"],"rb") as document:
                st.download_button(label = "Descargar libro",data = document,file_name = os.path.basename(item["ruta"]))
else:
    st.warning("No se encontraron libros con esos criterios.")