# Python 3 required
# Operating system
import os
import sys
# dependencies
from dependencies.menus import *
from dependencies.switches import *

while True:
    menu()
    opcion = input()

    if opcion == '0':
        break    
    
    switchMain(opcion)
    
    pass
