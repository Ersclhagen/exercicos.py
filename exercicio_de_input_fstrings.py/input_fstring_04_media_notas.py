# Exercício 04 - Média de notas com input e f-string
# Peça para o usuário digitar três notas e calcule a média.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"A média das notas {nota1}, {nota2} e {nota3} é {media:.2f}")