import os
import sys

def menuMain():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|          SCRIPT DE CONFIGURACIÓN EN PYTHON [INICIO]                 |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. HOST.                                                          |")
    print("| [2]. PING.                                                          |")
    print("| [3]. PUERTOS.                                                       |")
    print("| [0]. SALIR                                                          |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")

def menuHost():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|               SCRIPT DE CONFIGURACIÓN EN PYTHON [IP]                |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. IP ESTATICO.                                                   |")
    print("| [2]. IP DINAMICO.                                                   |")
    print("| [0]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")

def menuPing():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|              SCRIPT DE CONFIGURACIÓN EN PYTHON[PING]                |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. PING A LA RED.                                                 |")
    print("| [2]. PING DISPOSITIVO.                                              |")
    print("| [0]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")

def menuPuertos():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|           SCRIPT DE CONFIGURACIÓN EN PYTHON [PUERTOS]               |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. VER PUERTOS ABIERTOS.                                          |")
    print("| [2]. CERRAR PUERTO.                                                 |")
    print("| [0]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")