#____________________________________________Bibliotecas que necesitamos_________________________________________________________________________________________________________________________________________________________________# 
import streamlit as st
from pathlib import Path
import json
import os 
import plotly.express as px
from PIL import Image
#propia
import bibliotecas.own_library_st as olst

#_______________________________________________DataFrames necesarios y variables_______________________________________________________________________________________________________________________________________________________#
# dataframe premios unidos cervantes y nobel
df_premios = olst.df_all_p

#dataframe bestsellers todos, casa del libro, amazon, nyt
df_bestsellers = olst.df_all_bs 

#dataframe de la relacion de los premiados(todos) con los bestsellers
df_relacion_premio_bestseller_all = olst.autores_con_bestsellers

# dataframe de lo mismo de arriba pero exceptuando la casa del libro y vervantes que es solamente para habla hispana 
df_relacion_premio_bestseller_eng = olst.sencillo

# porciento de los autores con premio nobel que tienen al menos un bestseller
porciento = olst.average_bestseller_premio(df_relacion_premio_bestseller_eng)    

# para tener la ruta de donde se ejecuta este archivo
BASE_DIR = Path(__file__).parent

# como los datos estan en esta ruta pero dentro de la carpeta data me creo esta variable
DATA_DIR = BASE_DIR / "data"

#esta es la ruta del archivo de la foto que va a ser el icono del storytelling
icon_path = BASE_DIR / "icon.png"
##################################################################################################################################################

# confihuracion preedetermianda de la pagina
st.set_page_config(
    page_title="Narrativa en Datos",
    page_icon= str(icon_path) if icon_path.exists() else "📚",
    layout="wide"
    )

# creacion menu del costado
with st.sidebar:
    st.title("📚 Menú")
    categoria = st.radio(
        "Aquí se encuentran las opciones para navegar en nuestro sitio:",
        options=["Página Principal de Presentación", "Storytelling: Canon vs Mercado", "Data Product","Data Frame Bestsellers New York Times", "Data Frame Bestsellers Amazon", "Data Frame Bestsellers Casa del Título(2018-2024)", "Data Frame Premios Nobel", "Data Frame Premios Cervantes", "Acerca de"],
        index=0
    )
    
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
    # Crear el sidebar
    st.sidebar.title("Navegación en la app")
    # Agregos al sidebar
    st.sidebar.markdown("Síguenos en Instagram: ")
    st.sidebar.markdown("[@narrativa_en_datos](https://www.instagram.com/narrativa_en_datos/)")
    st.sidebar.markdown("[nuestro canal en Youtube siguelo para estar atento al video](https://www.youtube.com/datarraset/)")
    # Imagen decorativa
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
        **Pero... ¿y si es falso? ¿existe una relación entre estos autores y/o obras que se “contraponen”?**  
             
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
             🔵 Pero también están los Nobel que permanecen fuera del radar popular. Bob Dylan, Olga Tokarczuk, Svetlana Alexievich, entre otros, tienen una fuerte presencia crítica pero cero presencia en listas de ventas recientes.
             """)

    #grafico de apoyo para explicacion 1
    fig1 = px.bar(
    df_relacion_premio_bestseller_eng,
    x='num_bestsellers',
    y='name',
    orientation='h',
    color='num_bestsellers',
    color_continuous_scale='Viridis',
    hover_data=['year', 'nationality', 'language'],
    labels={'cantidad de bestsellers': 'Número de Bestsellers', 'name': 'Autor', 'year': 'Año del Premio'},
    height=600
    )
    fig1.update_traces(
        hovertemplate="<b>%{y}</b><br>" +
                 "Bestsellers: %{x}<br>" +
                 "Premio: %{customdata[0]}<br>" +
                 "Nacionalidad: %{customdata[1]}<br>" +
                 "Idioma: %{customdata[2]}<extra></extra>"
                 )
    st.plotly_chart(fig1, use_container_width=True)
    st.markdown(f"En los últimos 30 años un **{porciento}%** de los autores premiados han tenido al menos un bestseller, es decir que un poco más de la mitad")
    st.markdown("")
    
    #grafico de la biblioteca que muetsra la cantidad de bestsellers que tienen cada autor despues de ganar su bestseller
    olst.many_best_after_nobel(olst.df_bs_eng, olst.df_nobel)
    
    
    #explicacion 2
    st.write()
    
    # grafico explicacion 2
    fig2 = px.scatter(
        df_relacion_premio_bestseller_eng,
        x='year',
        y='num_bestsellers',
        size='num_bestsellers',
        color='language',
        hover_name='name',
        hover_data=['nationality'],
        labels={'year': 'Año del Premio', 'num_bestsellers': 'Bestsellers'},
        size_max=30,
        height=500
        )
    fig2.update_traces(
        hovertemplate="<b>%{hovertext}</b><br>" +
        "Año: %{x}<br>" +
        "Bestsellers: %{y}<br>" +
        "Nacionalidad: %{customdata[0]}<extra></extra>"
        )
    st.plotly_chart(fig2, use_container_width=True)

    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
 























#____________________________________________________Data Product________________________________________________________________________________________________________________________________________________________________________________________#       
elif categoria == "Data Product":
    st.title("Data Product")        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
   
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