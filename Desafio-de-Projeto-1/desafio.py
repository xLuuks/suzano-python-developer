saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("\n====== MENU ======")
    print("[1] Depositar")
    print("[2] Sacar")
    print("[3] Extrato")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("❌ Operação falhou! O valor do depósito deve ser positivo.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("❌ Operação falhou! Saldo insuficiente.")
        elif valor > limite:
            print("❌ Operação falhou! Valor do saque excede o limite de R$ 500,00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("❌ Operação falhou! Número máximo de saques diários atingido.")
        elif valor <= 0:
            print("❌ Operação falhou! Valor inválido para saque.")
        else:
            saldo -= valor
            extrato += f"Saque:    R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")

    elif opcao == "3":
        print("\n====== EXTRATO ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=====================")

    elif opcao == "0":
        print("🏁 Encerrando o sistema bancário... Até logo!")
        break

    else:
        print("❌ Opção inválida. Escolha uma opção válida.")
