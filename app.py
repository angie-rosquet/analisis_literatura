#____________________________________________Bibliotecas que necesitamos_________________________________________________________________________________________________________________________________________________________________# 
import streamlit as st
from pathlib import Path
import pandas as pd
import json
import os 
import plotly.express as px
from PIL import Image
import numpy as np
#propia
import bibliotecas.own_library_st as olst

#_______________________________________________DataFrames necesarios y variables_______________________________________________________________________________________________________________________________________________________#
# dataframe premios unidos cervantes y nobel
df_premios = olst.df_all_p

#dataframe bestsellers todos, casa del libro, amazon, nyt
df_bestsellers = olst.df_all_bs 

#dataframe de la relacion de los premiados(todos) con los bestsellers
df_relacion_premio_bestseller_all = olst.relacion_premio_bs_all

# dataframe de lo mismo de arriba pero exceptuando la casa del libro y vervantes que es solamente para habla hispana 
df_relacion_premio_bestseller_eng = olst.relacion_premio_bs

# porciento de los autores con premio nobel que tienen al menos un bestseller
porciento_all = olst.v1  #todo

porciento = olst.v2

#dataframe de los autores con premios que tienen bessellers

filtter_jusy_nonel_with_bs = olst.relacion_filtrada


# para tener la ruta de donde se ejecuta este archivo
BASE_DIR = Path(__file__).parent

# como los datos estan en esta ruta pero dentro de la carpeta data me creo esta variable
DATA_DIR = BASE_DIR / "data"

#esta es la ruta del archivo de la foto que va a ser el icono del storytelling
icon_path = BASE_DIR / "icon.png"


#____________________________________________PAGINA______________________________________________________________________________________________________________________________________________________________________________________________#

# CONFIGURACION DE LA PAGINA
st.set_page_config(
    page_title="Narrativa en Datos",
    page_icon= str(icon_path) if icon_path.exists() else "📚",
    layout="wide"
    )

#creacion menu del costado
with st.sidebar:
    st.title("📚 Menú")
    categoria = st.radio(
        "Aquí se encuentran las opciones para navegar en nuestro sitio:",
        options=["Página Principal de Presentación", "Storytelling: Canon vs Mercado", "Data Product","Data Frame Bestsellers New York Times", "Data Frame Bestsellers Amazon", "Data Frame Bestsellers Casa del Título(2018-2024)", "Data Frame Premios Nobel", "Data Frame Premios Cervantes", "Acerca de"],
        index=0
    )
    
# Agregos al sidebar
st.sidebar.markdown("Síguenos en Instagram: ")
st.sidebar.link_button("@narrativa_en_datos", "https://www.instagram.com/narrativa_en_datos/")
st.sidebar.link_button("nuestro canal en Youtube siguelo para estar atento al video", "https://www.youtube.com/@arraset_ds")
    
#_____________________________________________________Presentacion______________________________________________________________________________________________________________________________________#
if categoria == "Página Principal de Presentación":
    st.title("Proyecto Narrativa en Datos")

    # Vizualización introductoria
    st.subheader("Tenemos todo un listado de curiosidades analíticas para indagar. Si te apasiona la lectura y como esta se desenvuelve en el mundo actual, esto te interesa.")
    st.markdown("Esta app une el poder de la **Ciencia de Datos** con la pasión por la **literatura**.")
    st.markdown("Aquí podrás:")
    st.markdown(" ► Explorar una colección de libros ordenada por autores y títulos.")
    st.markdown(" ► Buscar, filtrar y descargar obras literarias.")
    st.markdown(" ► Observar gráficos interactivos que revelan información sobre la literatura actual. Navega ya en nuestro Dataproduct!")
    st.markdown(" ► Disfrutar de una historia acerca de la literatura utilizando Ciencia de Datos(Se encuentra en la Sección del Storytelling).")
    st.markdown(" ► Si le interesa seguir curoseando puede acceder a nuestro video de Youtube donde también hablamos acerca de literatura con datos(al final de esta página).")
    imagen_1 = Image.open("imagenes/1.png")
    st.image(imagen_1)
#___________________________________________________Storytelling__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#  
if categoria == "Storytelling: Canon vs Mercado":
                                                            #Intro
    st.write("""
        ## Las dos caras del éxito literario: el mercado y el canon  
        Imagina que entras a una librería. A tu izquierda, una pila de ejemplares de El código Da Vinci con un cartel que dice "Más de 100 millones vendidos". A tu derecha, un estante modesto con los Cuentos completos de Clarice Lispector y una medalla que reza "Premio Nobel". Dos mundos, dos formas de entender la literatura.  
        **¿Qué tipo de lector eres?**  
        La pregunta no es trivial. Es como elegir entre:  
        * **🍔 Una hamburguesa jugosa que satisface al instante**  
        * **🍷 Un vino reserva que exige paladar entrenado**  
        O entre:  
        * **🎵 El éxito viral de Bad Bunny** (4.6 mil millones de streams en Spotify)  
        * **🎻 La profundidad de una ópera de Verdi** (que perdura siglos)  
        En el cine, sería preferir:  
        * **🎥 Los Vengadores** (taquilla récord)  
        * **🎞️ Parásitos** (Óscar a mejor película)  
        Durante décadas nos han dicho que hay dos caminos excluyentes:  
        1. El mercado (bestsellers):  
        - Dan Brown, Stephen King, J.K. Rowling
        - Fórmulas narrativas probadas  
        2. El canon (premios):    
        - Toni Morrison, José Saramago, Olga Tokarczuk  
        - Innovación lingüística  
        - Reconocimiento académico  
        **Pero... ¿y si es falso? ¿de verdad hay que elegir un solo camnino?**  
             
        Primeramente, debemos entender que es un bestseller (en inglés, literalmente "mejor vendido") es un término usado en la industria editorial para referirse a Títulos que han vendido una gran cantidad de ejemplares en poco tiempo. Si desea conocer mas acerca de los bestsellers puedes visitar nuestro video en youtube(el link se encuentra en el menú) 
        Mientras que canon literario se refiere a una selección de textos que, por su valor estético, histórico, filosófico o lingüístico, son considerados fundamentales dentro de una literatura nacional o universal. Lo que define que una obra o autor es un canon literario son los siguientes aspectos:  
        1.	Calidad literaria (innovación en el lenguaje, profundidad temática, estilo).  
        2.	Influencia en otras obras, autores y movimientos.  
        3.	Reconocimiento institucional, como:  
        •	Premios literarios (Nobel, Cervantes)  
        •	Presencia en planes de estudio y universidades  
        •	Crítica especializada y académica  
        4.	 Permanencia en el tiempo (son obras que siguen leyéndose y analizándose décadas o siglos después de su publicación).  
        Bestseller ≠ Canon literario  
        Un bestseller no implica calidad literaria según los criterios académicos. Algunos bestsellers son criticados por tener fórmulas comerciales (por ejemplo, After de Anna Todd), mientras que otros sí tienen mérito literario (como Cien años de soledad).
        Esto nos da los primeros destellos de solapamiento entre el canon literario y los bestsellers.
        """)
    
                                                        #La historia     
    
    #explicacion 1
    st.write("""
             Cuando uno piensa en el Premio Nobel de Literatura, imagina solemnidad: discursos densos, novelas introspectivas, y autores que difícilmente aparecen en la mesa de novedades del supermercado.  
             Pero… esta gráfica nos invita a cuestionar ese prejuicio.  
             Aquí se representan los autores ganadores del Nobel desde 1994 hasta 2024 y cuántos bestsellers han logrado, según los datos recopilados. La gama de colores refleja desde quienes nunca han figurado entre los más vendidos (morado oscuro), hasta quienes lo han logrado cuatro veces (amarillo brillante).  
             Y la sorpresa es clara:  
             🟡 Louise Glück, Kazuo Ishiguro, Mario Vargas Llosa, Elfriede Jelinek y J.M. Coetzee son ejemplos de escritores que, además de haber sido reconocidos por su maestría literaria, han logrado capturar el gusto del público general, con hasta 4 títulos bestseller cada uno.  
             🟢 Autores como Alice Munro, Orhan Pamuk, Doris Lessing también muestran una notable presencia comercial con 2 o 3 bestsellers.  
             🔵 Pero también están los Nobel que permanecen fuera del radar popular. Olga Tokarczuk, Svetlana Alexievich, entre otros, tienen una fuerte presencia crítica pero cero presencia en listas de ventas recientes.
             """)


    #grafico de cantidad de bestsellers que tiene un autor premiado

    def graficar_autores_con_bestsellers(df_relacion):
        
        df = df_relacion.copy()
        df['año'] = df['año'].astype(int)  #asegurar q sea un entero
        df['count'] = df['count'].fillna(0).astype(int)

        df['barra'] = df['count'].apply(lambda x: x if x > 0 else 0.0001)
        df = df.sort_values('año')

        autores_ordenados = df.drop_duplicates('autor', keep='first')['autor'].tolist()

        df['autor'] = pd.Categorical(df['autor'], categories=autores_ordenados, ordered=True)
        
        fig = px.bar(
            df,
            x='barra',
            y='autor',
            orientation='h',
            color='count',
            color_continuous_scale='Viridis',
            hover_data={'año': True, 'nationality': True, 'language': True, 'count': True, 'barra': False},
            labels={
                'barra': 'Número de Bestsellers',
                'autor': 'Autor',
                'año': 'Año del Premio',
                'count': 'Bestsellers'
            },
            height=700,
        )

        fig.update_traces(
            hovertemplate="<b>%{y}</b><br>" +
                        "Bestsellers: %{customdata[3]}<br>" +
                        "Premio: %{customdata[0]}<br>" +
                        "Nacionalidad: %{customdata[1]}<br>" +
                        "Idioma: %{customdata[2]}<extra></extra>"
        )

        fig.update_layout(
            coloraxis_colorbar=dict(title="Nº Bestsellers"),
            yaxis_title="Autor (ordenado por año del premio)",
            xaxis_title="Número de Bestsellers"
        )

        st.plotly_chart(fig, use_container_width=True)
        
    graficar_autores_con_bestsellers(df_relacion_premio_bestseller_all)
    
    st.write(f"""
                En los últimos 30 años, un {porciento}% de los autores galardonados con el Nobel de Literatura han logrado al menos un bestseller. Analizando los datos hasta 2023, observamos que anualmente ingresan a las listas de bestsellers una gran cantidad de títulos, aunque con picos notables en ciertos años.
                """)
    
    #grafico para ver en el tiempo la cantidad de bestsellers
    def grafico_lineal_bs(df_bestsellers):
        df = df_bestsellers.copy()
        df = df[~df['año'].isin([2024, 2025])]
        count_by_year = df['año'].value_counts().reset_index()
        count_by_year.columns = ['año', 'cantidad']
        count_by_year = count_by_year.sort_values('año')

        fig = px.line(
            count_by_year,
            x='año',
            y='cantidad',
            title='<b>Tendencia Anual de Bestsellers</b>',
            labels={'año': 'Año', 'cantidad': 'Número de Bestsellers'},
            markers=True,
            line_shape='spline',
            template='plotly_white',
            height=500
        )

        fig.update_layout(
            hovermode='x unified',
            xaxis=dict(tickmode='linear', dtick=1),
            yaxis_title='Número de libros',
            title_x=0.3
        )
        max_year = count_by_year.loc[count_by_year['cantidad'].idxmax()]
        fig.add_annotation(
            x=max_year['año'],
            y=max_year['cantidad'],
            text=f"Máximo: {max_year['cantidad']} en {max_year['año']}",
            showarrow=True,
            arrowhead=1
        )
        st.plotly_chart(fig, use_container_width=True)
        
    grafico_lineal_bs(df_bestsellers)
    
    st.write("""
             El pronunciado pico observado entre 1999 y 2003, que comenzó a descender en 2004 y luego se estabilizó, puede atribuirse principalmente a fenómenos literarios excepcionales. En 2003 se publicó la quinta entrega de Harry Potter: _Harry Potter y la Orden del Fénix_, cuyo éxito editorial coincidió con el lanzamiento de las adaptaciones cinematográficas, creando un fenómeno cultural sin precedentes. Ese mismo año, Dan Brown publicó _El código Da Vinci_, obra que generó controversia y cuyo éxito se tradujo posteriormente en una exitosa adaptación al cine.  
              Este período coincidió además con la expansión global de Amazon, que hasta 2003 solo operaba en Estados Unidos. La combinación de estos factores -el boom de sagas literarias, las adaptaciones cinematográficas y la democratización del acceso a libros mediante plataformas digitales- explica el notable incremento en ventas durante esta etapa.
                """)
    
    #grafico para ver el # de bestsellers por autor
    def num_bs_per_autor(df_bestsellers):
        bestsellers_por_autor = df_bestsellers['autor'].value_counts().reset_index()
        bestsellers_por_autor.columns = ['autor', 'cantidad']
        bestsellers_por_autor = bestsellers_por_autor.sort_values('cantidad', ascending=False)

        col1, col2 = st.columns(2)
        with col1:
            top_n = st.slider(
                "Mostrar top N autores",
                min_value=5,
                max_value=50,
                value=15,
                help="Selecciona cuántos autores quieres visualizar"
            )
        with col2:
            min_bestsellers = st.slider(
                "Mínimo de bestsellers por autor",
                min_value=1,
                max_value=int(bestsellers_por_autor['cantidad'].max()),
                value=2,
                help="Filtrar autores con al menos X bestsellers"
            )

        df_filtrado = bestsellers_por_autor[
            (bestsellers_por_autor['cantidad'] >= min_bestsellers)
        ].head(top_n)

        fig = px.bar(
            df_filtrado,
            x='cantidad',
            y='autor',
            orientation='h',
            title=f'<b>Top {top_n} Autores con más Bestsellers</b>',
            labels={'autor': 'Autor', 'cantidad': 'Número de Bestsellers'},
            color='cantidad',
            color_continuous_scale='Bluered',
            height=600 + (top_n * 10)  # Ajuste dinámico de altura
        )

        fig.update_layout(
            yaxis={'categoryorder': 'total ascending'},
            xaxis_title="Número de libros en listas de bestsellers",
            title_x=0.3,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)
    
    num_bs_per_autor(df_bestsellers)
    
    # promedio de cantidad de best sellers 
    bestsellers_por_autor = df_bestsellers['autor'].value_counts().reset_index()
    bestsellers_por_autor.columns = ['autor', 'cantidad']
    promedio = round(np.mean(bestsellers_por_autor['cantidad']))
        
    st.write(f"""
             Sin duda, J.K. Rowling es un fenómeno en estos listados, y aunque hay autores con más de 20 bestsellers, esta no es la norma. En promedio, los escritores que logran ingresar a estas listas tienen {promedio} bestsellers. Por lo tanto, en los últimos 30 años, la mitad de los autores premiados alcanzan un éxito moderado entre el público lector. Aunque no está mal para autores con una poca producción literaria nos demuestra que existe una difurcación en los caminos.  
             Mientras que la ficción domina ampliamente los listados de bestsellers -con el fenómeno BookTok impulsando géneros como el 'romantasy' hasta alcanzar una popularidad sin precedentes-, el estilo literario de los autores premiados tiende a ser más convencional, con una mayor presencia de obras de no ficción y narrativa literaria tradicional.
            """)
    
    
    

    # 1. Procesamiento: Contar apariciones por libro
    libros_populares = df_bestsellers.groupby(['titulo', 'autor', 'Género']).size().reset_index(name='apariciones')
    libros_populares = libros_populares.sort_values('apariciones', ascending=False)

    # 2. Gráfico de los top N libros
    top_n_libros = st.slider("Selecciona cuántos libros mostrar:", 5, 20, 10)

    fig_libros = px.bar(
        libros_populares.head(top_n_libros),
        x='apariciones',
        y='titulo',
        orientation='h',
        color='autor',
        title=f'<b>Top {top_n_libros} Libros con más apariciones en listas</b>',
        labels={'Título': '', 'apariciones': 'Veces en listas de bestsellers'},
        hover_data=['Género'],
        height=500 + (top_n_libros * 15)  # Ajuste dinámico de altura
    )

    fig_libros.update_layout(
        yaxis={'categoryorder': 'total ascending'},
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )

    st.plotly_chart(fig_libros, use_container_width=True)
    
    st.write("""
             
             """)
    
    # 1. Obtener lista de autores Nobel con bestsellers
    autores_nobel = filtter_jusy_nonel_with_bs['autor'].unique()
    
    # 2. Widget de selección con search
    autor_seleccionado = st.selectbox(
        "Selecciona un autor Nobel:",
        options=sorted(autores_nobel),
        format_func=lambda x: f"{x} ({filtter_jusy_nonel_with_bs[filtter_jusy_nonel_with_bs['autor']==x]['año'].values[0]})"
    )
    
    # 3. Datos del autor seleccionado
    datos_autor = filtter_jusy_nonel_with_bs[filtter_jusy_nonel_with_bs['autor'] == autor_seleccionado].iloc[0]
    año_nobel = datos_autor['año']
    
    # 4. Filtrar bestsellers del autor (insensible a mayúsculas/minúsculas)
    libros_autor = df_bestsellers[
        (df_bestsellers['autor'].str.lower() == autor_seleccionado.lower())
    ].sort_values('año')
    
    # 5. Gráfico de evolución
    if not libros_autor.empty:
        # Procesar datos
        evolucion = libros_autor['año'].value_counts().reset_index()
        evolucion.columns = ['año', 'cantidad']
        evolucion = evolucion.sort_values('año')
        
        # Crear figura
        fig = px.area(
            evolucion,
            x='año',
            y='cantidad',
            title=f'<b>{autor_seleccionado}: Bestsellers antes/después del Nobel {año_nobel}</b>',
            labels={'año': 'Año', 'cantidad': 'N° Bestsellers'},
            markers=True,
            line_shape='spline'
        )
        
        # Línea del Nobel
        fig.add_vline(
            x=año_nobel,
            line_dash="dash",
            line_color="red",
            annotation_text=f"Nobel {año_nobel}",
            annotation_position="top right"
        )
        
        # Área de análisis (5 años antes/después)
        fig.add_vrect(
            x0=año_nobel-5,
            x1=año_nobel+5,
            fillcolor="lightgray",
            opacity=0.2,
            annotation_text="Ventana de análisis",
            annotation_position="top left"
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # 6. Métricas clave
        col1, col2, col3 = st.columns(3)
        antes = libros_autor[libros_autor['año'] < año_nobel]
        despues = libros_autor[libros_autor['año'] >= año_nobel]
        
        with col1:
            st.metric("Total bestsellers", len(libros_autor))
        with col2:
            st.metric("Antes del Nobel", len(antes))
        with col3:
            cambio = len(despues) - len(antes)
            st.metric("Después del Nobel", len(despues), delta=f"{'+' if cambio>=0 else ''}{cambio}")
        
        # 7. Tabla de libros expandible (VERSIÓN CORREGIDA - sin columna 'fuente')
        with st.expander(f"📚 Ver todos los bestsellers de {autor_seleccionado}"):
            # Verificar qué columnas existen realmente en el DataFrame
            columnas_disponibles = ['Título', 'titulo', 'title', 'año', 'year']
            columnas_a_mostrar = [col for col in columnas_disponibles if col in libros_autor.columns]
            
            st.dataframe(
                libros_autor[columnas_a_mostrar],
                column_config={
                    "año": st.column_config.NumberColumn("Año", format="%d"),
                    "year": st.column_config.NumberColumn("Año", format="%d")
                },
                hide_index=True,
                use_container_width=True
            )
            
    else:
        st.warning(f"No se encontraron bestsellers para {autor_seleccionado} en los datos")
            
            
            
            
            
            
            
            
            
            
        
        
 























#____________________________________________________Data Product________________________________________________________________________________________________________________________________________________________________________________________#       


elif categoria == "Data Product":
    st.title("Data Product")        
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
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
   
#______________________________________________________________Data Frames_____________________________________________________________________________________________________________________________________________________________#    
elif categoria == "Data Frame Bestsellers New York Times":
    st.title("Recopilación de los Bestsellers en el New York Time de 1994 a 2024")
    olst.df_nyt

elif categoria == "Data Frame Bestsellers Amazon":
    st.title("Recopilación de los Bestsellers en Amazon 1995 a 2024")
    olst.df_amazon
    
elif categoria == "Data Frame Bestsellers Casa del Título(2018-2024)":
    st.title("Recopilación de los Bestsellers en Casa del Título de 1994 a 2024")
    olst.df_casalibro
    
elif categoria == "Data Frame Premios Nobel":
    st.title("Recopilación de los Premios Nobel de 1994 a 2024")
    olst.df_nobel
    
elif categoria == "Data Frame Premios Cervantes":
    st.title("Recopilación de los Premios Cervantes de 1994 a 2024")
    olst.df_cervantes
#_____________________________________________________Acerca de_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________#
elif categoria == "Acerca de":
    st.subheader("Este proyecto está desarrollado por estudiantes de Ciencia de Datos en la Universidad de La Habana con el objetivo de demostrar las capacidades del uso de las matemáticas y estadistica en la explicación de fenómenos, facilitar el acceso a las obras literarias y extraer información respecto a las tendencias literarias actuales.")
    st.markdown("Para cualquier queja o sugerencia contáctanos en https://www.instagram.com/narrativa_en_datos?igsh=b3EzcWtqN3Nnbmhn")
    with st.form("Feedback"):
        st.write("¿Qué tema te gustaría que analicemos?")
        sugerencia = st.text_input("Tu sugerencia")
        if st.form_submit_button("Enviar"):
            st.success("¡Gracias por tu aporte!")