import random

word = random.choice(["banana", "melancia", "laranja"])
scrambled_word = "".join(random.sample(word, len(word)))

for attempt in range(3):
    user_input = input(
        f"Tentativa {attempt + 1}/3: Que palavra é essa? {scrambled_word}\n"
    )
    if user_input == word:
        print("Você acertou!")
        break
    if attempt == 2:
        print("Você perdeu!")
