'''
Esse programa armazena dados dos alunos em um dicionario
Encerra quando a matricula for 0
'''
alunos=dict() #dicionario com todos os alunos
print('leitura dos dados')
while 1:
    try:
        matr=int(input('Digite a matricula: '))
        if matr==0:
            break
        elif matr in alunos.keys():
            print(f'matricula {matr} ja cadastrada')
            continue
        nome=input('nome: ')
        idade=int(input('idade: '))
        curso=input('curso: ')
        alunos[matr]=(nome,idade,curso)
        print()
    except ValueError:
        print('Valor invalido')
print('=*'*20)

print('\nCadastro de alunos')
for matricula,dados in alunos.items():
    print(f' Aluno: {dados[0]}')
    print(f' Matricula: {matricula}')
    print(f' Idade: {dados[1]}')
    print(f' Curso: {dados[2]}')
    print()

print('***FIM***')

