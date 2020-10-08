from abc import ABC, abstractmethod, ABCMeta

class Instrumento(ABC):

    @abstractmethod
    def afinar(self):
        pass

    @abstractmethod
    def tocar(self):
        pass

    @abstractmethod
    def tocarnota(self, nota):
        #self.nota = nota
        pass


class Guitarra(Instrumento):

    def __init__(self):
        self = self

    def afinar(self):
        return print("Afinando Guitarra")

    def tocar(self):
        return print("Tocando Guitarra")

    def tocarnota(self, nota):
        #self.nota = nota
        return print("Tocando Guitarra en " + nota)


class Bajo(Instrumento):

    def __init__(self):
        self = self

    def afinar(self):
        return print("Afinando Bajo")

    def tocar(self):
        return print("Tocando Bajo")

    def tocarnota(self, nota):
        #self.nota = nota
        return print("Tocando Bajo en " + nota)


class Violin(Instrumento):

    def __init__(self):
        self = self

    def afinar(self):
        return print("Afinando Violin")

    def tocar(self):
        return print("Tocando Violin")

    def tocarnota(self, nota):
        #self.nota = nota
        return print("Tocando Violin en " + nota)