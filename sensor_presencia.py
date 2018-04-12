#!/usr/bin/env python


import RPi.GPIO as GPIO    #Importamos la libreria GPIO
import time                #Importamos time
import os
from time import gmtime, strftime  #importamos gmtime y strftime
GPIO.setmode(GPIO.BCM)             #Configuramos los pines GPIO como BCM
PIR_PIN = 23                        #Usaremos el pin GPIO n16 real
GPIO.setup(PIR_PIN, GPIO.IN)       #Lo configuramos como entrada

#GPIO.setup(17, GPIO.OUT)          #Configuramos el pin 17 como salida (para un led)

try:
    while True:  #Iniciamos un bucle infinito
        if GPIO.input(PIR_PIN):  #Si hay senyal en el pin GPIO n7
            data = (time.strftime("%d_%m_%y"))
            hora = (time.strftime("%H:%M:%S"))
            nom= hora+data
#           GPIO.output(17,True) #Encendemos el led
            time.sleep(1)        #Pausa de 1 segundo
            
            print data +" "+hora + " MOVIMIENTO DETECTADO"  #La sacamos por pantalla
            time.sleep(1)  #Pausa de 1 segundo
            os.chdir('/media/HDD')
            os.system('mkdir -p Imatges')
            os.chdir('/media/HDD/Imatges')
            os.system('mkdir -p '+data)
            os.chdir('/media/HDD/Imatges/'+data)
            os.system('raspistill -vf -hf -o ' +hora+'.jpg')
            time.sleep(120)
#           GPIO.output(17,False)  #Apagamos el led
        time.sleep(1)              #Pausa de 1 segundo y vuelta a empezar
except KeyboardInterrupt:   #Si el usuario pulsa CONTROL + C...
    print "quit"            #Anunciamos que finalizamos el script
    GPIO.cleanup()          #Limpiamos los pines GPIO y salimos