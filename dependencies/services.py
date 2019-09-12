import os
import sys
import subprocess

def asignIP():
    plataforma = sys.platform
    try:
        interface=''
        ip=''
        mascara=''
        gateway=''
        while True:
            if plataforma == 'linux':
                os.system('clear')
            elif plataforma == 'win32':
                os.system('cls')
            print("Ingrese la tarjeta sobre la cual se aplicara le IP. Ej: \n LINUX: enp0s3, enp0s8 \n WINDOWS: Ethernet, Wi-Fi")
            interface = input()
            print("Ingrese su nueva direccion IP. Ej: 192.168.43.48")
            ip = input()
            print("Ingrese la mascara de red. Ej: 255.255.255.0")
            mascara = input()
            print("Ingrese el gateway de la red(usualmente lleva al final el 1). Ej: 192.168.43.1")
            gateway = input()
            if (interface != '') and (ip != '') and (mascara != '') and (gateway != ''):
                break
            else:
                print("Complete los campos nuevamente. (puede que algunos campos no esten completados) ")
                interface = input()
        interface.strip()
        ip.strip()
        mascara.strip()
        gateway.strip()
        if plataforma == 'linux':
            release = subprocess.Popen(
                ['sudo', 'ifconfig', interface, ip, 'netmask', mascara],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = release.communicate()
            release1 = subprocess.Popen(
                ['sudo', 'route', 'add', ip, 'gw', gateway, interface],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout1, stderr1 = release1.communicate()
        elif plataforma == 'win32':
            release = subprocess.Popen(
                ['netsh', 'interface', 'ipv4', 'set', 'address', 'name='+interface, 'static', ip, mascara, gateway],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = release.communicate()
        print("\n\nCambio realizado.")
        print("\n\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()
    except:
        print("Error inesperado[ENTER]")
        variable = input()


def refreshIP():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')
    try:
        if plataforma == 'linux':
            release = subprocess.Popen(
                ['sudo', 'dhclient', '-r'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = release.communicate()

            renew = subprocess.Popen(
                ['sudo', 'dhclient'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = renew.communicate()

        elif plataforma == 'win32':
            release = subprocess.Popen(
                ['ipconfig', '/release'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = release.communicate()

            renew = subprocess.Popen(
                ['ipconfig', '/renew'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            stdout, stderr = renew.communicate()

        print("\n\nRefrescado exitoso.")

        print("\n\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()
    except:
        print("Error inesperado[ENTER]")
        variable = input()

def pingNetwork():
    plataforma = sys.platform
    try:
        network = ''
        mask = ''
        while True:
            if plataforma == 'linux':
                os.system('clear')
            elif plataforma == 'win32':
                os.system('cls')
            print('Ingrese la dirección de red que desea analizar. Ej: 192.168.1.0')
            network = input()
            print('Ingrese la mascara de red en numeros naturales. Ej: 24')
            mask = input()
            if (network != '') and (mask != ''):
                break
            else:
                print("Complete los campos nuevamente. (puede que algunos campos no esten completados) ")
                interface = input()
        net = network.strip()
        netPoint = net.split('.')
        # n=1
        # while n<256:
        #     if plataforma == 'linux':
        #         os.system('ping -c 1 '+netPoint[0]+'.'+netPoint[1]+'.'+netPoint[2]+'.'+str(n))
        #     elif plataforma == 'win32': 
        #         os.system('ping -n 1 '+netPoint[0]+'.'+netPoint[1]+'.'+netPoint[2]+'.'+str(n))
        #     n=n+1
        
        scanner(net, mask)
        
        print("\n\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()
    except NameError:
        print(NameError.__gt__)
        print("\n\n\nERROR[Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()



def pings():
    plataforma = sys.platform
    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')

    try:
        print('Ingrese la dirección ip. Ej: 192.168.1.5')
        ip = input()
        if plataforma == 'linux':
            scan = subprocess.Popen(
                ['ping', '-c', '4', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            stdout, stderr = scan.communicate()

            cadena = stdout.decode('cp1252')
            x = cadena.split('\n')

            for item in x:
                sin_espacios = item.strip()
                print(sin_espacios)

        elif plataforma == 'win32':
            scan = subprocess.Popen(
                ['ping', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            stdout, stderr = scan.communicate()
            cadena = stdout.decode('cp1252')

            x = cadena.split('\r\n')

            for item in x:
                sin_espacios = item.strip()
                print(sin_espacios)

        print("\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()
    except:
        print("\n\n\nError [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()


def scanner(network, mask):
    plataforma = sys.platform

    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')

    try:

        scan = subprocess.Popen(
            ['nmap', '-sP', network+'/'+mask],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        stdout, stderr = scan.communicate()

        cadena = stdout.decode('cp1252')

        if plataforma == 'linux':
            x = cadena.split('\n')
        elif plataforma == 'win32':
            x = cadena.split('\r\n')

        salida = []
        item_salida = []

        for item in x:

            sin_espacios = item.strip()

            if len(sin_espacios) > 0:

                if sin_espacios.find('for') != -1:

                    if len(item_salida) > 0:
                        item_salida = []

                    ip = sin_espacios.split(' ')
                    item_salida.append(ip[len(ip)-1])
                    salida.append(item_salida)
                    # print('ip')

                if sin_espacios.find('latency') != -1:
                    remove_open = sin_espacios.replace('(', '')
                    remove_close = remove_open.replace(')', '')
                    latencia = remove_close.split(' ')
                    item_salida.append(latencia[3])
                    # print('latency')

                if sin_espacios.find('MAC') != -1:
                    mac_remove_open = sin_espacios.replace('(', '')
                    mac_remove_close = mac_remove_open.replace(')', '')
                    mac = mac_remove_close.split(' ')
                    item_salida.append(mac[2])
                    # print('MAC')

        num = 0

        for host in salida:
            num = num + 1
            if len(host) == 1 :
                print("| {}  |(IP) {} |(Latencia) -- |(MAC) -- |".format(num, host[0]))
            elif len(host) == 2 :
                print("| {}  |(IP) {} |(Latencia) {} |(MAC) -- |".format(num, host[0], host[1]))
            elif len(host) == 3 :
                print("| {}  |(IP) {} |(Latencia) {} |(MAC) {} |".format(num, host[0], host[1], host[2]))

            print("--------------------------------------------------------------")

        if plataforma == 'win32':
            print("El ultimo registro es la direcion ip de la maquina actual.")

        print("{} dispositos conectados.".format(num))
        print("\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()

    except:
        print('Puede que NMAP no este instalado. \ncomprueba usando nmap -v o dirigente a la pagina de descarga https://nmap.org/download.html ')
    

def portsView():

    plataforma = sys.platform

    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')

    try:
        print('Ingrese la dirección ip. Ej: 192.168.1.5')
        ip = input()
        
        if plataforma == 'linux':
            scan = subprocess.Popen(
                ['sudo','nmap', '-sS', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            stdout, stderr = scan.communicate()
        elif plataforma == 'win32':
            scan = subprocess.Popen(
                ['nmap', '-sS', ip],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            stdout, stderr = scan.communicate()
        
        # print(type(stdout))

        cadena = stdout.decode('cp1252')

        if plataforma == 'linux':
            x = cadena.split('\n')
        elif plataforma == 'win32':
            x = cadena.split('\r\n')

        for item in x:
            sin_espacios = item.strip()
            print(sin_espacios)

        print("\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()
    except:
       print('\n\n\nERROR: Puede que NMAP no este instalado. \ncomprueba usando nmap -v o dirigente a la pagina de descarga https://nmap.org/download.html ')
       variable = input()

def portsKill():
    try:
        plataforma = sys.platform

        if plataforma == 'linux':
            os.system('clear')
            print('Ingrese la dirección ip. Ej: 192.168.1.5 [para visualizar los puertos]')
            ip = input()
            os.system('sudo nmap -sS -v '+ ip)
            print('Ingrese el puerto para cerrar Ej: 80/tcp.')
            port = input()
            os.system('sudo fuser -k '+ port)
            print('\n\n\nPuerto cerrado. [ENTER]')
            variable = input()

        elif plataforma == 'win32':
            print('\n\n\nWindows no permitido [ENTER]')
            variable = input()
    except:
        print('\n\n\nERROR [ENTER]')
        variable = input()
