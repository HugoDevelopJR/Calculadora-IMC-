# Proyecto: Calculadora de Índice de Masa Corporal (IMC).
# Objetivo: Determinar el estado nutricional. 
        
       # Introduccion :

print ( " ¡¡¡¡¡Tu salud es primero!!!!! ")

    # Introduccion de datos :

peso = float (input("Indique su peso en Kg: "))
estatura = float (input("Inserta tu estatura en metros: "))
edad = int (input("Ingresa tu edad: "))

IMC = (peso / estatura ** 2)

if edad < 5: 
    print ("No tienes suficiente edad para calcular tu masa aún. ")
elif estatura < 0:
    print ("La estatura no puede ser 0. ")
else:
    print ("Conozcamos tu indice de masa corporal: ")
  
  
    print (f"Tu IMC es de: {IMC:.2f} ")

    # Condiciones :

if IMC <= 18 :
    print ("Persona clasificacion bajo peso.") 
elif IMC <= 25 :
    print ("Persona clasificacion peso normal. ")
elif IMC <= 30 :
    print ("Persona clasificacion sobrepeso. ")
elif IMC <= 35 :
    print ("Persona clasificacion obesidad leve. ")
elif IMC <= 40 :
    print ("Persona clasificacion obesidad media. ")   
else : 
    print ("Persona clasificacion obesidad grado II o superior. ")



