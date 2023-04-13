from collections.abc import Iterator
from exercicio2 import Baralho


class IteradorDoBaralhoInverso(Iterator):
    def __init__(self, cartas):
        self._cartas = cartas
        self._pos = -1

    def __next__(self):
        try:
            carta = self._cartas[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos -= 1
            return carta


class BaralhoInverso(Baralho):
    def __iter__(self):
        return IteradorDoBaralhoInverso(self._cartas)
