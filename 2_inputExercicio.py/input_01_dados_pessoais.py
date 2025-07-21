# Exercício 01 - Coletando dados pessoais
#
# Peça para o usuário digitar seu nome, idade e cidade onde mora.
# Depois, exiba a seguinte mensagem usando .format():
#
# "Olá, João! Vejo que você tem 30 anos e mora em Belo Horizonte."

nome = input("Digite o seu nome:")
idade = int(input("Digite a sua idade:"))
cidade = input("Digite a cidade de onde mora:")

mensagem = "Olá, {}! Vejo que você tem {} anos e mora em {}.".format(
    nome, idade, cidade
) 
print(mensagem)