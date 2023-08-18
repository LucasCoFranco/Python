'''
crie uma matriz de dimensão 5x5
preencha com valores inteiros sequencias de 1 ate 25.(sem leitura)
mostre a matriz resultante no formato(linha x coluna)
em seguida mostre os elemtentos das diagonais principal e secundaria
diagonal principal: 1 7 13 19 25
diagonal secundaria:5 9 13 17 21
'''

mat=[[0 for x in range(5)]for y in range(5)]
n=1
for x in range(5):
    for y in range(5):
        mat[x][y]=n
        print(f'{mat[x][y]:2} \t', end='')
        n+=1
    print()
    
'''Diagonal principal'''
print('\nDiagonal Principal')
for x in range(5):
    print(f'{mat[x][x]:6}', end='')
print()

'''Diagonal secundaria'''
print('\nDiagonal Secundaria')
for x in range(5):
    print(f'{mat[x][4-x]:6}', end='')
print()

