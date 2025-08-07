# Exercício 04 - Classificação de nota
# Peça para o usuário digitar a nota final de um aluno (de 0 a 10).
# De acordo com o valor, classifique da seguinte forma:
# - Menor que 5: Reprovado
# - De 5 até 6.9: Recuperação
# - De 7 até 8.9: Bom
# - De 9 a 10: Excelente

nota_final = float(input("Digite a nota final (0 a 10): "))

if nota_final < 5:
    classificacao = "reprovado!"
elif 5 <= nota_final <= 6.9:
    classificacao = "recuperação!"
elif 7 <= nota_final <= 8.9:
    classificacao = "passou!"
else:
    classificacao = "passou com excelência!"

print(f"Sua nota {nota_final:.1f} | classificação: {classificacao.upper()}")