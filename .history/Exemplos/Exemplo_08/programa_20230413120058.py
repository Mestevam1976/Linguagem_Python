# EStrutura Para (for):
x: int
soma: int

N = int(input("Quantos números serão digitados? "))

soma = 0
for i in range(0,N):
    x = int(input("Digite um número: "))
    soma = soma + x

print(f"A soma é igual a {}")