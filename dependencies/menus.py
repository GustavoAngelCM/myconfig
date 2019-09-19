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
    print("| [4]. LVM Manager.                                                   |")
    print("| [5]. SSH Manager.                                                   |")
    print("| [6]. DHCP.                                                          |")
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


def menuLVM():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|           SCRIPT DE CONFIGURACIÓN EN PYTHON [LVM]                   |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. Ver particiones.                                               |")
    print("| [2]. Formatear disco y crear particiones.                           |")
    print("| [3]. Extender una particion.                                        |")
    print("| [0]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")

def menuSSH():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    else:    # Para otros sistemas y variantes de Unix
        print('ERROR AL LIMPIAR LA PANTALLA')

    print("+---------------------------------------------------------------------+")
    print("|           SCRIPT DE CONFIGURACIÓN EN PYTHON [SSH]                   |")
    print("+---------------------------------------------------------------------+")
    print("| [1]. Crear usuarios.                                                |")
    print("| [2]. Crear grupo.                                                   |")
    print("| [3]. Editar grupo.                                                  |")
    print("| [4]. Eliminar grupo.                                                |")
    print("| [5]. Eliminar usuario.                                              |")
    print("| [0]. Volver.                                                        |")
    print("+---------------------------------------------------------------------+")
    print("| Seleccione una opcion...                                            |")
    print("+---------------------------------------------------------------------+")

def menuDHCP():
   plataforma = sys.platform
   if plataforma == 'linux':
       os.system('clear')
   elif plataforma == 'win32':
       os.system('cls')
   else:    # Para otros sistemas y variantes de Unix
       print('ERROR AL LIMPIAR LA PANTALLA')

   print("+---------------------------------------------------------------------+")
   print("|           SCRIPT DE CONFIGURACIÓN EN PYTHON [DHCP]                  |")
   print("+---------------------------------------------------------------------+")
   print("| [1]. CREAR DHCP.                                                    |")
   print("| [2]. ASIGNAR IP POR MAC.                                            |")
   print("| [0]. Volver.                                                        |")
   print("+---------------------------------------------------------------------+")
   print("| Seleccione una opcion...                                            |")
   print("+---------------------------------------------------------------------+")