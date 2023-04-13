# Problema do Retângulo

comprimento = float(input("===========DADOS DO RETÂNGULO===========\n\
                          Digite o valor do comprimento do retângulo: "))
largura = float(input("Digite o valor da largura do retângulo: "))

area = comprimento * largura

perimetro = 2 * (comprimento + largura)

print(f"A área do retângulo digitado é {area:.2f} e o perímetro é igual a {perimetro:.2f}")