






quantidade_alunos = int(input("Digite a quantidade de alunos que deseja cadastrar: "))

for i in range(quantidade_alunos):
    print(f"\nCadastro do Aluno {i+1}: ")
    
    nome = input("Digite o nome do aluno: ")
    primeira_nota = float(input("Digite a primeira nota: "))
    segunda_nota = float(input("Digite a segunda nota: "))
    media = (primeira_nota + segunda_nota) / 2

    if media < 5:
        classificacao = "reprovado!"
        feedback = "não foi dessa vez!"
    elif 5 <= media < 7:
        classificacao = "recuperação!"
        feedback = "você ainda tem uma chance!"
    elif 7 <= media < 9:
        classificacao = "parabéns você passou!"
        feedback = "parabéns pelo seu esforço!!"
    else:
        classificacao = "você passou com honra!"
        feedback = "aluno(a) lendario!!!"

    print(f"Nome do aluno: {nome.title()} | Média: {media:.1f} | Classificação: {classificacao.upper()} | Feedback: {feedback.capitalize()}")