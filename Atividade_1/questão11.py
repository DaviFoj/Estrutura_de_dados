palavra =input("Digite uma palavra: ")

for palimdromo in palavra:
    if palavra == palavra [::-1]:
        print(f"A palavra '{palavra}' é um palíndromo")
        break
    else:
        print(f"A palavra '{palavra}' não é um palíndromo")
        break