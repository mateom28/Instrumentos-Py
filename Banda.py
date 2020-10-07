from Instrumento import *
from random import randint, uniform,random
from Persona import *
from Musico import *

class Banda(Musico):

    def agregar_musico(nombreMusico):

        musicos.append(nombreMusico)

        return musicos

def presentar_banda(self):
        m = Musico
        lista = len(musicos)
        for nombre in range(0, lista):
            m.presentar(nombre)
            m.tocar()
    

b = Banda
b.agregar_musico("Pepito")
b.agregar_musico("Juan")
b.agregar_musico("Mariana")
b.presentar_banda("")