#!/usr/bin/env python3

from colorama import Fore, Style
import os
import time

print(Fore.YELLOW + Style.BRIGHT)
pymap = '''
]KKKKKKNWw                     KKK     .KKKL      ]KKKH       ]KKKKKKNWw
]KK    "TKKN                  jKMKN    #KBKH     .KKRKKp      ]KK    "TKKN
]KK      ]KKL  9KN       #KR  ]KN1KN  #KL]KM     #KN ]KN      ]KK      ]KK
]KK      #KK    KKN     ]KK   ]KN 1Kp]KM ]KN    ]KK   KKN     ]KK      #KK
]KKWWW#KKKM      KKm   jKK^   ]KN  #KKM  ]KN   jKKL   "KKW    ]KKWWW#KKKM
]KKl""ll         "KKp .KKG    ]KM   MM   ]KN   KKNwwwww#KK    ]KK"""ll
]KK               1KKp#KM     #KM        ]KK  #KM*******9KN   ]KK
]KK                1KKKM      #KH        ]KK ]KK         KKN  ]KK
`""                ,KKM       l"          "' l"`         `"'  `""
                  ,gKKR
                1KKMF                  by SAMILOSOSAMI
'''
print(pymap + Style.RESET_ALL)
time.sleep(0.3)
ip_ordenador = input(Fore.CYAN + "Introduce la IP de la maquina victima: " + Style.RESET_ALL)

escaneo_sencillo = f"nmap {ip_ordenador}"
escaneo_avanzado_noverbose = f"nmap -p- --open -sV -sC -sS --min-rate 5000 -n -Pn {ip_ordenador}"
escaneo_avanzado_siverbose = f"nmap -p- --open -sV -sC -sS --min-rate 5000 -n -Pn -vvv {ip_ordenador}"

time.sleep(0.2)
tipo_escaneo = input(Fore.CYAN + "Deseas hacer un escaneo " + Style.RESET_ALL + Fore.YELLOW + Style.BRIGHT + "[1]sencillo " + Style.RESET_ALL + Fore.CYAN + "o " + Style.BRIGHT + Fore.YELLOW + "[2]avanzado" + Style.RESET_ALL + Fore.CYAN + "? " + Style.RESET_ALL)
time.sleep(0.2)

if tipo_escaneo.lower() == "2":
    time.sleep(0.2)
    verbose = input(Fore.GREEN + "Deseas mostrar el progreso en pantalla mientras de ejecuta? (S/N): " + Style.RESET_ALL)

    if verbose == "S":
        time.sleep(0.2)
        print()
        print(Fore.GREEN + " [+] Tipo de escaneo? " + Fore.YELLOW + "Avanzado")
        time.sleep(0.6)
        print(Fore.GREEN + " [+] Escaneo dinámico? " + Fore.YELLOW + "Si")
        time.sleep(0.6)
        print(Fore.GREEN + " [+] Velocidad promedio: " + Fore.YELLOW + "Media-lenta")
        time.sleep(0.6)
        print()
        print(Fore.MAGENTA +  Style.BRIGHT + "Escaneando..." + Style.RESET_ALL)
        time.sleep(1.5)
        print()
        os.system(escaneo_avanzado_siverbose)
    elif verbose == "N":
        time.sleep(0.2)
        print()
        print(Fore.GREEN + " [+] Tipo de escaneo? " + Fore.YELLOW + "Avanzado")
        time.sleep(0.6)
        print(Fore.GREEN + " [+] Escaneo dinámico? " + Fore.YELLOW + "No")
        time.sleep(0.6)
        print(Fore.GREEN + " [+] Velocidad promedio: " + Fore.YELLOW + "Media-lenta")
        time.sleep(0.6)
        print()
        print(Fore.MAGENTA + Style.BRIGHT + "Escaneando..." + Style.RESET_ALL)
        time.sleep(1.5)
        print()
        os.system(escaneo_avanzado_noverbose)

    else:
        time.sleep(0.1)
        print()
        print(Fore.RED + " [!] Escoge una de las opciones")
        print()



elif tipo_escaneo.lower() == "1":
    time.sleep(0.2)
    print()
    print(Fore.GREEN + " [+] Tipo de escaneo? " + Fore.YELLOW + "Sencillo")
    time.sleep(0.6)
    print(Fore.GREEN + " [+] Escaneo dinámico? " + Fore.YELLOW + "No")
    time.sleep(0.6)
    print(Fore.GREEN + " [+] Velocidad promedio? " + Fore.YELLOW + "Rápida")
    time.sleep(0.6)
    print()
    print(Fore.MAGENTA + Style.BRIGHT + "Escaneando..." + Style.RESET_ALL)
    time.sleep(1.5)
    print()
    os.system(escaneo_sencillo)

else:
   time.sleep(0.1)
   print()
   print(Fore.RED + " [!] Escoge una de las opciones")
   print()
