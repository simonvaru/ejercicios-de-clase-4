from sys import exit
from textwrap import dedent


valor1 = int(input("Ingrese primer numero: "))
valor2 = int(input("Ingrese segundo numero: "))
r = 0

print(dedent("""
      Ingrese 1 si desea sumar los dos valores.
      Ingrese 2 si desea restar al 1er valor el 2do numero.
      Ingrese 3 si desea multiplicar el 1er valor por 2do numero.
      Ingrese 4 si desea interrumpir este programa.
      """))

valor3 = int(input("Ingrese respuesta: "))

#if valor3 == 4 or valor3 != range(1:4): 
if 1 > valor3 > 4:
    exit
    
else:    

    if valor3 == 1:
        r = valor1 + valor2
        print("Se eligió la opción 1 y el resultado es: ", r)
        
    elif valor3 == 2:
        r = valor1 - valor2
        print("Se eligió la opción 2 y el resultado es: ", r)
        
    elif valor3 == 3:
        r = valor1 * valor2
        print("Se eligió la opción 3 y el resultado es: ", r)
        
    elif valor3 == 4:
        print("Opción incorrecta.")    
 
