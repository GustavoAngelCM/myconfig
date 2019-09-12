# Python 3 required

# dependencies
from dependencies.menus import menuMain
from dependencies.switches import switchMain

while True:
    
    menuMain()
    opcion = input()

    if opcion == '0':
        break    
    
    switchMain(opcion)