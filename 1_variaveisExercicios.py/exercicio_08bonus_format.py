# 🎯 Exercício Bônus — Formatação com .format()
#
# Crie 5 variáveis:
# - nome_completo
# - idade
# - profissao
# - cidade
# - salario
#
# Depois, use o método `.format()` para exibir essas informações
# em uma única frase bem formatada, sem usar f-strings nem vírgulas no print().
#
# Exemplo esperado de saída:
# Gustavo tem 25 anos, trabalha como Programador e mora em Votorantim. Seu salário é R$ 5500.79.

nome_completo = "luiz gustavo moscatelli de campos"
idade = 25
profissao = "programador junior"
cidade = "votorantim"
salario = 5500.79

print("=== .FORMAT() ===")
mensagem = "{} tem {} anos, trabalha como {} e mora em {}. Seu salário é {:.2f}.".format(
    nome_completo, idade, profissao, cidade, salario
)

print(mensagem)