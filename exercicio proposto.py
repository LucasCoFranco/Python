'''
Leia e armazene em um dicionário o nome, a idade 
e o número de telefone de seus contatos, sendo 
que a chave deve ser o nome. Encerre quando o 
nome for vazio
Apresente na tela os dados em ordem alfabética 
pelo nomes. Em seguida, armazene os contatos em 
2 dicionários, utilizando o critério de idade: 
menores de 18 anos em um dicionário e maiores 
em outro, eliminando o dicionário original.
Apresente na tela os 2 dicionários após a 
separação
'''
contatos=dict()
contatomenor=dict()
contatomaior=dict()
while 1:
    nome=input('Digite o nome: ')
    if nome=='':
        break
    elif nome in contatos.keys():
        print(f'contato {nome} ja cadastrado')
        continue
    idade=int(input("idade: "))
    numero=input('numero de telefone: ')
    contatos[nome]=(idade,numero)
    print()        
print('=*'*20)

for nome,dados in sorted(contatos.items()):
    print(f' nome: {nome}')
    print(f' idade: {dados[0]}')
    print(f' contato: {dados[1]}')
    print()
for k,v in contatos.items():
    if v[0]>=18:
        contatomaior[k]=contatos[k]
    else:
        contatomenor[k]=contatos[k]
print(f' Contatos maiores de idade:{contatomaior}')
print(f' Contatos menores de idade:{contatomenor}')

               




        
