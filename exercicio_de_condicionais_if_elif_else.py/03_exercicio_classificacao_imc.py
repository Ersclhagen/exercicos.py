# Exercício 03 - Classificação do IMC
# Entrada:
#   - Solicite o peso (em kg)
#   - Solicite a altura (em metros)
# Processamento:
#   - Calcule o IMC com a fórmula: IMC = peso / (altura ** 2)
#   - Classifique o resultado:
#       - IMC abaixo de 18.5 → "Abaixo do peso"
#       - IMC entre 18.5 e 24.9 → "Peso normal"
#       - IMC entre 25 e 29.9 → "Sobrepeso"
#       - IMC entre 30 e 39.9 → "Obesidade"
#       - IMC 40 ou mais → "Obesidade grave"
# Saída:
#   - Mostre o valor do IMC e a classificação correspondente 

peso = float(input("Digite o seu peso: ")) 
altura = float(input("Digite a sua altura: ")) 
imc = peso / (altura ** 2) 

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif 18.5 <= imc <= 24.9:
    classificacao = "Peso normal"
elif 25 <= imc <= 29.9:
    classificacao = "Sobrepeso"
elif 30 <= imc <= 39.9:
    classificacao = "Obesidade"
else:
    classificacao = "Obesidade grave"
    
print(f"Seu imc é {imc:.2f} | classifação:{classificacao}")