import os
import sys

def menu():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('echo "???"')
    
    print("+---------------------------------------------------------------------+")
    print("|                   SCRIPT DE CONFIGURACIÓN EN PYTHON                 |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. Visualizar dispositivos conectados a la red Actual.            |")
    print("| [2]. Ver Puertos.                                                   |")
    # print("| [2]. Gestionar Puertos.                                             |")
    print("| [3]. Configurar IP.                                                 |")
    print("| [4]. Configurar servidor  DHCP.                                     |")
    print("| [5]. Configurar servidor  PROXY.                                    |")
    print("| [6]. Configurar servidor  DNS.                                      |")
    print("| [7]. Configurar servidor  EMAIL.                                    |")
    print("| [8]. Configurar servidor  WEB.                                      |")
    print("| [9]. Configurar Virtual Host.                                       |")
    print("| [0]. SALIR                                                          |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")


def menuIP():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('echo "???"')

    print("+---------------------------------------------------------------------+")
    print("|                          ASIGNACION DE IP                           |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. Refrecar ip dinamicamente.                                     |")
    print("| [2]. Asignar ip especifica.                                         |")
    print("| [3]. Configurar DHCP.                                               |")
    print("| [4]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")


def menuScanner():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('echo "???"')

    print("+---------------------------------------------------------------------+")
    print("|                          ASIGNACION DE IP                           |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. Lista de dispositivos conectados a la red.                     |")
    print("| [2]. Realizar prueba de conexion.                                   |")
    print("| [3]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")