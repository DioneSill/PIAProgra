#Validar datos
def validar_numero(valor):
    try:
        return int(valor)
    except ValueError:
        print("Entrada inválida, debe ser un número")
        return None

while True:

    try:
        valor = float(input(mensaje))

        return valor  


    except:

        print("Ingresar numero valido")
