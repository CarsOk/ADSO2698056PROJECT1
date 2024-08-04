import os 
os.system("cls")
num1 = int(input("ingrese el primer numero:  "))
num2 = int(input("ingrese el segundo numero:  ")) 


a = int(input("menu\n1. suma\n2. resta\n3. multiplicacion\n4. division\n5. salir\n"))

print ("el resultado es ")

if (a == 1): 
    print (str(num1 + num2 ))
    
elif (a == 2):
    print (str(num1 - num2))
    
elif (a == 3):
    print (str(num1 * num2))

elif (a == 4):
    print (str(num1 / num2))
