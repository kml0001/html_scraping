import re

def clean_string_for_json(input_string):
    """
    Esta función recibe un string y reemplaza todos los caracteres no alfanuméricos
    por guiones bajos, transforma el string resultante en minúsculas y asegura
    que termine con la extensión '.json', haciéndolo adecuado como nombre de archivo JSON.
    """
    
    # Reemplazar todos los caracteres no alfanuméricos por guiones bajos
    result = re.sub(r'\W+', '_', input_string)
    
    # Asegurar que el resultado no comienza ni termina con un guión bajo
    result = result.strip('_')
    
    # Convertir el resultado en minúsculas
    result = result.lower()
    
    # Añadir la extensión '.json' al resultado
    result += '.json'
    
    return result
