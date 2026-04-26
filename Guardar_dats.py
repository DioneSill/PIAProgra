#Guardar datos

with open ("Reportes de Consulta API/consulta_fecha_hora.txt","w") as archivo:
    for t in datos :
        linea = f"{t['magnitud]}, {t['lugar]},{t['fecha']},{t['profunidad']}\n" archivo write (linea)
        print("Datos guardados correctamente")

except:

    print("Error al guardar el archivo")
    
    












