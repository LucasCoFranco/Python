'''
Esse programa armazena dados dos alunos em dicionario aninhados
Encerra quando a matricula for 0
'''
alunos=dict()
while 1:
    try:
        matr=int(input('Digite a matricula: '))
        if matr==0:
            break
        elif matr in alunos.keys():
            print(f'matricula {matr} ja cadastrada')
            continue
        dicAluno={}
        dicAluno['nome']=input('nome= ')
        dicAluno['idade']=int(input('idade= '))
        dicAluno['curso']=input('curso= ')
        alunos[matr]=dicAluno
        print()
    except ValueError:
        print('Valor Invalido')
print('=*'*20)

print('\nCadastro dos alunos')
for matricula,dados in alunos.items():
    print(f"  Aluno: {dados['nome']}")
    print(f"  Matricula: {matricula}")
    print(f"  Idade: {dados['idade']}")
    print(f"  Curso: {dados['curso']}")
    print()
print('***fim***')
