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
            menuDHCP()
            opcion = input()
            if opcion == '0':
                break
            switchDHCP(opcion)
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
        extendLVM()  
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()

def switchSSH(value):
    if value == '1':
        createUser()
    elif value == '2':
        createGroup()
    elif value == '3':
        editGroup()
    elif value == '4':
        deleteGroup()
    elif value == '5':
        deleteUser()    
    else:
        print("Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()


def switchDHCP(value):
    if value == '1':
        createDHCP()
    elif value == '2':
        addIPMAC()
    else:
        print(
            "Error al seleccionar una opción, Seleccione valores entre 0 y 2. \nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        enter = input()
