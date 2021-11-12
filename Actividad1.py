class Actividad1():
    tex1 = ""
    tex2 = ""
    tex3 = ""
    def setTex1(self, tex1):
        self.tex1 = tex1        
    def getTex1(self):
        return self.tex1 

    def setTex2(self, tex2):
        self.texto2 = tex2
    def getTex2(self):
        return self.tex2
        
    def setTex3(self, tex3):
        self.tex3 = tex3
    def getTex3(self):
        return self.tex3 

    def calPromedio(self):
        longitud1 = len(self.tex1)
        longitud2 = len(self.tex2)
        longitud3 = len(self.tex3)        
        prome = ((longitud1 + longitud2 + longitud3)/3)
        return "El promedio de la longitudes es: ", prome

    def calcuMenor15(self):
        respuesta=""
        longitud1 = len(self.tex1)
        longitud2 = len(self.tex2)
        longitud3 = len(self.tex3)
        totalLongi = longitud1+longitud2+longitud3
        if totalLongi > 15:
            respuesta = "La longitud  mayor a 15"
        elif totalLongi < 15:
            respuesta = "La longitud menor a 15"
        else:
            respuesta = "La longitud igual a 15"      
        return respuesta

    def indicarCarac(self):
        respuesta =""
        longitud1 = len(self.tex1)
        longitud2 = len(self.tex2)
        longitud3 = len(self.tex3)
        if longitud1 > longitud2 and longitud1> longitud3:
            respuesta = "El texto que tiene mas caracteres es: ", self.tex1
        elif longitud2 > longitud1 and longitud2> longitud3:
            respuesta = "El texto que tiene mas caracteres es: ", self.tex2
        elif longitud3 > longitud1 and longitud3> longitud2:
            respuesta = "El texto que tiene mas caracteres es: ", self.tex3 
        return respuesta

    def cantidadNum(self):
        numeros = ['0','1','2','3','4','5','6','7','8','9']
        contar=0        
        concatenacion = self.tex1 + self.tex2 + self.tex3
        for caracter in concatenacion:
            for numero in numeros:
                if caracter == numero:
                    contar+=1
        return "La cantidad de caracteres de numemros es: ", contar
