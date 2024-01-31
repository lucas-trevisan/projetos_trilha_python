menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("\nDigite o valor do depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito de R${valor:.2f}\n"
            print(f"\n => Deposito no valor de R${valor:.2f} Realizado com sucesso.")

    elif opcao == "s":
        valor = float(input("\nDigite o valor a ser sacado:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
  
        if excedeu_saldo:
            print("\nVocê não tem saldo o suficiente")
       
        elif excedeu_limite:
            print(f"\nValor do saque superior ao limite, seu limite de saque é: R${limite:.2f}")

        elif excedeu_saques:
            print("\nVocê excedeu seu limite diario de saques")

        elif valor > 0:
            saldo -= valor
            numero_saques += 1
            extrato += f"Saque de R${valor:.2f}\n"
            print(f"\nVocê sacou R${valor:.2f}")
        
        else:
            print("Valor informado invalido, tente novamente")

            

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
       

    elif opcao == "q":
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")