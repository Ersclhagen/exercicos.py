# Crie um programa que solicite:
# - o nome do aluno
# - duas notas (valores de 0 a 10)
# O programa deve calcular a média e:
# - classificar o aluno como:
#   * REPROVADO (média < 5)
#   * RECUPERAÇÃO (5 <= média < 7)
#   * APROVADO (7 <= média < 9)
#   * APROVADO COM HONRA (média >= 9)
# Além disso, o programa deve exibir um FEEDBACK personalizado com base na média:
# - Se reprovado: "É hora de revisar os conteúdos e tentar de novo!"
# - Se em recuperação: "Você está quase lá, continue estudando!"
# - Se aprovado: "Parabéns! Continue assim!"
# - Se aprovado com honra: "Excelente desempenho! Você brilhou!"

# Exemplo de saída:
# Aluno: João | Média: 8.5 | Situação: APROVADO
# Feedback: Parabéns! Continue assim!
nome = input("Digite um nome: ")
primeira_nota =  float(input("Digite a priemira nota (0 a 10):"))
segunda_nota  =  float(input("Digite a segunda nota (0 a 10):"))

media = (primeira_nota + segunda_nota) / 2

if media < 5:
    classificacao = "reprovado!"
    feedback = "É hora de revisar os conteúdos e tentar de novo!"
elif 5 <= media < 7:
    classificacao = "recuperação!"
    feedback = "Você está quase lá, continue estudando!"
elif 7 <= media < 9:
    classificacao = "aprovado!"
    feedback = "Parabéns! Continue assim!"
else:
    classificacao = "aprovado com honra!"
    feedback = "Excelente desempenho! Você brilhou!"

print(f"Aluno: {nome} | Média: {media:.1f} | Classificação: {classificacao.upper()}")
print(f"FeedBack: {feedback}")



