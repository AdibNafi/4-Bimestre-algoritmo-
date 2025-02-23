import math

num = int(input("Digite um número inteiro: "))

if num >= 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada de {num} é: {raiz:.2f}")
else:
    print("Número inválido! Não é possível calcular a raiz quadrada de um número negativo.")
