# 📐 Exercício 04 — Calculadora de Área de um Retângulo
#
# Crie um programa que:
# 1. Armazene em variáveis os valores:
#    - largura de um retângulo (em metros) 
#    - altura do retângulo (em metros)
#
# 2. Calcule a área do retângulo usando a fórmula:
#    área = largura * altura
#
# 3. Exiba no terminal:
#    - A largura
#    - A altura
#    - A área total
#
# Observações:
# - Não use input() nem f-string.
# - Use apenas print() com vírgulas.
# - Os valores podem ser decimais.
# - Use um cabeçalho como "=== Cálculo da Área ==="

largura_retangulo = 5.0
altura_retangulo = 3.0
area = largura_retangulo * altura_retangulo

print("=== Cálculo da Área ===")

print("Largura do Retângulo:", round(largura_retangulo, 2))
print("Altura do Retângulo:", round(altura_retangulo, 2))
print("Área Total:", round(area, 2), "metros quadrados")