
"""
lista com 10 valores e onde ta o maior valor
"""

numero =[]

for i in range(10):
   numerosunitario = float(input("digite um número"))
   numero.append(numerosunitario)

posicao = 0

for i in range(10):
    if numero[posicao]< numero[i]:
        posicao=i


print(f"A posição do maior número no vetor é: {posicao}")