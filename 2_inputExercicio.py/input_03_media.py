# Exercício 03 - Média de três números
#
# Peça para o usuário digitar três números (podem ser decimais).
# Calcule a média desses números e exiba o resultado.
#
# Exemplo de saída:
# A média dos números 7.5, 8.0 e 6.5 é 7.33

numero1 = float(input("Digite o primeiro número:"))
numero2 = float(input("Digite o segundo número:"))
numero3 = float(input("Digite o terceiro número:"))

media = (numero1 + numero2 + numero3) / 3
print(f" A média dos números {numero1}, {numero2} e {numero3} é {media:.2f}")