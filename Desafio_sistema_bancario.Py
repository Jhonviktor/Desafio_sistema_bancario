menu =  """
============================= BANCO PYTHON DESAFIO =============================

=========== MENU ===========

ESCOLHA A SUA OPERAÇÃO:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
"""

saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0 
LIMITE_DIARIO = 3


while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("Deposito")
        valor = float(input("Deposite o valor desejado: "))
        
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'
        else:
            print("Falha na operação, valor informado não é compatível ou inválido.")
    
    
    elif opcao == 's':
        valor = float(input('Informe o valor que deseja sacar: '))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite_saque
        
        excedeu_saques = numero_saques >= LIMITE_DIARIO
        
        if excedeu_saldo:
            print('Falha na operação, saldo insuficiente para transação!')
        
        elif excedeu_limite:
            print('Falha na operação, o valor excedido.')
       
        elif excedeu_saques:
            print("Falha na operação, número máximo de saques diários atingidos.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            
        else:
            print("Falha na operação, o valor informado é inválido.")
    
    
    elif opcao == 'e':
        print("\n ========================= EXTRATO =========================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print("===============================================")
    
    elif opcao == 'q':
        print("Saindo.")
        break
    
    
    else:
        print("Operação inválida, por favor selecionar novamente a operação desejada.")
        