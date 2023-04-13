salario1: float; salario2: float
nome1: str; nome2: str
idade: int
sexo: str

nome1 = input("Nome da primeira pessoa: ")
salario1 = float(input("Salário da primeira pessoa: "))

nome2 = input("Nome da segunda pessoa: ")
salario2 = float(input("Salário da segunda pessoa: "))

idade = int(input("Favor informar uma idade: "))
sexo = input("Favor informar o Sexo (M/F): ")

print(f"Nome da primeira pessoa: {nome1}")
print(f"Salario da primeira pessoa: {salario1:.2f}")
print(f"Nome da segunda pessoa: {nome2}")
print(f"Salario da segunda pessoa: {salario1:.2f}")
