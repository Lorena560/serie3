#clase del módulo 
from Actividad1 import Actividad1
#objeto
actividad1 = Actividad1()

#llamamos al objeto 
actividad1.setTex1(input("Ingrese texto 1: "))
actividad1.setTex2(input("Ingrese texto 2: "))
actividad1.setTex3(input("Ingrese texto 3: "))

#llamamos al objeto para retornar 
print (actividad1.calPromedio())
print (actividad1.calcuMenor15())
print (actividad1.indicarCarac())
print (actividad1.cantidadNum())
