def mostrar_menu():
    print("\n=== MENU BANCO ===")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def ver_saldo(saldo):
    print(f"\nSeu saldo atual é: R${saldo:.2f}")

def depositar(saldo):
    valor = float(input("Digite o valor para depositar: R$"))
    if valor > 0:
        saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo

def sacar(saldo):
    valor = float(input("Digite o valor para sacar: R$"))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print(f"Saque de R${valor:.2f} realizado com sucesso!")
    elif valor > saldo:
        print("Saldo insuficiente!")
    else:
        print("Valor inválido para saque.")
    return saldo

saldo = 0.0  # saldo inicial
opcao = 0

while opcao != 4:
    mostrar_menu()
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        print("Entrada inválida. Digite um número de 1 a 4.")
        continue

    if opcao == 1:
        ver_saldo(saldo)
    elif opcao == 2:
        saldo = depositar(saldo)
    elif opcao == 3:
        saldo = sacar(saldo)
    elif opcao == 4:
        print("Saindo do sistema. Até logo!")
    else:
        print("Opção inválida. Tente novamente.")
