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
from random import randint
def menu():
    print('escolha uma opção:')
    print('1:INTERSEÇÃO')
    print('2:UNIAO')
    print('3:DIFERENÇA ENTRE A E B')
    print('4:DIFERENÇA ENTRE B E A')
    print('5:DIFERENÇA SIMETRICA ENTRE A E B')
    print('6:SAIR')
    mostra()

def sorteio():
    while len(A)<8:
        A.add(randint(1,20))
    while len(B)<8:
        B.add(randint(1,20))
   

def mostra():
    print("\tconjuntos")
    print('Conjunto A:',A)
    print('Conjunto B:',B)
    
A=set()
B=set()
sorteio()
    
while True:
    menu()
    m=input("==> ")
    if m=='1':
        print(A&B)
    elif m=='2':
        print(A|B)
    elif m=='3':
        print(A-B)
    elif m=='4':
        print(B-A)
    elif m=='5':
        print(A^B)
    elif m=='6':
        print("FIM DAS ANALISES")
        break
    else:
        print("OPCAO INVALIDA")
    
    pare=input("Tecle algo....")
    
      


