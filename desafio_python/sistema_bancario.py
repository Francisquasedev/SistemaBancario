# Sistema Bancário Versão 1.0

# Inicializando variáveis de saldo e contadores de depósitos e saques
saldo = 0
qtd_dep = 0
qtd_saque = 0

while True:
    # Exibindo o menu inicial e solicitando uma escolha  do usuário
    menu_inicial = int(input('''Escolha uma das opções:
    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
    ''')) 

    # ÍNICIO DEPÓSITO
    if menu_inicial == 1:
        print("Você escolheu a opção Depósito.")
        deposito = float(input("Informe o valor que será depositado: "))
        if deposito > 0:
            # Realizando o depósito se o valor for positivo
            print("Depósito realizado com sucesso!")
            saldo += deposito
            print(f"Valor depositado: R$ {deposito:.2f}")
            print(f"Saldo: R$ {saldo:.2f}")
            qtd_dep += 1
        else:
            print("Valor informado é inválido.")
    # FIM DEPÓSITO
            
    # ÍNICIO SAQUE
    elif menu_inicial == 2:
        print("Você escolheu a opção Saque.")
        while qtd_saque < 3:
            saque = float(input("Informe o valor que gostaria de sacar: "))
            if saque > 500:
                print("Valor máximo permitido é de 500.")
                continue
            if saque > saldo:
                print("Saldo insuficiente.")
                continue
            # Realizando o saque se o valor estiver dentro dos limites
            saldo -= saque
            print("Saque realizado com sucesso!")
            print(f"Valor do saque: R$ {saque:.2f}")
            print(f"Saldo: R$ {saldo:.2f}")
            qtd_saque += 1
    # FIM SAQUE

    # ÍNICIO EXTRATO
    elif menu_inicial == 3:
        print("Você escolheu a opção Extrato.")
        print("Visualizar Extrato")
        if qtd_saque != 0 and qtd_dep != 0:
            # Exibindo informações do extrato se houver movimentações na conta
            print(f"Saques realizados: {qtd_saque}")
            print(f"Depósitos realizados: {qtd_dep}")
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("Não foram realizadas movimentações na conta.")
    # FIM EXTRATO

    # SAIR 
    elif menu_inicial == 0:
        print("Você escolheu a opção Sair.")
        print("Obrigado por usar este sistema. Até mais!!!")
        break
