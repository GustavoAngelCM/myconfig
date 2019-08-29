import os
import sys
import subprocess

def devices():
    
    plataforma = sys.platform

    if plataforma == 'linux':
        os.system('clear')
    elif plataforma == 'win32':
        os.system('cls')

    try:

        print('Ingrese la dirección de redque desea analizar. Ej: 192.168.1.0')
        network = input()
        print('Ingrese la mascara de red en numeros naturales. Ej: 24')
        mask = input()

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
        
        print("El ultimo registro es la direcion ip de la maquina actual.")            
        print("\n\nPresione [Enter] o cualquier tecla seguido de [Enter]  para continaur...")
        variable = input()

    except:

        print('Puede que NMAP no este instalado. \ncomprueba usando nmap -v o dirigente a la pagina de descarga https://nmap.org/download.html ')
