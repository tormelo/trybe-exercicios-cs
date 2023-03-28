name = input("Digite um nome:")

for limit in range(len(name), 0, -1):
    print(name[0:limit])
