'''
Crie um vetor de tamanho x, sendo que x será informado pelo usuário
(o valor de x deve estar entre 5 e 20).
Faça tratamento de exceção para este valor.
Preencha este vetor com números inteiros aleatórios gerados automaticamente
pelo programa na faixa de 1 a 10. Mostre o vetor gerado.
Escreva uma função que informe quantas vezes cada número diferente
armazenado no vetor se repetiu.
'''
def qnt():
    print('o número {} repetiu {} vezes ')
    print('\nO número {} repetiu {} vezes '.format(A))
    print('\nO número {} repetiu {} vezes '.format(B))
    
import random

vetor=[]
while True:
    try:
        tamanho=int(input('Informe o tamanho do vetor: '))
        if tamanho<5 or tamanho>20:
            print('O tamanho do vetor deve estar entre 5 e 20' )

        else:
            while len(vetor): #for i in range(len(vetor))
                vetor = random.randint(1,10)
            break
    except ValueError:
        print('O tamanho do vetor deve ser numérico ')
print(vetor)
            
  
        
