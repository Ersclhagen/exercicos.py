def classificar_aluno(media):
    if media < 5:
        return "reprovado!", "faltou com atenção nas aulas"
    elif 5 <= media < 7:
        return "recuperação!", "você ainda tem uma chance de passar"
    elif 7 <= media < 9:
        return "você passou!", "continue assim"
    else:
        return "você passou com honra!", "jovem padawan"
    
    
alunos = []

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

for i in range(quantidade_alunos):
    print(f"\nCadastro do aluno {i+1}: ")

    nome = input("Digite o seu nome: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    classificacao, feedback = classificar_aluno(media)

    aluno = {
    "nome": nome.title(),
    "nota1": nota1,
    "nota2": nota2,
    "media": media,
    "classificacao": classificacao.upper(),
    "feedback": feedback.capitalize(),
}    
    
    
    alunos.append(aluno)

print(f"\nResumo geral dos alunos cadastrados \n")
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} | Média: {aluno['media']:.1f} | Classificação: {aluno['classificacao']} | Feedback: {aluno['feedback']} ")