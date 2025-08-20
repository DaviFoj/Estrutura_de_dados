num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero: "))
mun3 = int(input("Digite outro numero: "))

if num1 > num2 and num1 > mun3:
    print(f"O maior numero é {num1}")
elif num2 > num1 and num2 > mun3:
    print(f"O maior numero é {num2}")
else:
    print(f"O maior numero é {mun3}")