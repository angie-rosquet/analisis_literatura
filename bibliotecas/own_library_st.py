## biblioteca para el storytelling
import json
from pathlib import Path
import pandas as pd
import plotly.express as px
import json
from collections import defaultdict
import plotly.graph_objects as go
from datetime import datetime

#rutas que necesito
amazon_path = "data\damazonoficial1995-2024.json"
casa_del_libro_path = "data\dcasa_del_libro_manual.json"
nobel_path = "data\dnobel_literature_1994_2024.json"
nyt_path = "data\dnotable_books_nyt.json"
premios_cervantes_path = "data\dpremios_cervantes.json"

#funcion para cargar los json
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

#funcion para normalizar los dataframe
def normalize_df_bs(df):
    mapeo = {
        'titulo': 'titulo',
        'title': 'titulo',
        'nombre': 'titulo',
        'autor': 'autor',
        'author': 'autor',
        'escritor': 'autor',
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

# funcion para mezclar los dataframe 3
def mix_df_3(amazon_df, nyt_df, casalibro_df):
    bestsellers_unidos = pd.concat(
        [amazon_df, nyt_df, casalibro_df],
        ignore_index=True
        )
    # Ordenar por año descendente
    bestsellers_unidos = bestsellers_unidos.sort_values('año', ascending=False)
    return bestsellers_unidos

df_all_bs = mix_df_3(normalize_df_bs(df_amazon), normalize_df_bs(df_nyt), normalize_df_bs(df_casalibro))
df_all_p = pd.concat(
    [df_nobel, df_cervantes],
    ignore_index= True
    )

# funcion para mezclar los dataframe 2
def mix_df_2(amazon_df, nyt_df):
    bestsellers_unidos = pd.concat(
        [amazon_df, nyt_df],
        ignore_index=True
        )
    # Ordenar por año descendente
    bestsellers_unidos = bestsellers_unidos.sort_values('año', ascending=False)
    return bestsellers_unidos

df_all_bs = mix_df_3(normalize_df_bs(df_amazon), normalize_df_bs(df_nyt), normalize_df_bs(df_casalibro))
df_all_p = pd.concat(
    [df_nobel, df_cervantes],
    ignore_index= True
    )

df_bs_eng = mix_df_2(normalize_df_bs(df_amazon), normalize_df_bs(df_nyt))

def procesar_autores_premiados(bestsellers_df, premios_df):
    premios_df['autor_normalizado'] = premios_df['name'].str.lower().str.strip()
    bestsellers_df['autor_normalizado'] = bestsellers_df['Autor'].str.lower().str.strip()
    conteo_bestsellers = bestsellers_df['autor_normalizado'].value_counts().reset_index()
    conteo_bestsellers.columns = ['autor_normalizado', 'num_bestsellers']
    autores_premiados = premios_df.merge(
        conteo_bestsellers,
        on='autor_normalizado',
        how='left'
    ).fillna({'num_bestsellers': 0})
    return autores_premiados

autores_con_bestsellers = procesar_autores_premiados(df_all_bs, df_all_p)

sencillo = procesar_autores_premiados(df_bs_eng, df_nobel)