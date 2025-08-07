def classificar_aluno(nome, nota1, nota2):
    media = (nota1 + nota2) / 2

    if media < 5:
        classificacao = "reprovado!"
    elif 5 <= media < 7:
        classificacao = "recuperação!"
    elif 7 <= media < 9:
        classificacao = "parabéns, você passou!"
    else:
        classificacao = "passou com honra!"

    return f"Aluno: {nome.title()} | Média: {media:.1f} | Classificação: {classificacao.upper()}"
print(classificar_aluno("gustavo", 8, 9))