from abc import ABC, abstractmethod, ABCMeta

class Instrumento(ABC):

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def tocar(self, nota):
        self.nota = nota
        pass

class Guitarra(Instrumento):

    nombre = 'Guitarra'

    def __init__(self):
        self = self

    def tocar(self):
        return("tocando Guitarra")

    def afinar(self):
        return ("afinando Guitarra")

    def tocar(self,nota):
        return("tocando Guitarra en" + self.nota)   
   


class Bajo(Instrumento):

    nombre = 'Bajo'    
    
    def __init__(self):
        self = self

    def tocar(self):
        return("tocando Bajo")

    def afinar(self):
        return ("afinando Bajo")

    def tocar(self,nota):
        return("tocando Bajo en" + self.nota)  



class Violin(Instrumento):

    nombre = 'Violin'  

    def __init__(self):
        self = self

    def tocar(self):
        return("tocando Violin")

    def afinar(self):
        return ("afinando Violin")

    def tocar(self,nota):
        return("tocando Violin en" + self.nota)   


     
