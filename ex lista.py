lista=[]
while True:
    try:
        num=int(input('Digite um número positivo ou zero para encerrar: '))
        if num==0:
            print('Contagem encerrada!\n')
            break
        else:
            lista.append(num)
    except ValueError:
        print('O valor deve ser númerico!!')
print('os numeros digitados foram ',lista)
print('A quantidade de numeros foram ',len(lista))
