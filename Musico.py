from Instrumento import *
from random import randint, uniform,random
from Persona import *

class Musico(Persona):
    
    def tocar(self,nota):
        self.nota = nota
        opc = random.randrange(3)
        if (opc == 0):
            i = Guitarra
            i.afinar()
            i.tocar()
            i.tocar_nota(self.nota)

        elif (opc == 1):
            i = Bajo
            i.afinar()
            i.tocar()
            i.tocar_nota(self.nota)

        elif (opc == 2):
            i = Violin
            i.afinar()
            i.tocar()
            i.tocar_nota(self.nota)