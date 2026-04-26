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
    




        










