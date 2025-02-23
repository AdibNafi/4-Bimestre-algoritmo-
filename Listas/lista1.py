"""
A QUANTIDADE DE NUMEROS NEGATIVOS 
A SOMA DOS NUMEROS POSITIVOS
"""


numero = []
  
for i in range(10):   
    numerounitaria = float(input("Digite a nota do aluno: "))   
    numero.append(numerounitaria)
quantidade_negativos = 0
soma_positivos = 0 
for numerounitaria in numero:
    if numerounitaria <0 :
        quantidade_negativos += 1 
    if numerounitaria > 0 : 
        soma_positivos += numerounitaria
print(f"quantidade de numeros negativos: {quantidade_negativos}, e a soma dos positivos é :{soma_positivos}")
