import requests

url = ""
params = {"fecha": fecha, "lugar":lugar}

respuesta = requests.get(url)


if respuesta.status_code == 200:
    datos = respuesta.json()


    else:
        print ("Error en la consulta")
        print ("¿Desea continuar?")
        return []


def guardar_txt(datos, campo):
     with open(f"Reportes de Consulta API/{campo}.txt", "w", encoding="utf-8") as archivo:
        for t in datos:
            archivo.write(f"{t[campo]}\n")
    print(f"Datos de {campo} guardados en TXT")
    
def consultar_profundidades():
    datos = consultar_api()
    for t in datos:
        print(f"Profundidad: {t['profundidad']} km")
    guardar_txt(datos, "profundidad")

def consultar_fechas():
    datos = consultar_api()
    for t in datos:
        print(f"Fecha y hora: {t['fecha']}")
    guardar_txt(datos, "fecha")

def consultar_magnitudes():
    datos = consultar_api()
    for t in datos:
        print(f"Magnitud: {t['magnitud']}")
    guardar_txt(datos, "magnitud")

def consultar_lugares():
    datos = consultar_api()
    for t in datos:
        print(f"Lugar: {t['lugar']}")
    guardar_txt(datos, "lugar")




        










