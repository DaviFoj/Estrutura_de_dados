password = input("Digite a senha: ")

if password.count("@") < 1 or password.count("#") < 1 or password.count("$") < 1 and len(password) < 8:
    print("Senha valida")
else:
    print("Senha invalida")


