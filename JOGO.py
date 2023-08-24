from time import sleep
import random

opcoes = int(input("""Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL 
[ 2 ] TESOURA
Qual é a sua jogada? """))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

lista = ("Pedra", "Papel", "Tesoura")
escolhido = random.choice(lista)
print("-=-"*20)
print(f"O computador escolheu {escolhido}")
if opcoes == 0:
    print("E o jogador escolheu Pedra")
elif opcoes == 1:
    print("E o jogador escolheu Papel")
elif opcoes ==2:
    print("E o jogador escolheu Tesoura")
print("-=-" * 20)

if opcoes == 0 and escolhido == "Pedra":
    print("Ngm ganhou")
elif opcoes == 0 and escolhido == "Papel":
    print(" O Computador venceu")
elif opcoes == 0 and escolhido == "Tesoura":
    print("O Jogador Venceu")
elif opcoes == 1 and escolhido == "Pedra":
    print("O Computador Venceu")
elif opcoes == 1 and escolhido == "Papel":
    print("Ngm ganhou")
elif opcoes == 1 and escolhido == "Tesoura":
    print("O Computador Venceu")
elif opcoes == 2 and escolhido == "Pedra":
    print("O computador venceu")
elif opcoes == 2 and escolhido == "Papel":
    print("O Jogador Venceu")
elif opcoes == 2 and escolhido == "Tesoura":
    print("Ngm ganhou")