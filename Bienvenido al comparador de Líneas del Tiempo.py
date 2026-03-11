print ("Bienvenido al comparador de Líneas del Tiempo ")
    
    #actualizacion de año

año_actual = int(input("Introduce tu año actual: "))
calcular = int(input("Introduce otro año para calcular: "))

if año_actual > calcular :
    resto = año_actual - calcular

    if resto == 1 :

     print ("Desde el año "  +  str (calcular)  + " ha pasado solo 1 año. ")

    else :

      print ("Aun faltan "  +  str (resto)  +  " años para llegar al "  +  str(año_actual))

    input ()

elif año_actual < calcular :
   resto = calcular - año_actual

   if resto == 1 : 

    print ("Para llegar al año "  +  str(calcular)  +  " falta solo 1 año ")

   else :
     
     print ("Han transcurrido "  +  str (resto)  +  " años desde el "  +  str(año_actual))

   input ()

else : 
  
  print ("Has introducido el mismo año que el actual ")

  input ()
