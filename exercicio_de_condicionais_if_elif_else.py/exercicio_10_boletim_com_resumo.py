# Exercício 10 - Cadastro de alunos com classificação e resumo final
# ------------------------------------------------------------
# Objetivo: Criar um sistema para cadastrar alunos e calcular a média de duas notas.
# Para cada aluno, exibir:
# - Nome
# - Média das notas
# - Classificação (reprovado, recuperação, aprovado, aprovado com honra)
# - Feedback personalizado
#
# Bônus:
# 1. Validar se as notas estão entre 0 e 10.
# 2. Repetir o processo para N alunos.
# 3. Mostrar um resumo final com:
#    - Total de alunos aprovados
#    - Total em recuperação
#    - Total de reprovados
#Aluno: NOME | Média: X.X | Classificação: XXXXXXX | Feedback: XXXXXXXX

nome = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: ")) 
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    classificacao = "reprovado!"
    feedback = "não foi dessa vez"
elif 5 <= media < 7:
    classificacao = "recuperação!" 
    feedback = "você ainda tem uma chance"
elif 7 <= media < 9:
    classificacao = "aprovado!"
    feedback = "parabéns você passou"
else:
    classificacao = "aprovado com honra!"
    feedback = "você teve um ótimo desempenho!!!"

print(f"Aluno: {nome} | Média: {media:.1f} | Classificação: {classificacao.upper()} | Feedback: {feedback.title()}")
