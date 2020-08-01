import RPi.GPIO as GPIO         	#Importa a biblioteca das GPIO

def turn_on(led_list):
    for key in led_list:
        GPIO.output(int(key), 1)	#Coloca os pinos em nivel alto (1)

def turn_off(led_list):
    for key in led_list:
        GPIO.output(int(key), 0)	#Coloca os pinos em nivel baixo (0)

