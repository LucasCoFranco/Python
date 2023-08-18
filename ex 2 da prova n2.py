'''
Crie um programa que leia o nome, idade e salário de diversas pessoas,
guardando os dados de cada pessoa em um dicionário,
e todos os dicionários em uma lista.
Quando o nome for repetido, descarte e quando for vazio, encerre o programa.
Ao encerrar o programa mostre.

a. Os dados das pessoas cadastradas (formatados)

b. Quantas pessoas foram cadastradas

c. A média de idade do grupo

d. Uma lista de todas as pessoas com idade acima da média de idades

e. A soma de todos os salários
'''

dados=dict()
print('Leitura dos dados')
while True:
        nome=input('Digite seu nome ou tecle ENTER para encerrar: ')
        if nome=="":     #encerramento do programa
            break
        elif nome in dados.keys():    #descarte de nome repetido
            print(f'o nome {nome} já está cadastrado!!')
            continue
        dicDados={}
        dicDados['idade']=int(input('Digite sua idade: '))
        dicDados['salario']=float(input('Digite seu salário: '))
        dados[nome]=(dicDados)
        print()
print('\nDados das pessoas')
for pessoa,numeros in dados.items():
    print(f"    Nome: {pessoa}")
    print(f"    Idade: {numeros['idade']}")
    print(f"    Salário: {numeros['salario']}")
    print()

print(f'Pessoas cadastradas:{len(dados)}')
for k,v in dados.items():
        media={v['idade']}/len(dados)
print('Média de idade do grupo:',media)
if idade>media:
        maiores=[]
print('As pessoas com idade acima da media:',maiores[])

    
    
