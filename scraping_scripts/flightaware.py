from bs4 import BeautifulSoup
from utils import clean_string


with open('html_raw_data/2024-05-03/flightaware/datos_aeropuerto_santiago_cuba.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()


def scrapping(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Estructura de datos para almacenar los datos de todas las tablas
    datos_globales = {}

    tablas = soup.find_all('table', class_='airportBoard')

    for tabla in tablas:
        nombre_tabla = tabla.find('h2').text.strip()

        # Versión "limpia" del nombre de la tabla como clave para el diccionario
        nombre_clave = clean_string.clean_string_for_json(nombre_tabla)

        # Contar todas las filas ('tr') con id
        filas = tabla.find_all('tr', id=True)
        count = len(filas)
        
        datos_globales[nombre_clave] = count

    return datos_globales

print(scrapping(html))