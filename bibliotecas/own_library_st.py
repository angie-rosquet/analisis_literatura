## biblioteca para el storytelling
import json
from pathlib import Path
import pandas as pd
import plotly.express as px
import json
from collections import defaultdict
import plotly.graph_objects as go
from datetime import datetime

#rutas de los datos
amazon_path = "data\damazonoficial1995-2024.json"
casa_del_libro_path = "data\dcasa_del_libro_manual.json"
nobel_path = "data\dnobel_literature_1994_2024.json"
nyt_path = "data\dnotable_books_nyt.json"
premios_cervantes_path = "data\dpremios_cervantes.json"


#_______________________________________funcion para cargar los json_________________________________________________________________________#
def load_data(path):
    with open(path, 'r', encoding = 'utf-8') as f:
        json_data = json.load(f)
    return json_data

#DataFrames creados 
df_amazon = pd.DataFrame(load_data(amazon_path))
df_casalibro = pd.DataFrame(load_data(casa_del_libro_path))
df_nobel = pd.DataFrame(load_data(nobel_path))
df_nyt = pd.DataFrame(load_data(nyt_path))
df_cervantes = pd.DataFrame(load_data(premios_cervantes_path))

#___________________________________________funcion para normalizar los dataframe________________________________________________________________#

def normalize_df_bs(df):
    mapeo = {
        'titulo': 'titulo',
        'title': 'titulo',
        'nombre': 'titulo',
        'autor': 'autor',
        'author': 'autor',
        'escritor': 'autor',
        'name' : 'autor',
        'año': 'año',
        'year': 'año',
        'anio': 'año',
        'fecha': 'año',
        'Año': 'año',
        'publication_year': 'año'
    }
    df = df.rename(columns={k: v for k, v in mapeo.items() if k in df.columns})
    for col in ['titulo', 'autor', 'año']:
        if col not in df.columns:
            df[col] = None
    return df

#DataFrame Normalizado
df_amazon_n = normalize_df_bs(df_amazon)
df_casalibro_n = normalize_df_bs(df_casalibro)
df_nobel_n = normalize_df_bs(df_nobel)
df_nyt_n = normalize_df_bs(df_nyt)
df_cervantes_n = normalize_df_bs(df_cervantes)

#_________________________________________________________funcion para mezclar los dataframe(2 o 3)________________________________________________________________#

def mix_df_3(amazon_df, nyt_df, casalibro_df):
    bestsellers_unidos = pd.concat(
        [amazon_df, nyt_df, casalibro_df],
        ignore_index=True
        )
    bestsellers_unidos = bestsellers_unidos.sort_values('año', ascending=False)
    return bestsellers_unidos

# funcion para mezclar los dataframe 2
def mix_df_2(amazon_df, nyt_df):
    bestsellers_unidos = pd.concat(
        [amazon_df, nyt_df],
        ignore_index=True
        )
    bestsellers_unidos = bestsellers_unidos.sort_values('año', ascending=False)
    return bestsellers_unidos

df_all_bs = mix_df_3(df_amazon_n, df_nyt_n, df_casalibro_n)
df_eng_bs = mix_df_2(df_amazon_n, df_nyt_n)
df_all_p = mix_df_2(df_nobel_n, df_cervantes_n)

#________________________________________funcion para hallar la cantidad de libros bestsellers que tiene un ganador de premio________________________________________________________#
def procesar_autores_premiados(bestsellers_df, premios_df):
    conteo_bestsellers = bestsellers_df['Autor'].value_counts().reset_index()
    conteo_bestsellers.columns = ['autor_normalizado', 'num_bestsellers']
    autores_premiados = premios_df.merge(
        conteo_bestsellers,
        on='autor_normalizado',
        how='left'
    ).fillna({'num_bestsellers': 0})
    return autores_premiados

#dataframe con columna que dice la cantidad de bestsellers que tienen todos los premiados
autores_con_bestsellers = procesar_autores_premiados(df_all_bs, df_all_p)
#dataframe con columna que dice la cantidad de bestsellers que tienen todos los premiados nobel
sencillo = procesar_autores_premiados(df_eng_bs, df_nobel)

#______________________________________funcion por ciento de ganadores de bestsellers en ganadores nobel_______________________________________________________________________________________#
def average_bestseller_premio(dataframe):
    total_autor = len(dataframe)
    con_bestseller = dataframe[dataframe["num_bestsellers"] > 0].shape[0]
    if total_autor == 0:
        return 0.0
    porcentaje = (con_bestseller / total_autor) * 100
    return round(porcentaje, 2)


#_____________________________________funcion para ver los autores cuantos bestsellers tienen despues de su premio nobel_______________________________________________________________________________________#
def many_best_after_nobel(df_bestsellers, df_nobel):
    df_bestsellers["autor_normalizado"] = df_bestsellers["name"].str.lower().str.strip()
    df_nobel["autor_normalizado"] = df_nobel["autor_normalizado"].str.lower().str.strip()
    df_merge = pd.merge(df_bestsellers, df_nobel, on="autor_normalizado", suffixes=("_bestseller", "_nobel"))
    df_post_nobel = df_merge[df_merge["Año"] > df_merge["year"]]
    conteo = df_post_nobel["Autor"].value_counts().reset_index()
    conteo.columns = ["Autor", "Cantidad"]
    fig = px.bar(
        conteo,
        x="Cantidad",
        y="Autor",
        orientation="h",
        title="Autores con Bestsellers Publicados Después de Ganar el Premio Nobel",
        labels={"Cantidad": "Número de Bestsellers", "Autor": "Autor"},
        color="Cantidad",
        color_continuous_scale="plasma"
    )
    fig.update_layout(yaxis=dict(autorange="reversed"))  # Invertir eje Y para mejor lectura
    fig.show()



#_________________________________________funcion para ver si fueron bestsellers antes de ser premoio nobel______________________________________________________________________________________________#






#____________________________________________funcion para ver si el idioma esta presente en estas relaciones_______________________________________________#




#______________________________________funcion para calcular el por ciento de representacion femenina enlos premios nobel y en los bestsellers_______________________________________________________#



#______________________________________funcion para ver si los premios en castellano estan tan alejados como los premios nobel de los bessellers_________________________________________________#
