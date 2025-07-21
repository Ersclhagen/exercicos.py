print("=== calculadora de IMC ===")

nome = input("Digite o seu nome completo:")
altura = float(input("Digite a sua altura em metros:"))
peso = float(input("Digite o seu peso em Kg:"))
imc = peso / altura ** 2


print("\n === Resultado ===")
print(f"\tNome:\t\t{nome}")
print(f"\tAltura:\t\t{altura:.1f}m")
print(f"\tPeso:\t\t{peso:.1f}")
print(f"\tIMC:\t\t{imc:.2f}")

