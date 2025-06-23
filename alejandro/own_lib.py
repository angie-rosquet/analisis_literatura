import json 
import pandas as pd
import os
import pdfplumber
import numpy as np

# Buscar los autores que más obras literarias sacaron en Amazon en los últimos 30 años:
def author_appearings(data:list[dict]):

    data_f = pd.DataFrame(data)

    author_count = {}
    for author in data_f["Autor"]:
        if author not in author_count:
            counter = 0
            for name in data_f["Autor"]:
                if name == author:
                    counter += 1
            author_count[author] = counter

    authors_count_df = pd.DataFrame(author_count.keys(),columns = ["Autores"])
    authors_count_df["Apariciones"] = author_count.values()

    return authors_count_df.sort_values(by = "Apariciones",ascending = False)

# Buscar cantidad de palabras únicas en la muestra de Títulos:
def unique_words(route:str):
    
    with pdfplumber.open(route) as pdf:
        texto_completo = ""

        for hoja in pdf.pages:
            texto = hoja.extract_text()
                    
            if texto:
                texto_completo += texto
        
    palabras = texto_completo.split(" ")
    palabras_unicas = set()
    
    for palabra in palabras:
        palabra_limpia = ""
        for letra in palabra:
            if ord(letra) in range(96,122) or ord(letra) in range(64,90) or ord(letra) in range(159,165):
                palabra_limpia += letra
        palabras_unicas.add(palabra_limpia)
    palabras_unicas = list(palabras_unicas)

    return palabras_unicas

# Analizar la cantidad de veces que aparece una nacionalidad en los autores ganadores en premios Nobel en los últimos 30 años:
def nat_counting(data:list[dict]):
    
    nationalities_count = {"Nacionalidad":[],"Conteo":[]}
    
    for i in range(len(data)):
        for nation in data[i]["nationality"].split("/"):
            if nation in nationalities_count["Nacionalidad"]:
                nationalities_count["Conteo"][nationalities_count["Nacionalidad"].index(nation)] += 1
            else:
                nationalities_count["Nacionalidad"].append(nation)
                nationalities_count["Conteo"].append(1)
            
    nationalities_count = pd.DataFrame(nationalities_count)
    return nationalities_count

# Analizar los tipos de literatura más repetidos según la lista de Títulos notables de The NY Times:
def lit_styles(nyt_notbooks:list[dict]):
    
    genders_count = {"Estilo":[],"Conteo":[]}
    for i in range(len(nyt_notbooks)):
        for gender in nyt_notbooks[i]["Género"].split(","):
            if gender in genders_count["Estilo"]:
                genders_count["Conteo"][genders_count["Estilo"].index(gender)] += 1
            else:
                genders_count["Estilo"].append(gender)
                genders_count["Conteo"].append(1)
    
    return pd.DataFrame(genders_count)

# Buscar los conteos de autores en la lista de publicaciones en Amazon:
def amazon_authors(data:list[dict]):
    
    data_f = pd.DataFrame(data)

    author_count = {}
    for author in data_f["Autor"]:
        if author not in author_count:
            counter = 0
            for name in data_f["Autor"]:
                if name == author:
                    counter += 1
            author_count[author] = counter

    authors_count_df = pd.DataFrame(author_count.keys(),columns = ["Autores"])
    authors_count_df["Apariciones"] = author_count.values()

    return authors_count_df

# Busca la reseña media de cada autor de Amazon en el orden del vector de entrada:
def med_califications(authors:list,amazon_info:list[dict]):
    
    med_cal = {"Autores": authors,"Estrellas promedio":[]}
    for author in authors:
        med_cal["Estrellas promedio"].append([])

    for i in range(len(amazon_info)):
        if amazon_info[i]["Estrellas"] != None:
            med_cal["Estrellas promedio"][med_cal["Autores"].index(amazon_info[i]["Autor"])].append(amazon_info[i]["Estrellas"])

    for y in range(len(med_cal["Autores"])):
        med_cal["Estrellas promedio"][y] = np.mean(med_cal["Estrellas promedio"][y])

    return pd.DataFrame(med_cal)

# Busca la cantidad media de calificaciones de cada autor de Amazon en el orden del vector de entrada:
def med_eval_quantity(authors:list,amazon_info:list[dict]):
    
    med_quant = {"Autores": authors,"Cant. evaluaciones por autor":[]}
    for author in authors:
        med_quant["Cant. evaluaciones por autor"].append([])

    for i in range(len(amazon_info)):
        if isinstance(amazon_info[i]["Número de Calificaciones"],int):
            med_quant["Cant. evaluaciones por autor"][med_quant["Autores"].index(amazon_info[i]["Autor"])].append(amazon_info[i]["Número de Calificaciones"])

    for y in range(len(med_quant["Autores"])):
        med_quant["Cant. evaluaciones por autor"][y] = np.median(med_quant["Cant. evaluaciones por autor"][y])

    return pd.DataFrame(med_quant)

# Busca el precio medio de las obras de para cada autor de Amazon en el orden del vector de entrada:
def med_cost(authors:list,amazon_info:list[dict]):
    
    med_price = {"Autores": authors,"Precios":[]}
    for author in authors:
        med_price["Precios"].append([])

    for i in range(len(amazon_info)):
        if isinstance(amazon_info[i]["Precio"],float):
            med_price["Precios"][med_price["Autores"].index(amazon_info[i]["Autor"])].append(amazon_info[i]["Precio"])

    for y in range(len(med_price["Autores"])):
        med_price["Precios"][y] = np.median(med_price["Precios"][y])

    return pd.DataFrame(med_price)