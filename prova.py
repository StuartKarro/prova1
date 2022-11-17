1)
def fazerlista(tamanho):
    lista = list()
    for l in range(tamanho):
        lista.append(0)
    return lista


tamanho = int(input('Insira o tamanho da lista'))
lista = fazerlista(tamanho)
for l in range(len(lista)):
    numero = int(input("Insira um número da lista: "))
    lista[l] = numero

ordem = sorted(lista)
soma = sum(lista)
maiornumero = max(lista)

print("Lista.", lista)
print(" lista ordenada.", ordem)
print("A soma dos valores.", soma)
print("O maior número da lista.", maiornumero)

2)
dado = [1,2,3,4,5,6]
player1 = list()
player2 = list()
verificar = 0
from random import  randint


while True:
    opcao = int(input("[ 1 ] - Jogar [ 2 ] - Sair \nDigite 1 para jogar e 2 para sair: "))

    if opcao == 1:
        if verificar % 2 == 0:
            player1.append(dado[randint(0,5)])
            print("Número do Player1:",(player1[-1]))
            verificar += 1
        
        else:
            player2.append(dado[randint(0,5)])
            print("Número do Player2",(player2[-1]))
            verificar += 1
            
    else:
        if verificar % 2 != 0:
            player2.append(dado[randint(0, 5)])
            print("Último número do jogador 2", (player2[-1]))
        break

soma = sum(player1)
soma1 = sum(player2)
print("\nResultados: ")
print("Jogadas do jogador 1:", player1)
print("Jogadas do jogador 2:", player2)
print("Soma dos valores do jogador 1:", soma)
print("Soma dos valores do jogador 2:", soma1)
if sum(player1) > sum(player2):
    print("O jogador 1 é o vencedor")
else:
    print("O jogador 2 é o vencedor")
print("Obrigada por Jogar!")


3)
def fazermatriz(linha, coluna):
    lista = list()
    for i in range(linha + 1):
        lista.append([0] * coluna)
    return lista


linha = int(input("Digite o número de linhas:"))
coluna = int(input("Digite o número de colunas: "))
matriz = fazermatriz(linha, coluna)
contador = 0

for l in range(linha):
    for c in range(coluna):
        contador += 1
        indices = linha * coluna
        numero = int(input("Digite", indices, "numeros"))
        matriz[l][c] = numero
  



4)
linha = 5
coluna = 5

def fazermatriz(linha, coluna):
    lista = list()
    for i in range(linha + 1):
        lista.append([0] * coluna)
    return lista


matriz = fazermatriz(linha, coluna)


for l in range(linha):
    for c in range(coluna):
        if l == c:
            matriz[l][c] = 1

for i in range(linha):
    print(matriz[i])
