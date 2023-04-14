from abc import ABC, abstractmethod


class Alarme:
    def __init__(self):
        self.__rotinas = []

    def adicionar_rotina(self, rotina):
        self.__rotinas.append(rotina)

    def acionar_rotinas(self):
        for rotina in self.__rotinas:
            rotina.acionar()

    def despertar(self):
        print("Ta na hora!!!")
        self.acionar_rotinas()


class Acionador(ABC):
    @abstractmethod
    def acionar(self):
        pass


class AcionadorLuzes(Acionador):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotina(self)

    def acionar(self):
        print("Acendendo as luzes...")


class AcionadorCafe(Acionador):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotina(self)

    def acionar(self):
        print("Preparando o café...")


class AcionadorComputador(Acionador):
    def __init__(self, alarme):
        self.alarme = alarme
        self.alarme.adicionar_rotina(self)

    def acionar(self):
        print("Ligando o computador...")


if __name__ == "__main__":
    alarme = Alarme()
    AcionadorLuzes(alarme)
    AcionadorCafe(alarme)
    AcionadorComputador(alarme)
    alarme.despertar()
