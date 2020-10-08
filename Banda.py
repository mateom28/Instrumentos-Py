from Musico import *

class Banda(Musico):

    def agregarmusico(nombremusico):

        musicos.append(nombremusico)

        return (musicos)

    def presentarbanda(self):
        m = Musico
        lista = len(musicos)
        for nombre in range(0, lista):
            m.saludar("",nombre)
            m.tocar("","Do")
 
b = Banda
b.agregarmusico("Lorena")
b.agregarmusico("Mateo")
b.agregarmusico("Samuel")
b.agregarmusico("Julian")
b.presentarbanda("")
