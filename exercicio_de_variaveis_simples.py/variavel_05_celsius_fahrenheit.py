# Exercício 05 - Conversão de temperatura
# Peça para o usuário digitar uma temperatura em Celsius e converta para Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F.")