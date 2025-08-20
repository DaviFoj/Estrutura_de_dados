ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto")
else:
    print(f"{ano} não é um ano bissexto")
    print("O próximo ano bissexto é", ano + (4 - ano % 4) if ano % 4 != 0 else ano + 4)