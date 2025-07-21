# 🎮 Exercício 06 — Dados de um Personagem de Jogo
#
# Crie um programa que armazene em variáveis as seguintes informações sobre um personagem de jogo:
# - nome do personagem
# - classe (ex: guerreiro, mago, arqueiro...)
# - nível (número inteiro)
# - pontos de vida (HP)
# - pontos de mana (MP)
#
# Depois, exiba todos os dados com `print()`, um por linha.
# Use vírgulas (sem f-string), adicione um cabeçalho visual com `print()`
# e explore métodos como `.title()` ou `.upper()` nas strings, se quiser deixar mais bonito.


nome = "ersclhagen fireball"
classe = "Mago"
nivel = 37
hp = 150.47
mp = 300.66

print("=== Dados do Peersonagem ===")
print("\n\tNome do Personagem:", nome.title())
print("\n\tClasse do personagem:", classe.upper())
print("\n\tNível do personagem:", nivel)
print("\n\tPontos de Vida:", round(hp, 2))
print("\n\tPontos de Mana:", round(mp, 2))

