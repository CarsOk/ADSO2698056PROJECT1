import os
os.system("cls")

diccionario = {
    "programar" : "Programar es pasar el cafe a codigo",
    "POO" : "Programaciòn Orientada a Objetos",
    "MVC" : "Modelo Vista Controlador"
    
}

numeros = {
    "1" : "Uno",
    "2" : "Dos",
    "3" : "Tres",
    "4" : "Cuatro",
    "5" : "Cinco",
    "6" : "Seis",
    "7" : "Siete",
    "8" : "Ocho",
    "9" : "Nueve"
    
}

print("BIENVENIDO AL DICCIONARIO")
segir = True
while segir:
    print("--------------------")
    print('''Que quiere buscar?      
    - concepto 
    - numero 
          
    O desea:
    - salir''')
    print("--------------------")
    n1 = input('>')
    if n1 == 'salir' :
        segir = False
    if n1 == 'concepto' :
        n2 = input("¿Cual Concepto Quiere Buscar? =")
        print(diccionario[n2])
        print('  ')
        print("--------------------")
        print('  ')
        print('  ')
    if n1 == 'numero' :
        n3 = input("Que numero quiere buscar =")
        TF = ''
        for letra in n3:
            TF += numeros[letra] + ' '
        print(TF)
        print('  ')
        print("--------------------")
        print('  ')
        print('  ')
    