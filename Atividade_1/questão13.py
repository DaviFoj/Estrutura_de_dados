sair = ["sair", "Sair", "SAIR"]

while sair not in sair:
    hora = int(input("Digite a hora (0-23): "))
    sair = input("Digite 'sair' para encerrarsa: ")

    if 0 <= hora <= 11:
        print("Bom dia!")
    elif 12 <= hora <= 17:
        print("Boa tarde!")
    elif 18 <= hora <= 23:
        print("Boa noite!")
    else:
        print("Hora inválida. Por favor, digite um valor entre 0 e 23.")