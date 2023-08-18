'''
o programa le o nome, o sexo(F/M), o peso e a altura de 1 pessoa. O peso deve
ser um valor entre 30 e 250kg e a altura um valor entre 1.0 e 2.20m. Recusar
valores fora dos intervalos.
calcule o imc da pessoa dada pela formula: imc=peso/altura*2
mostre o nome, o imc e informa de acordo com o sexo a situaçao da pessoa
sexo f
imc < 20 - abaixo
imc >= 20 e < 35 - normal
imc >= 35 - acima

sexo m
imc < 25 - abaixo
imc >= 25 e < 38 - normal
imc >= 38 - acima
'''
resp='s'
while resp=='s':
    nome=input('Digite seu nome: ')
    while True:
        sexo=input('Digite seu sexo (F/M): ')
        sexo=sexo.upper()
        if sexo=="F" or sexo=="M":
            break
        else:
            print('O sexo deve ser F(feminino) ou M(masculino).\nDigite novamente ')
    while True:
        try:
            peso=float(input('Digite seu peso: '))
            if peso>=30 and peso<=250:
                break
            else:
                print('O seu peso deve estar entre 30 e 250kg.\nDigite novamente ')
        except ValueError:
            print('O valor digitado não é aceito')
    while True:
        try:
            altura=float(input('Digite sua altura: '))
            if altura>=1.0 and altura<=2.20:
                break
            else:
                print('Sua altura deve estar entre 1.0 e 2.20m.\nDigite novamente ')
        except ValueError:
            print('O valor digitado não é aceito')

    imc = peso/altura**2
    if sexo=="F":
        if imc < 20:
            print(nome,'seu imc é de',imc,' e está abaixo do normal')
        elif imc < 35:
            print(nome,'seu imc é de',imc,' e está normal')
        else:
            print(nome,'seu imc é de',imc,' e está acima do normal')
    else:
        if imc < 25:
            print(nome,'seu imc é de',imc,' e está abaixo do normal')
        elif imc <38:
            print(nome,'seu imc é de',imc,' e está normal')
        else:
            print(nome,'seu imc é de',imc,' e está acima do normal')
    resp=input('Deseja continuar? (s/n): ')
        
