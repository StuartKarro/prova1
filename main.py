saldo = 0
menu = 0
print("bem-vindo")
while menu != 4:
    menu = int(input("Digite 1 para consultar o saldo \n"
                 "Digite 2 para saque \n"
                 "Digite 3 para depósito \n"
                 "Digite 4 para sair"))

    if menu == 1:
        print(float(saldo))
    elif menu == 2:
        saque = float(input("Digite o valor do saque"))
        if saque > saldo:
            print("saldo indisponivel")
        else:
            saldo = saldo - saque
            print(float("saldo"))
    elif menu == 3:
        deposito = float(input("Digite o valor do deposito"))
        saldo = saldo + deposito
        print(saldo)






