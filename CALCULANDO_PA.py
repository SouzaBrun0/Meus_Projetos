print("Gerador de PA")
print("-="*10)
primeiro = int(input("Primeiro termo: "))
razão = int(input("Razão: "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razão   #resultado
        cont +=1  #contador
    print("Pausa")
    mais = int(input("Quantos termos vc quer ver a mais? (0 para sair): "))
print(f"Fim do programa com {total} termos mostrado")