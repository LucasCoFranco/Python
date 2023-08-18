'''
crie 2 conjuntos de 8 elementos com numeros de 1 a 20. Mostre os 2 conjuntos em
um menu com as seguintes opções:
1:INTERSECÇÃO
2:UNIAO
3:DIFERENÇA ENTRE A E B
4:DIFERENÇA ENTRE B E A
5:DIFERENÇA SIMETRICA ENTRE A E B
6:SAIR
'''
def sorteio():
    while len(A)<8:
        A.add(randint(1,20))
    while len(B)<8:
        B.add(randint(1,20))
    print('Conjunto A:',A)
    print('\nConjunto B:',B)
return A,B

A=set()
B=set()

sorteio()
print('Esses foram os numeros sorteados:',sorteio())
