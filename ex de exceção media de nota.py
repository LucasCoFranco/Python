'''
notas dos alunos
'''
resp='s'
while resp=='s':
    nome=input('Digite seu nome: ')
    while True:  
        try:
            nota1=float(input('Digite a primeira nota: '))
            if nota1>=0 and nota1<=10:
               print('nota digitada: ',nota1)
               break
            else:
                print('valor invalido!\nO valor deve estar entre 0 e 10!')
        except ValueError:
            print('O valor deve ser numérico')
        
            
    while True:
        try:
            nota2=float(input('Digite a segunda nota: '))
            if nota2>=0 and nota2<=10:
                print('nota digitada: ',nota2)
                break
            else:
                print('valor invalido!\nO valor deve estar entre 0 e 10!')
        except ValueError:
             print('O valor deve ser numérico')
    while True:      
        try:
            nota3=float(input('Digite a terceira nota: '))
            if nota3>=0 and nota3<=10:
                break
            else:
                print('valor invalido!\nO valor deve estar entre 0 e 10!')
        except ValueError:
                 print('O valor deve ser numérico')
    soma=nota1 + nota2 + nota3
    media=soma/3
    print('nota digitada: ',nota3)
    print(nome,',Sua média é de ',media)
    resp=input('\nDeseja continuar? (s/n): ')

        

