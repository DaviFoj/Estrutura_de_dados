senha = input("digite sua senha: ")
i = 0

while True:
    if len(senha) <= 8:
        print("Senha muito curta, digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.isalpha():
        print("Senha deve conter números, digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.isdigit():
        print("Senha deve conter letras, digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.islower():
        print("Senha deve conter letras maiúsculas, digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.isupper():
        print("Senha deve conter letras minúsculas, digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.count('@') != 1:
        print("Senha deve conter exatamente um '@', digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.count('#') != 1:
        print("Senha deve conter exatamente um '#', digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    elif senha.count('$') != 1:
        print("Senha deve conter exatamente um '$', digite novamente")
        senha = input("digite sua senha: ")
        i += 1
    else:
        print("Senha válida")
        break
        

