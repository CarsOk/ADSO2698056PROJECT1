# calculadora de IMC
# IMC = Peso / (altura x altura)
# < 19: delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# mas de 30: obesidad

def calcularIMC(peso, alturaEnMetros):
    
    imc = int( peso / (alturaEnMetros * alturaEnMetros))
    return imc

def pedirELIMC():
    
    for i in range(1,datos):
        
        nombre = input('ingresa tu nombre = ')
        print(f'Hola, { nombre }')
        print('regalame unos datos.')
        peso = int(input('su peso en Kg = '))
        alturaEnCM = int(input('su altura en cm = '))
        alturaEnMetros = alturaEnCM / 100
        imc = int(calcularIMC(peso, alturaEnMetros))
        print('-------------------------------------')
        print('Gracias por utilizar nuestro sistema.')
        print('-------------------------------------')

        print(f' { nombre } su IMC es de { imc }')

        if imc <= 19:
            print('Y usted se encuentra en estado de delgades')
        if (imc >= 20) and (imc <= 25):
            print('Y usted se encuentra en un estado de peso normal')
        if (imc >= 26) and (imc < 30):
            print('Y usted se encuentra en estado de sobrepeso')
        if imc > 30:
            print('Y usted se encuentra en estado de obesidad')
        print('    ')

print('BIENVENIDO AL SISTEMA DE IMC')
datos = int(input("¿A cuantas personas le quiere sacar su IMC?"))

for i in range(1,datos):
  pedirELIMC()
        
