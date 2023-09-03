import os 
os.system("cls")

num1 = int(input("ingrese el primer numero:  "))
num2 = int(input("ingrese el segundo numero:  ")) 

menu = 0
while True:
    print("""
    MENU

    1- Suma
    2- Resta
    3- Multiplicacion
    4- division
    5- ingresar nuevos valores
    6- cerrar calculadora """)
    menu = int(input("Eliga una opcion del menu: ") )     

    if menu == 1:
        print("La suma del numero ",num1," y ",num2,"es igual a",num1+num2)
    elif menu == 2:
        print("la suma del numero ",num1," y ",num2,"es igual a",num1-num2)
    elif menu == 3:
        print("la suma del numero ",num1," y ",num2,"es igual a",num1*num2)
        
    elif menu == 4:
        print("La suma del numero ",num1,"y",num2,"es igual a",num1/num2)
    elif menu == 5:
        num1 = int(input("Introduce tu primer número: ") )
        num2 = int(input("Introduce tu segundo número: ") )
    elif menu == 6:
        break
    else:
        print("Opción incorrecta")