from bs4 import BeautifulSoup
import re

    
with open('html_raw_data/2024-05-03/insmetrss.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()

def scrapping(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Estructura de datos para almacenar los datos que se van a devolver
    datos_globales = {}
    
    cdata_content = soup.description.string  # Extrae el contenido de CDATA

    # Procesa el contenido de CDATA con BeautifulSoup
    soup_cdata = BeautifulSoup(cdata_content, 'html.parser')

    forecast_text = soup_cdata.get_text(separator="\n")

    # Expresiones regulares para extraer los datos específicos
    temperaturas_max_regex = re.search(r'máximas estarán entre (\d+) y (\d+) grados Celsius', forecast_text)
    temperaturas_min_regex = re.search(r'noche las temperaturas estarán entre (\d+) y (\d+) grados Celsius', forecast_text)
    viento_regex = re.search(r'velocidades entre (\d+) y (\d+) kilómetros por hora', forecast_text)

    # Extraer y almacenar datos específicos
    
    datos_globales['temperatura_max'] = temperaturas_max_regex.group(2) if temperaturas_max_regex else "No disponible"
    datos_globales['temperatura_min'] = temperaturas_min_regex.group(1) if temperaturas_min_regex else "No disponible"
    datos_globales['velocidad_viento_max'] = f"{viento_regex.group(2)} km/h" if viento_regex else "No disponible"
    datos_globales['velocidad_viento_min'] = f"{viento_regex.group(1)} km/h" if viento_regex else "No disponible"

    return datos_globales

print(scrapping(html))
