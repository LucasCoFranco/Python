pecas={}
print('Leitura dos dados')
while True:
    cod=int(input('Digite o código: '))
    if cod==0:
        break
    elif cod in pecas:
        print(f'a peca {cod} já está cadastrada')
        continue
    qtde=int(input('Digite a quantidade: '))
    pecas[cod]=qtde
print('Fim da leitura\n')
print('Estoque de pecas')
for c,q in pecas.items():
    print(f' {q} unidades da peca {c}')
print('\n***FIM***')

