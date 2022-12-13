#     AUTOR:    BrincandoComIdeias
#     APRENDA:  https://cursodearduino.net/
#     SKETCH:   Meu primeiro Robo com Pico
#     DATA:     05/12/22

import machine
from utime import sleep as delay 

pinLdr = machine.ADC(26)
pinServo = machine.Pin(15)

garra = machine.PWM(pinServo)
garra.freq(50) #Frequencia do sinal do Servo

# Valores min e max da garra utilizada
anguloMin = 45 
anguloMax = 78 

# Valores min e max das leituras do LDR
Vmin = 170 
Vmax = 250 

# Equivalente a função map()
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Converte um angulo no valor de pulso do Servo
def pulsoServo(x):
    if (x <= 0) :
        return 3276 # 1 mS = 0º
    elif (x >= 180) :
        return 6553 # 2 mS = 180º
    else :
        return map(x, 0, 180, 3276, 6553) 

while True:
    
    leitura = pinLdr.read_u16() # 0 ~ 65535
    tensao = map(leitura, 0, 65535, 0, 330)
    angulo = map(tensao, Vmin, Vmax, anguloMin, anguloMax)
    
    garra.duty_u16(pulsoServo(angulo))
        
    print(f"Leitura: {leitura}\t Tensão: {tensao}\t Angulo: {angulo}    ", end='\r')
    delay(0.05) # delay de 50mS
    