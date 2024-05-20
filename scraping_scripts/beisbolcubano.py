from bs4 import BeautifulSoup


with open('html_raw_data/2024-05-03/beisbolcubano/scoreboard.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()


def scrapping(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Estructura de datos para almacenar los datos que se van a devolver
    datos_globales = {}
    
    main_content = soup.find('div', id='MainContent_ctl02_UC_FSC_UpdatePanel')
    card_partido_list = main_content.find_all('li')
    
    # Cantidad de equipos
    cantidad_equipos = len(card_partido_list)
    
    cantidad_carreras = 0
    cantidad_hits = 0
    cantidad_errores = 0
    
    for partido in card_partido_list:
        div_score_list = partido.find_all('div', class_='col-lg-4 col-md-4 col-sm-4 col-xs-4 p-0')
        carreras_win = div_score_list[3]
        carreras_loss = div_score_list[6]
        
        hits_win = div_score_list[4]
        hits_loss = div_score_list[7]
        
        errores_win = div_score_list[5]
        errores_loss = div_score_list[8]
        
        cantidad_carreras += int(carreras_win.find('span').text)
        cantidad_carreras += int(carreras_loss.find('span').text)

        cantidad_hits += int(hits_win.find('span').text)
        cantidad_hits += int(hits_loss.find('span').text)

        cantidad_errores += int(errores_win.find('span').text)
        cantidad_errores += int(errores_loss.find('span').text)

        
      
    # Añadir valores al diccionario
    datos_globales['equipos'] = cantidad_equipos
    datos_globales['carreras'] = cantidad_carreras
    datos_globales['hits'] = cantidad_hits
    datos_globales['errores'] = cantidad_errores

    return datos_globales

print(scrapping(html))