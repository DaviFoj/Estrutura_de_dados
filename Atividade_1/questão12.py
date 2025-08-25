senha = "python123"
tentativas = 2

def verificar_senha(senha):
    entrada = input("Digite a senha: ")
    if senha == entrada:
        return "Senha correta."
    else:
        return "Senha incorreta."

def validar_senha(senha):
    if verificar_senha(senha) == "Senha correta.":
        return "Acesso concedido."
    else:
        return "Acesso negado."
    
for tentativa in range(tentativas + 1):
    resultado = validar_senha(senha)
    if resultado == "Acesso concedido.":
        print(resultado)
        break
    else:
        print(f"{resultado} Você tem mais {tentativas - tentativa} tentativas.")
        if tentativa == tentativas:
            print("Número máximo de tentativas atingido. Acesso bloqueado.")