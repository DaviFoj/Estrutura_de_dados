n = int(input("Digite um número inteiro: "))

if n <= 1:
    print(f" O número {n} não é primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f" O número {n} não é primo")
            break
    else:
        print(f" O número {n} é primo")