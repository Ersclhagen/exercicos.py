# Crie um programa que simule um **boletim escolar**.
# O usuário deverá digitar:
# - O nome do aluno
# - A primeira nota (0 a 10)
# - A segunda nota (0 a 10)

# O programa deve calcular a **média** entre as duas notas
# e exibir uma **mensagem personalizada**, de acordo com a média final:
# 
# Se média < 5: REPROVADO
# Se média >= 5 e < 7: RECUPERAÇÃO
# Se média >= 7 e < 9: APROVADO
# Se média >= 9: APROVADO COM HONRA

# Exemplo de saída:
# Aluno: Gustavo | Média: 8.5 | Situação: APROVADO

nome = input("Digite o nome do aluno: ")
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))                        

media = (primeira_nota + segunda_nota) / 2


if media < 5:
    situacao = "reprovado!"
elif 5 <= media < 7:
    situacao = "recuperação!"
elif 7 <= media < 9:
    situacao = "aprovado!"
else:
    situacao = "aprovado com honra!"

print(f"Aluno: {nome} | Média: {media:.1f} | Situação: {situacao.upper()} ") 

