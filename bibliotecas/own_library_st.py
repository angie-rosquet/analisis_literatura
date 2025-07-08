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
        'Título': 'titulo',
        'nombre': 'titulo',
        'autor': 'autor',
        'author': 'autor',
        'escritor': 'autor',
        'name' : 'autor',
        'Autor': 'autor',
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
    for col in ['titulo', 'autor']:
        df[col] = df[col].astype(str).str.lower().str.strip()
    return df

#DataFrame Normalizado
df_amazon = normalize_df_bs(df_amazon)
df_casalibro = normalize_df_bs(df_casalibro)
df_nobel = normalize_df_bs(df_nobel)
df_nyt = normalize_df_bs(df_nyt)
df_cervantes = normalize_df_bs(df_cervantes)

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

df_all_bs = mix_df_3(df_amazon, df_nyt, df_casalibro)
df_eng_bs = mix_df_2(df_amazon, df_nyt)
df_all_p = mix_df_2(df_nobel, df_cervantes)


#______________________________________funcion para ver cuantos bestsellers tiene cada autor________________________________________________________#
def new_df_number_bs(df_bs):
    conteo_bestsellers = (
        df_bs['autor']
        .value_counts()
        .reset_index()
        .rename(columns={'index': 'autor', 'autor': 'autor'})
    )
    return conteo_bestsellers

#DataFrame de los autores con su cantidad de bestsellers
count_all = new_df_number_bs(df_all_bs)

count_eng = new_df_number_bs(df_eng_bs)

#___________________________________________funcion para mezclar los dataframe__________________________________________________________________________________________________________________________________#

def mix_df(df_all_p, count_all):
    df_merged = df_all_p.merge(
        count_all.rename(columns={'autor': 'autor', 'count': 'count'}),
        on='autor',
        how='left'
    )
    df_merged['count'] = df_merged['count'].fillna(0).astype(int)
    return df_merged

#DataFrame de los premiados con su cantidad de bestsellers

relacion_premio_bs_all = mix_df(df_all_p, count_all)

relacion_premio_bs = mix_df(df_nobel, count_eng)

#______________________________________funcion por ciento de ganadores de bestsellers en ganadores nobel_______________________________________________________________________________________#

def average_premios_bs(df_premios):
    total = len(df_premios)
    autores_con_bs = df_premios[df_premios['count'] > 0].shape[0]
    
    porcentaje = (autores_con_bs / total) * 100
    return round(porcentaje, 2)

v1 = average_premios_bs(relacion_premio_bs_all)

v2 = average_premios_bs(relacion_premio_bs)



#__________________________________________________________funcion para filtar el data frame de las relaciones por lo que tienen bestsellers_______________________________________________________________________________________________________________________________________________________#

def filtter_bs(df):
    return df[df['count'] > 0].copy()

relacion_filtrada = filtter_bs(relacion_premio_bs)







#_____________________________________funcion para ver los autores cuantos bestsellers tienen despues de su premio nobel_______________________________________________________________________________________#



#_________________________________________funcion para ver si fueron bestsellers antes de ser premoio nobel______________________________________________________________________________________________#






#____________________________________________funcion para ver si el idioma esta presente en estas relaciones_______________________________________________#




#______________________________________funcion para calcular el por ciento de representacion femenina enlos premios nobel y en los bestsellers_______________________________________________________#



#______________________________________funcion para ver si los premios en castellano estan tan alejados como los premios nobel de los bessellers_________________________________________________#
