resposta = "Ss"
qnt = 0
num = 0
maior = 0
menor = 0
while resposta in "Ss" :
    num = int(input("Digite um numero: "))
    qnt += 1
    if qnt == 1:
         maior = menor = num
    else:
        if num> maior:
            maior = num
        if num< menor:
            menor = num
    resposta = str(input("Quer continuar [S/N]: ")).upper().strip()
media = num /qnt
print(f"""Vc digitou {qnt} numeros a media entre eles foi {media:.1f} 
o maior foi {maior} e o menor {menor}""")