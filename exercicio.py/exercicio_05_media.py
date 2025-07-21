# Exercicio 05 - Calculadora de Média
# Peça para o usuário digitar três notas (valores decimais, com ponto).
# Calcule a média dessas três notas.
# Mostre o resultado com uma frase como:
# "A média das notas 7.5, 8.0 e 6.5 é 7.33"

primeira_nota = float(input("Digite a priemira nota:"))
segunda_nota = float(input("Digite a segunda nota:"))
terceira_nota = float(input("Digite a terceira nota:")) 

media = (primeira_nota + segunda_nota + terceira_nota) / 3

print(f"A média das notas {primeira_nota}, {segunda_nota} e {terceira_nota} é {media:.2f}")