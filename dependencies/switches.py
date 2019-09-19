from .services import *
from .menus import *

def switchMain(value):
    if value == '1':
        while True:
            menuHost()
            opcion = input()
            if opcion == '0':
                break
            switchHost(opcion)
    elif value == '2':
        while True:
            menuPing()
            opcion = input()
            if opcion == '0':
                break
            switchPings(opcion)
    elif value == '3':
        while True:
            menuPuertos()
            opcion = input()
            if opcion == '0':
                break
            switchPuertos(opcion)
    elif value == '4':
        while True:
            menuLVM()
            opcion = input()
            if opcion == '0':
                break
            switchLVM(opcion)
    elif value == '5':
        while True:
            menuSSH()
            opcion = input()
            if opcion == '0':
                break
            switchPuertos(opcion)
    elif value == '6':
        while True:
            menuPuertos()
            opcion = input()
            if opcion == '0':
                break
            switchPuertos(opcion)
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 3. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()

def switchHost(value):
    if value == '1':
        asignIP()
    elif value == '2':
        refreshIP()
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()

def switchPings(value):
    if value == '1':
        pingNetwork()
    elif value == '2':
        pings()
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()

def switchPuertos(value):
    if value == '1':
        portsView()
    elif value == '2':
        portsKill()
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()


def switchLVM(value):
    if value == '1':
        viewLVM()
    elif value == '2':
        createPartitionLVM()
    elif value == '3':
        portsKill()
    
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()

def switchSSH(value):
    if value == '1':
        portsView()
    elif value == '2':
        portsKill()
    elif value == '3':
        portsKill()
    elif value == '4':
        portsKill()
    elif value == '5':
        portsKill()    
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()
