# Exercício 04 - Cálculo da área de um retângulo com f-string
#
# Peça para o usuário digitar a largura e a altura de um retângulo.
# Calcule a área (largura * altura) e exiba o resultado usando f-string.
#
# Exemplo de saída:
# A área do retângulo de largura 5.0 e altura 3.0 é 15.00.
largura = float(input("Digite a largura do retângulo:"))
altura = float(input("Digite a altura do retângulo:"))

area = largura * altura 
print(f"A área do retângulo de largura {largura:.1f} e altura {altura:.1f} é {area:.2f}")