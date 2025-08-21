n = int(input("Digite um número inteiro: "))

for i in range(1, n + 1):
    if i % 3 == 0:
        print(f"{i} é múltiplo de 3")