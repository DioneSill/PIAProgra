#Leer datos

def guardar_txt(datos, campo):
    with open("Reportes de Consulta API/consulta.txt", "w", encoding="utf-8") as archivo:
        for t in datos:
            archivo.write(f"{t[campo]}\n")
    print("Datos guardados en TXT")

def leer_txt():
    try:
        with open("Reportes de Consulta API/consulta.txt", "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print("No existe archivo TXT")
        return []


datos = []
try:
    with open ("Reportes de Consulta API/consulta.txt","r", encoding = "utf-8") as archivo:
        for linea in archivo:
            partes = linea.strip().split(",")
            terremoto = {
            "magnitud": float(partes[0]),
            "lugar" : partes[1],
            "fecha": partes[2],
            "profundidad" : float(partes[3])

         }

        datos.append(terremoto)


 except=
     print("No se pudo leer el archivo")

    return datos

