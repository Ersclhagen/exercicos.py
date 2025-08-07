# Exercício 05 - Conversão de temperatura com input e f-string
# Peça para o usuário digitar a temperatura em Celsius e converta para Fahrenheit.

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"{celsius}°C equivalem a {fahrenheit:.2f}°F.")