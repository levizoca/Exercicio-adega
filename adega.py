total = 0
cont = 0
vinho = ['tinto', 'branco', 'rosé'] #3 vinhos como exemplo
estoque = [0, 0, 0]

resposta = 1
while resposta == 1:
    print("O que deseja fazer?",
        "\n 1. Deseja adicionar vinhos ao estoque?",
        "\n 2. Deseja adicionar um novo tipo de vinho?",
        "\n 3. Sair")
    resposta2 = int(input())
    if resposta2 == 1:
        resposta3 = resposta2
        
        #Define qual vinho será escolhido
        while resposta3 == 1:
            print("Qual vinho deseja adicionar?")
            while cont < (len(vinho)):
                print(cont, vinho[(cont)])
                cont = cont + 1
            idVin = int(input())
            cont = 0
            tipoVin = vinho[idVin]
            
            #Adiciona a quantidade de vinhos ao estoque
            while tipoVin == vinho[idVin]:
                numVin = int(input("Digite a quantidade de vinhos:"))
                estoque[idVin] = estoque[idVin] + numVin
                total = total + numVin
                print("Deseja adicionar mais algum vinho?",
                    "\n 1. Sim",
                    "\n 2. Não")
                resposta3 = int(input())
                tipoVin = ""
                if resposta3 == 2:
                    resposta2 = 2
                    resposta = 2                    
    else:
        
        #Adiciona um novo tipo de vinho a lista
        new = str(input("Digite o nome do vinho: "))
        vinho.append(new)
        estoque.append(0)

if total != 0:
    print("Total de vinhos na adega:", total)
    cont = 0
    for cont in range(len(vinho)):
        print("Quantidade de vinhos", vinho[cont],"no estoque:", estoque[cont])
else:
    print("Ok!")
    
