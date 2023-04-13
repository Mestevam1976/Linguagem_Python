x: int
y: float

b1, b2, h = 10.2,24.5, 15.3
area = ((b1 + b2) / 2) * h

x = 5
y = 2
nome = 'Maria'
idade = 19
salario = 4550.4567
sexo = 'F'

print("A funcionária %s tem %d anos e tem salário de %.2f" %(nome,idade,salario))
print("{:.3f}".format(salario))
print(f"A funcionária {nome}, sexo {sexo}, ganha {salario:.2f} e tem {idade} anos")
print(x)
print(y)
print(area)