# exercicio_07_var_01_idade_categoria.py
# Perguntar a idade e dizer se a pessoa está na infância, adolescência, adulto ou terceira idade.

idade = int(input("Digite uma idade: "))

if idade < 12:
    classificacao = "criança!"
elif 12 <= idade < 18:
    classificacao = "Adolescente!"
elif  18 <= idade < 60:
    classificacao = "Adulto!" 
else:
    classificacao = "Terceira idade!"            
print(f"Você está na {classificacao}: {idade} anos.")    