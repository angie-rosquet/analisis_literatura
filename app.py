import streamlit as st
from pathlib import Path
import bibliotecas.own_library_st as olst
import json
import os 
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"
icon_path = BASE_DIR / "icon.png"

st.set_page_config(
    page_title="Storytelling Literario de Narrativa en Datos",
    page_icon= str(icon_path) if icon_path.exists() else "📚",
    layout="wide"
    )
with st.sidebar:
    st.title("📚 Menú")
    categoria = st.radio(
        "Aquí puedes ver los datos con los que se trabajan:",
        options=["Página Principla(Storytelling)", "Bestsellers New York Times", "Bestsellers Amazon", "Bestsellers Casa del Título(2018-2024)", "Premios Nobel", "Premios Cervantes"],
        index=0
    )
if categoria == "Página Principla(Storytelling)":
    
    # Intro
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
             
        Primeramente, debemos entender que es un bestseller (en inglés, literalmente "mejor vendido") es un término usado en la industria editorial para referirse a Títulos que han vendido una gran cantidad de ejemplares en poco tiempo.  
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
    
    #DataFrames necesarios
    df_premios = olst.df_all_p
    df_bestsellers = olst.df_all_bs 
    df_relacion_premio_bestseller_all = olst.autores_con_bestsellers
    df_relacion_premio_bestseller_eng = olst.sencillo
    
    #explicacion 1
    st.write("""""")
    
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

    st.header("Datos Completos")
    st.dataframe(
        df_relacion_premio_bestseller_all[['name', 'year', 'nationality', 'language', 'num_bestsellers']],
        column_config={
            "name": "Autor",
            "year": "Año Premio",
            "nationality": "Nacionalidad",
            "language": "Idioma",
            "num_bestsellers": "Bestsellers"
        },
        hide_index=True,
        use_container_width=True
    )
    st.write("""
             A pesar que el idioma que se ve mas distribuido entre años es el inglés hay una mayor concentración en español
             """)
    idiomas_counts = df_relacion_premio_bestseller_all['language'].value_counts()
    umbral = 3 
    idiomas_principales = idiomas_counts[idiomas_counts >= umbral]
    otros = idiomas_counts[idiomas_counts < umbral].sum()
    if otros > 0:
        idiomas_final = pd.concat([idiomas_principales, pd.Series({'Otros': otros})])
    else:
        idiomas_final = idiomas_principales
    plt.figure(figsize=(10, 8))
    plt.pie(
        idiomas_final,
        labels=idiomas_final.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=plt.cm.Paired.colors,
        wedgeprops={'edgecolor': 'white', 'linewidth': 1}
    )
    st.write("Existe una gran recurrencia entre autores premiados con Bestseller en español, esto significa que los autores en habla castellana son mejor premiados o mas vendidos, o tal vez logren encontrar la fórmula para ganar audiencia y a la vez innovar y tener un valor cultural significativo?")

    plt.title("Distribución de Idiomas entre Autores Premiados y Bestsellers", fontsize=14)
    st.write("Aunque en ingles hay mucha presencia el español revasa con creces a los demas idiomas")
    plt.axis('equal')
    plt.tight_layout()
    st.pyplot()
    
    
    
    
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
elif categoria == "Bestsellers New York Times":
    st.title("Recopilación de los Bestsellers en el New York Time de 1994 a 2024")
    olst.df_nyt

elif categoria == "Bestsellers Amazon":
    st.title("Recopilación de los Bestsellers en Amazon 1995 a 2024")
    olst.df_amazon
    
elif categoria == "Bestsellers Casa del Título(2018-2024)":
    st.title("Recopilación de los Bestsellers en Casa del Título de 1994 a 2024")
    olst.df_casalibro
    
elif categoria == "Premios Nobel":
    st.title("Recopilación de los Premios Nobel de 1994 a 2024")
    olst.df_nobel
    
elif categoria == "Premios Cervantes":
    st.title("Recopilación de los Premios Cervantes de 1994 a 2024")
    olst.df_cervantes