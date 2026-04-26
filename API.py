import requests

def consultar_api():
    url = "aqui va el link"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()   # lista de diccionarios
    else:
        print("Error en la consulta")
        return []
