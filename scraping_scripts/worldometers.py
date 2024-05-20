from bs4 import BeautifulSoup


with open('html_raw_data/2024-05-03/worldometers/cuba_population.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()


def scrapping(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Estructura de datos para almacenar los datos que se van a devolver
    datos_globales = {}
    
    # Lista de algunos datos demograficos que se desean capturar
    div_country_pop_description = soup.find('div', class_='col-md-8 country-pop-description')
    
    # Elementos de la lista anterior:
    description_element_list = div_country_pop_description.find_all('li')
    # [0] -> current population
    # [1] -> last year population
    # [2] -> total world relation population
    # [3] -> rank by population
    # [4] -> population density
    # [5] -> total land area
    # [6] -> urban population
    # [7] -> median age
    
    li_poblacion_total = description_element_list[0]
    li_relacion_total_mundial = description_element_list[2]
    li_media_edad = description_element_list[7]
    li_urbanizacion = description_element_list[6]
    
    # Lista de contenedores con otros datos demograficos que se desean capturar
    div_demographics_list = soup.find_all('div', class_='panel panel-default')
    # [0] -> life expentancy
    # [1] -> infant mortality
    # [2] -> deaths under age 5
    
    div_mortalidad_infantil = div_demographics_list[1]
    div_muertes_menores_age_5 = div_demographics_list[2]
    div_esperanza_vida = div_demographics_list[0]
      
      
    # Añadir valores al diccionario
    datos_globales['poblacion_total'] = li_poblacion_total.find_all('strong')[1].text
    datos_globales['relacion_total_mundial'] = li_relacion_total_mundial.find('strong').text
    datos_globales['media_edad'] = li_media_edad.find_all('strong')[1].text
    datos_globales['urbanizacion'] = li_urbanizacion.find_all('strong')[0].text
    datos_globales['mortalidad_infantil'] = div_mortalidad_infantil.find('div', class_='panel-body').find('span').text
    datos_globales['muertes_menores_age_5'] = div_muertes_menores_age_5.find('div', class_='panel-body').find('span').text
    datos_globales['esperanza_vida'] = div_esperanza_vida.find('div', class_='panel-body').find('span').text

    return datos_globales

print(scrapping(html))