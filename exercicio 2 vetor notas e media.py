'''
crie um vetor chamado aluno p/conter o nome de 8 alunos.
crie um vetor chamado nota p/conter a nota de 8 alunos.
para cada aluno leia o nome e a nota. Só aceite notas númericas reais entre 0
e 10(use tratamento de exceção).
calcule a media das notas dos 8 alunos.
depois mostre o nome, a nota e marque com * os alunos com nota acima da media
'''
aluno=[None]*8
nota=[0]*8
for x in range(8):
    aluno[x]=input(f'Digite o nome do {x+1}° aluno: ')
    while True:
        try:
            nota[x]=float(input(f'Digite a nota do {aluno[x]}: '))
            if nota[x]>=0 and nota[x]<=10:
                break
            else:
                print('valor invalido!\nO valor deve estar entre 0 e 10!')
                
        except ValueError:
             print('O valor deve ser numérico')
soma=0
for x in range(8):
    soma+=nota[x]
media=soma/8
print('A media das notas é de',media)
print('Nome          Notas  Acima da media')
for x in range(8):
    print(f'{aluno[x]:12} {nota[x]:5.1f}', end='')
    if nota[x]>=media:
        print(f"{'*':>8}")
    else:
        print()




    
