# Exercício 08 - Classificação de Alunos com Função
# 
# Escreva um programa que permita cadastrar a quantidade desejada de alunos.
# Para cada aluno, o usuário deve informar:
# - nome do aluno
# - primeira nota (float)
# - segunda nota (float)
# 
# O programa deve calcular a média e usar uma função chamada `classificar_aluno(media)`
# que retorna a classificação e o feedback com base nas regras:
#
# Média < 5       → "reprovado!", "não foi dessa vez!"
# 5 ≤ média < 7   → "recuperação!", "você ainda tem uma chance!"
# 7 ≤ média < 9   → "parabéns você passou!", "parabéns pelo seu esforço!!"
# Média ≥ 9       → "você passou com honra!", "aluno(a) lendário!!!"
#
# Ao final, exiba um resumo com:
# Nome do aluno (capitalizado), média (com 1 casa decimal),
# classificação (em letras maiúsculas) e feedback (capitalizado).

def classificar_aluno(media):
    if media < 5:
        return "reprovado!", "não foi dessa vez, força!"
    elif 5 <= media < 7:
        return "recuperação!", "tem uma chance!"
    elif 7 <= media < 9:
        return "você passou!", "continue assim!"
    else:
        return "passou com honra!", "mestre jedi!"
    
quantidade_de_alunos = int(input("Digite a quantidade de aluno: "))
for i in range (quantidade_de_alunos):
    print(f"\nCadastro do aluno {i+1}: ")

    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a nota do aluno: "))
    nota2 = float(input("Digite a nota do aluno: "))
    media = (nota1 + nota2) / 2
    classificacao, feedback = classificar_aluno(media)

    print(f"Aluno {nome.title()} | Média: {media:.1f} | Classificação: {classificacao.upper()} | Feedback: {feedback.capitalize()} ")
    
    
    