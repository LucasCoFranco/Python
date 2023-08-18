'''
Elabore um programa que efetue a leitura de valores positivos reais até que 0 ou um valor
negativo seja fornecido
 Aplique o tratamento de exceção para recusar dados inválidos. Ao
final devem ser apresentados:
o maior e o menor valores informados pelo usuário, a
quantidade de valores aceitos pelo programa, a soma e a média dos números lidos.

usar o len para ver quantos numeros tem  na lista
'''
lista=[]  #lista vazia pois não foi determinado quantos números serão inseridos
soma=0     #criando a variavel soma
menor=1000000000000000000000000000   #criando a variavel menor
maior=-1    #criando a variavel maior
while True:
    try:
        num=float(input('Digite um número positivo ou zero para encerrar: '))
        soma+=num        #fazer a soma dos números conforme acrescenta eles
        if num<=0:
            print('Contagem encerrada!\n')
            break
        else:
            if num>maior:
                maior=num       #acrescentar o valor ao maior valor
            if num<menor:
                menor=num       #acrescentar o valor ao menor valor
            lista.append(num)   #acrescentar o valor digitado à lista
    except ValueError:
        print('O valor deve ser númerico!!')  #tratamento de exceção caso o usuario não digite um número
media=soma/len(lista)   #calcular a média com a quantidade de números da lista
print('Os valores digitados:',lista)  
print('A quantidade de valores aceitos:',len(lista))
print('A soma dos valores é',soma)
print('A media desses valores é',media)
print('O maior valor digitado foi',maior, 'e o menor foi',menor)
        
              
        
