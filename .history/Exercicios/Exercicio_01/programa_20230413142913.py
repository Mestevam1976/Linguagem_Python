import math # para usar a raiz quadrada
# Problema do Retângulo

comprimento = float(input("===========DADOS DO RETÂNGULO===========\nDigite o valor do comprimento do retângulo: "))
largura = float(input("Digite o valor da largura do retângulo: "))

area = comprimento * largura

perimetro = 2 * (comprimento + largura)

diagonal = math.sqrt(pow(comprimento, 2) + pow(largura, 2))

print(f"A área do retângulo digitado é {area:.2f}, o perímetro é igual a {perimetro:.2f} e a diagonal é igual a {diagonal:.2f}")