'''
tratamento de exceções
'''
resp='s'
while resp=='s':
    while True:
        try:
            x=float(input('Digite o valor de x: '))
            y=float(input('Digite o valor de y: '))
            break
        except ValueError:
            print('O valor deve ser numérico')
        finally:
            print('Finalmente...')
            print(x, '+', y ,'=', x+y)
            print(x, '-', y ,'=', x-y)
            print(x, 'x', y ,'=', x*y)
            try:
                print(x, '/', y ,'=', x/y)
            except ZeroDivisionError:
                    print('? \nDivisão por zero!')
            finally:
                print('Sempre passo pelo finally')
    resp=input('\nDeseja continuar? (s/n): ')
