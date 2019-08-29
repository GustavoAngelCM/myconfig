from .services import *

def switchMain(value):
    if value == '1':
        devices()
    elif value == '2':
        # devices()
        ports()
    elif value == '3':
        ips()
    elif value == '4':
        # devices()
        print("4")
    elif value == '5':
        # devices()
        print("5")
    elif value == '6':
        # devices()
        print("6")
    elif value == '7':
        # devices()
        print("7")
    elif value == '8':
        # devices()
        print("8")
    elif value == '9':
        # devices()
        print("9")
    else:
        print(
            "Error al seleccionar una opción, Seleccione valores entre 0 y 9. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()
