# 🕒 Exercício 05 — Conversão de Minutos para Horas
#
# Crie um programa que:
# 1. Crie uma variável chamada `minutos` com um valor inteiro representando um tempo qualquer.
# 2. Crie outra variável chamada `horas`, que represente esse tempo convertido para horas.
#    (A fórmula é: horas = minutos / 60)
# 3. Exiba os dois valores usando apenas `print()` com vírgulas (sem f-string).
# 4. Mostre o resultado com até 2 casas decimais (dica: use `round()`).
# 5. Adicione um cabeçalho visual com print().

minutos = 20
horas = 60

horas = minutos / 60

print("=== Conversão de minutos p/ horas ===")
print("Minutos:", minutos)
print("Tempo convertido de minutos para horas:", round(horas, 2), "horas")
