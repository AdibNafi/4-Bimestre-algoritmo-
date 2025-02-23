"""
media geral da turma
"""

nota = []

for i in range(5):
   
    notaunitaria = float(input("Digite a nota do aluno: "))
    
    nota.append(notaunitaria)
    

media = 0 

for no in nota: 
    media = media + no

media = media/5

print (f"media geral: {media}")