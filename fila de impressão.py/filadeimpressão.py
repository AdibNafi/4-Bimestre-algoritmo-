#VAMOS SIMULAR COM FUNCIONA O ALGORITMO DE UMA 
#IMPRESSORA QUE PODE RECEBER IMPRESSAO DE DIVERSOS 
#COMPUTADORES, VAMOS PENSAR EM UMA FILA.

#funçoes de interação com o usuario 
def menu():
    fila_impressão=filaDeImpressao()
    #criando uma instancia para a classe
    fila_impressão.configurar_inicial()
    #configurar os atributos de entrada/inicial 
    while true:
        #opção para o nosso usuario
        print("Opções:")
        print("1 Adiciona um trabalho na fila da impressao")
        print("2. imprimir o proximo trabalho da fila")
        print("3. mostrar a fila de impressao")
        print("4. sair")
        escolha = input("escolha uma opcao 1-4")
         #aqui vai ser lido a escolha do usuario

    if escolha== "1":
        trabalho = input("digite o nome do trabalho a ser impresso")
        #maquina da pessoa que esta imprimindo 
        fila_impressao.adicionar_trabalho(trabalho)
    elif escolha=="2":
        fila_impressão.processar_trabalho()
    elif escolha=="3":
        fila_impressão.mostrar_fila()
    elif escolha=="4":
        print("saindo do programa")
        break
    else:
        print("opcao invalida")