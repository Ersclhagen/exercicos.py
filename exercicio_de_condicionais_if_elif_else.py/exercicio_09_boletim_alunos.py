# Crie um programa que simule um boletim escolar para múltiplos alunos.
# O programa deve:
# 1. Perguntar quantos alunos serão cadastrados.
# 2. Para cada aluno, solicitar:
#    - Nome
#    - Primeira nota (de 0 a 10)
#    - Segunda nota (de 0 a 10)
# 3. Calcular a média das duas notas.
# 4. Classificar o aluno de acordo com a média:
#    - Média < 5       → Reprovado
#    - 5 <= Média < 7  → Recuperação
#    - 7 <= Média < 9  → Aprovado
#    - Média >= 9      → Aprovado com honra
# 5. Exibir os resultados individuais no formato:
#    Aluno: NOME | Média: X.X | Classificação: XXXXXXX | Feedback: XXXXXXXX
#
# Extras opcionais:
# - Validar se as notas estão entre 0 e 10.
# - Exibir no final um resumo com total de aprovados, recuperação e reprovados

quantos_alunos_cadastrados = int(input("Digite quantos alunos serão cadastrados:"))
nome = input("Digite o nome: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
media = (primeira_nota + segunda_nota) / 2

if media < 5:
    classificacao = "reprovado!"
    feedback = "Não foi dessa vez"
elif 5 <= media < 7:
    classificacao = "recuperação!"
    feedback = "Você ainda tem uma chance"
elif 7 <= media < 9:
    classificacao = "aprovado!"
    feedback = "Parabéns você passou"
else:
    classificacao = "aprovado com honra!"
    feedback = "Sua dedicação merece reconhecimento"

print(f"Nome: {nome.tittle()} | Média: {media:.1f} | Classificação: {classificacao.upper()} | Feedback: {feedback}")

