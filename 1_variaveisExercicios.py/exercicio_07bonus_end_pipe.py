# ➕ Exercício Bônus — Impressão Horizontal com `end=" | "`
#
# Crie 3 ou mais variáveis com dados simples (ex: nome, idade, cidade, profissão, etc.).
# Use o comando print() para exibir todas essas informações em uma única linha, separadas por " | ".
#
# Regras:
# - Não use f-string nem input()
# - Use apenas print() com vírgulas e o parâmetro `end=" | "` para formatar a saída horizontalmente.

nome = "luiz gustavo"
idade = 25
cidade = "votorantim"
profissao = "Programador Junior"
salario = 5500.79

print("=== end= ===")
print("Meu nome é:", nome.title(), end="|")
print("\tEu tenho:", idade, "anos", end="|")
print("\tMoro em:", cidade.capitalize(), end="|")
print("\tTrabalho como:", profissao.upper(), end="|")
print("\tMeu salário é de:", round(salario, 2))