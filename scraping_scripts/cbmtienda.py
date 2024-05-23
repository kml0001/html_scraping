from bs4 import BeautifulSoup


with open('html_raw_data/2024-05-03/cbmtienda_muebles.html', 'r', encoding='utf-8') as archivo:
    html = archivo.read()


def scrapping(html):
    soup = BeautifulSoup(html, 'html.parser')

    # Estructura de datos para almacenar los datos que se van a devolver
    datos_globales = {}
    
    main_content = soup.find('div', class_='ast-woocommerce-container')
    div_producto_list = main_content.find('ul', class_='products columns-4').find_all('li')
    # Cantidad de equipos
    cantidad_productos = len(div_producto_list)
    
    precio_max = float('-inf')
    precio_min = float('inf')
    suma_total_precios = 0
    precio_promedio = 0
    
    for prodcuto in div_producto_list:
        span_precio_list = prodcuto.find_all('span', class_='woocommerce-Price-amount amount')
        
        precio_mayor = float('-inf')
        
        # Encontrar el mayor precio dentro de un producto
        for span_precio in span_precio_list:
            precio_valor = span_precio.bdi.get_text(strip=True).replace('$', '').replace(',', '')
            precio_valor_numerico = float(precio_valor)
        
            if precio_valor_numerico > precio_mayor:
                precio_mayor = precio_valor_numerico

        # Actualizar precio máximo y mínimo
        if precio_mayor > precio_max:
            precio_max = precio_valor_numerico
        if precio_mayor < precio_min:
            precio_min = precio_valor_numerico
        
        # Sumar al total de precios
        suma_total_precios += precio_valor_numerico

    # Calcular el precio promedio
    if cantidad_productos > 0:
        precio_promedio = suma_total_precios / cantidad_productos

        
      
    # Añadir valores al diccionario
    datos_globales['precio_maximo'] = precio_max
    datos_globales['precio_minimo'] = precio_min
    datos_globales['precio_promedio'] = precio_promedio

    return datos_globales

print(scrapping(html))