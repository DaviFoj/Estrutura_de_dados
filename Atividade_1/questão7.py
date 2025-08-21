n = int(input("Digite um número inteiro positivo: "))
i = 0
resultado = i

for i in range(1, n + 1):
    resultado += i
print(f"A soma dos números de 1 até {n} é: {resultado}")

