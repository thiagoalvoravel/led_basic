import RPi.GPIO as GPIO         		#Importa a biblioteca das GPIO
import time                     		#Importa a biblioteca de tempo
import led_functions                            #Importa o modulo com as funcionalidades do LED

GPIO.setmode(GPIO.BOARD)   			#Configura o modo de definicao de pinos como BOARD (contagem de pinos da placa)
GPIO.setwarnings(False)         		#Desativa os avisos 


led_list = {"11": GPIO.setup(11, GPIO.OUT),     #Configura o pino 18 da placa (GPIO24) como saida
	    "12": GPIO.setup(12, GPIO.OUT),
            "13": GPIO.setup(13, GPIO.OUT),
            "15": GPIO.setup(15, GPIO.OUT),
            "16": GPIO.setup(16, GPIO.OUT),
            "18": GPIO.setup(18, GPIO.OUT)}	

while(1):                       		#Inicia o loop infinito
    #Acender os LEDs
    led_functions.turn_on(led_list)
    time.sleep(0.05)               		#Delay de 0.05 segundo
    #Apagar os LEDs
    led_functions.turn_off(led_list)
    time.sleep(0.05)               		#Delay de 0.5 segundo