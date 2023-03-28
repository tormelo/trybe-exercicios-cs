import json
import random


def get_random_pokemon_name(pokemon_list):
    return random.choice(pokemon_list)["name"]


if __name__ == "__main__":
    with open("exercicios-bonus/pokemons.json") as file:
        pokemon_list = json.load(file)["results"]

    pokemon = get_random_pokemon_name(pokemon_list)

    for attempt in range(len(pokemon)):
        hint = pokemon[0:attempt] + ("-" * (len(pokemon) - attempt))
        user_input = input(f"Quem é esse pokemon? {hint}\n")
        if user_input.lower() == pokemon.lower():
            print("Você acertou!")
            break
        if attempt == len(pokemon) - 1:
            print("Você perdeu!")
