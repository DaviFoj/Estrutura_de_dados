palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"

for vogal in vogais:
    if vogal in palavra:
        print(f"A letra '{vogal}' está presente na palavra '{palavra}'")