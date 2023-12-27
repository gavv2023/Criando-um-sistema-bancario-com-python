menu = '''

[d] depositar
[s] sacar
[e] extrato
[q] sair

=> '''

saldo = 0
limite = 500
extrato = "Número de operação      Tipo        Valor\n"
numero_saques = 0
LIMITE_SAQUES = 3
contador = 0

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito = float(input("Informe o valor do seu depósito: "))
        while deposito < 0:
            deposito = float(input("Operação falhou! Digite um valor de depósito válido: "))
        saldo += deposito 
        contador += 1
        extrato += f"         {contador}              Depósito    R$ {deposito:.2f}\n"
    elif opcao == "s":
        saque = float(input("Informe o valor do seu saque: "))
        while saque < 0:
            saque = float(input("Operação falhou! Digite um valor de saque válido: "))
        if (saque > saldo):
            print("Operação falhou! Não é possivel realizar a operação por falta de saldo!")
        elif (saque >= limite):
            print("Operação falhou! O valor do saque excede o limite!") 
        elif (numero_saques >= LIMITE_SAQUES):
            print("Operação falhou! Número máximo de saques excedido!")
        else:    
            saldo -= saque 
            numero_saques += 1
            contador += 1
            extrato += f"         {contador}              Saque       R$ {saque:.2f}\n"
    elif opcao == "e":
        print(extrato)
        print()
        print(f"O saldo atual da conta é: R$ {saldo:.2f}")
    elif opcao == "q":
        break
    else:
        print("Operaçâo invalida, por favor selecione novamente a operação desejada.")
