1)
valor1 = int(input("Digite um valor"))
valor2 = int(input("Digite outro valor"))
valor3 = int(input("Digite outro valor"))
if valor1 > valor2 and valor1 > valor3:
    print(valor1)
elif valor2 > valor1 and valor2 > valor3:
    print(valor2)
else:print(valor3)

2)
idade = int(input("Digite a sua idade"))
tempoTrabalho = int(input("Digite o tempo de trabalho em anos"))

if idade >= 65:
    print("Pode se aposentar")
elif idade < 65 and tempoTrabalho >= 25:
    print("Pode se apresentar")
elif tempoTrabalho >= 30:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")

3)
import random
import string
contador = 0
letra = random.choice(string.ascii_letters)
print("Você tem apenas 5 chances para adivinhar a letra")
while contador <= 4:
    chance = input("Digite uma letra")
    if chance == letra:
        print("Acertou")
    else:
        contador = contador +1
print("Você não acertou, a letra era",letra)

4)
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
