from random import randint
from Persona import *
from Instrumento import *

class Musico(Persona):
    
    def tocar(self,nota):
        #self.nota = nota
        opc = randint(0,2)
        if (opc == 0):
            i = Guitarra
            i.afinar("")
            i.tocar("")
            i.tocarnota("", nota)

        elif (opc == 1):
            i = Bajo
            i.afinar("")
            i.tocar("")
            i.tocarnota("", nota)

        elif (opc == 2):
            i = Violin
            i.afinar("")
            i.tocar("")
            i.tocarnota("",nota)