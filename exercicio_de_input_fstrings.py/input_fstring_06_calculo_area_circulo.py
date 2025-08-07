# Exercício 06 - Cálculo da área do círculo com input e f-string
# Peça para o usuário digitar o raio do círculo e calcule a área.

raio = float(input("Digite o raio do círculo (em metros): "))
pi = 3.14159
area = pi * (raio ** 2)
print(f"A área do círculo de raio {raio} metros é {area:.2f} metros quadrados.")