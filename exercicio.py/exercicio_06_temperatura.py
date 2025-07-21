# Exercicio 06 - Conversor de temperatura
# Peça ao usuário a temperatura em graus Celsius.
# Converta para Fahrenheit usando a fórmula:
# Fahrenheit = (Celsius × 1.8) + 32
# Mostre o resultado com a frase:
# "30 graus Celsius equivalem a 86 graus Fahrenheit."

temperatura_celcius = float(input("Digite a temperatura em graus celsius:")) 

fahrenheit = (temperatura_celcius * 1.8) + 32
print(f"{temperatura_celcius} equivalem a {fahrenheit:.2f}")

