import os 
os.system("cls")

def Convertir_A_Segundos(h,m,s):
	return h * 3600 + m * 60 + s

def Convertir_A_horasminutossegundos(seg):
	h = seg//3600
	seg = seg - h*3600
	m = seg//60
	seg = seg - m*60
	s = seg
	return h,m,s

while True:
	print("1.- Convertir horas, minutos y segundos a solo segundos")
	print("2.- Convertir segundos a horas, minutos y segundos")
	print("3.- Salir")
	opcion = int(input())
	if opcion == 1:
		hor = int(input("Horas:"))
		minu = int(input("Minutos:"))
		seg = int(input("Segundos:"))
		print("la conversion de horas, minutos y segundos a solo segundos nos da un resultado de  ",Convertir_A_Segundos(hor,minu,seg),"segundos.")
	elif opcion == 2:
		segund=int(input("Segundos:"))
		hor,minu,seg = Convertir_A_horasminutossegundos(segund)
		print("la conversion de segundos a horas,minutos y segundos nos da un resultado de  ",hor," horas :",minu,"minutos :",seg, "segundos")
	elif opcion == 3:
		break
	else:
		print("Opción incorrecta")
