"""
As funções nota_partida e redutor tem complexidade O(len(s)), que é a
complexidade da operação de diferença entre conjuntos

A complexidade final da função blefe é O(len(s) + len(t)), devido a criação
de dois sets.
"""


def nota_partida(player, other):
    return max(player - other)


def redutor(player, other):
    return min(player - other)


def blefe(game):
    players = list(game.keys())

    p1set = set(game[players[0]])
    p2set = set(game[players[1]])

    p1points = nota_partida(p1set, p2set) - redutor(p1set, p2set)
    p2points = nota_partida(p2set, p1set) - redutor(p2set, p1set)

    if p1points > p2points:
        return players[0]
    elif p2points > p1points:
        return players[1]
    else:
        return "Empate"


if __name__ == "__main__":
    jogo = {"Clara": [0, 1, 5, 9, 10], "Marco": [0, 2, 8, 9, 10]}
    print(blefe(jogo))
