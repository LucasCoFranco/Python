while True:
    try:
        data=input("Digite a data no formato dd/mm/yyyy ou ENTER para sair: ")
        if data=='':
            break
        datalist=list(data)
        dia=datalist[:2]
        diaf=''.join(dia)
        mes=datalist[3:5]
        mesf=''.join(mes)
        ano=datalist[6:len(datalist)]
        anof=''.join(ano)
        if diaf=='29' and mesf=='02' and int(anof)%4!=0: #Verifica ano bissexto
            print("Ano não é bissexto")
        elif int(diaf)>29 and mesf=='02': #Verifica dia invalido em fevereiro
            print("Dia inválido")
        elif int(mesf)>12 or int(mesf)<1: #Verifica mês maior q 12 ou menor q 1
            print("Mês inválido")
        elif int(diaf)>31 or int(diaf)<1: #Verifica dia maior q 31 ou menor q 1
            print("Dia inválido")
        elif diaf=='31' and mesf=='04' or mesf=='06' or mesf=='09' or mesf=='11': #Verifica dia 31 em meses que não tem dia 31
            print("Dia inválido")
        else:
            if mesf=='01':
                print(f"{diaf} de janeiro de {anof}")
            if mesf=='02':
                    print(f"{diaf} de fevereiro de {anof}")
            if mesf=='03':
                print(f"{diaf} de março de {anof}")
            if mesf=='04':
                    print(f"{diaf} de abril de {anof}")
            if mesf=='05':
                print(f"{diaf} de maio de {anof}")
            if mesf=='06':
                    print(f"{diaf} de junho de {anof}")
            if mesf=='07':
                print(f"{diaf} de julho de {anof}")
            if mesf=='08':
                    print(f"{diaf} de agosto de {anof}")
            if mesf=='09':
                print(f"{diaf} de setembro de {anof}")
            if mesf=='10':
                    print(f"{diaf} de outubro de {anof}")
            if mesf=='11':
                print(f"{diaf} de novembro de {anof}")
            if mesf=='12':
                    print(f"{diaf} de dezembro de {anof}")
    except (TypeError, ValueError):
        print("O que foi digitado não era uma string ou não está no formato certo.")