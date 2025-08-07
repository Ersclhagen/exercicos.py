# Exercício 03 - Preço com desconto usando input e f-string
# Peça para o usuário digitar o preço e o percentual de desconto e calcule o valor com desconto.

preco = float(input("Digite o preço do produto: R$"))
desconto = float(input("Digite o percentual de desconto (%): "))
valor_final = preco - (preco * desconto / 100)
print(f"O preço final com {desconto}% de desconto é R${valor_final:.2f}")