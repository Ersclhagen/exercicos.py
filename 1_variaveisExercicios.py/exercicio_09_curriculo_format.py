# Exercicio 09 - Currículo formatado
#
# Crie variáveis para:
# - nome
# - idade
# - formação
# - experiência (cargo atual ou anterior)
# - linguagem_favorita
#
# Depois, monte um texto formatado como um mini currículo usando a função `.format()`.
#
# Exemplo de saída:
# João tem 30 anos, é formado em Análise de Sistemas, já atuou como Suporte Técnico,
# e sua linguagem favorita é Python.

nome = "João"
idade = 30
formacao = "Análise de Sistemas"
experiencia = "Suporte Técnico"
linguagem_favorita = "Python"
salario = 4700.89

mensagem = "{} tem {} anos, é formado em {}, experiência com {} e sua linguagem favorita é {} e seu salário é {:.2f}".format(
    nome, idade, formacao, experiencia, linguagem_favorita, salario
) 
print(mensagem)