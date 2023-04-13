class TV:
    def __init__(self, tamanho) -> None:
        self.__volume = 50
        self.__canal = 1
        self.__tamanho = tamanho
        self.__ligada = False

    def aumentar_volume(self):
        if self.__volume < 99:
            self.__volume += 1
        print(f"Volume: {self.__volume}")

    def diminuir_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
        print(f"Volume: {self.__volume}")

    def modificar_canal(self, canal):
        if canal <= 1 or canal >= 99:
            raise ValueError("Canal indisponível")

        self.__canal = canal
        print(f"Canal: {self.__canal}")

    def ligar_desligar(self):
        self.__ligada = not self.__ligada
        print("Ligada" if self.__ligada else "Desligada")
