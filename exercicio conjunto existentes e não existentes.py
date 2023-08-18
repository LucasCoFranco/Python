'''
criar e mostrar um conjunto de 10 elementos no intervalo de 1 a 30
digite o elemento que deseja procurar ou ENTER para encerrar
criar 2 conjuntos:
existentes
nexistentes
ao digitar ENTER mostre o conjunto original
                        o conjunto dos existentes
                        o conjunto dos não existentes
'''
from random import randint
conjunto=set()
e=set()
ne=set()
while len(conjunto)<10:
        conjunto.add(randint(1,30))
while True:
    
    print(conjunto)
    resp=int(input('Digite o elemento que deseja procurar ou 0 para encerrar: '))
    if resp==0:
        print('o conjunto original:',conjunto)
        print('conjunto dos existentes:',e)
        print('conjunto dos não existentes:',ne)
        break
    else:
        if resp in conjunto:
            e.add(resp)
            conjunto.remove(resp)
        else:
            ne.add(resp)

        
        
    
    
