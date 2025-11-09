# TPC 3


# passo 1: definir as funções

import random

def menu():
    print("""Bem vindo ao programa!
    1) criar lista
    2) ler lista
    3) soma dos valores da lista
    4) média dos valores da lista
    5) maior valor da lista
    6) menor valor da lista
    7) ver se a lista está ordenada por ordem crescente
    8) ver se a lista está ordenada por ordem decrescente
    9) procurar um valor na lista
    0) sair do programa 
    """)
    return int(input("digite o número da operação que pretende executar no programa "))

def randomList(): # consoante o número de valores que o utilizador quer ler, o PC vai dar return desses N valores de 0 a 100
    N=int(input("quantos números deseja ter na lista?"))
    return [random.randint(0,100) for i in range(N)] 

def inputList(): # o ultilizador é que digita os N números à sua escolha 
    N=int(input("quantos números deseja ter na lista?"))
    return [int(input(f"digite o número {i+1}/{N}")) for i in range (N)]

def somaList(list):
    soma=0
    for n in list:
        soma=soma+n
    return soma

def médiaList(list):  
    return somaList(list) / len(list)

def maxList(list): 
    max=list[0]
    for l in list[1:]: # lista a partir do índice 1 (2º elemento) até ao fim
        if l>max: 
            max=l # vai fazendo isto todas as vezes até chegar ao fim da lista (ou seja, vai comparando sempre o valor anterior ao seguinte, a ver qual é o maior)
    return max

def minList(list):
    min=list[0]
    for l in list[1:]:
        if l<min:
            min=l # vai fazendo isto todas as vezes até chegar ao fim da lista (ou seja, vai comparando sempre o valor anterior ao seguinte, a ver qual é o menor)
        return min
    
def estaOrdenadaMax(list):
    estaOrdenada=True
    for i in range(len(list)-1): # só há len(list)-1 comparações 
        if list[i]>= list[i+1]:
            estaOrdenada=False
    return print("Sim") if estaOrdenada else print("Não")

def estaOrdenadaMin(list):
    estaOrdenada=True
    for i in range(len(list)-1): # só há len(list)-1 comparações 
        if list[i]<=list[i+1]:
            estaOrdenada=False
    return print("Sim") if estaOrdenada else print("Não")

def procuraElemento(list, elem):
    for idx, n in enumerate(list): # idx = index
        if n==elem: # elem = valor que queremos saber se está na lista ou elem = lista[idx]
            return idx
    else:
        return -1 # caso o elemento que o utilizador queira procurar na lista não exista, o PC dá return do valor -1 (como pede o enunciado) 


# passo 2: constuir o código principal

op=menu()
internalList=[] # lista interna, para a qual vão os valores todos da lista criada

while op!=0:
    if op not in [0,1,2,3,4,5,6,7,8,9]:
        print("operação inválida")
        op=menu()

    if op==1:  
        internalList=randomList()  # guardar os dados da lista random na lista interna
    
    elif op==2: # guardar os dados da lista criada pelo utilizador na lista interna
        internalList=inputList()

    if (op!=1 or 2) and internalList==[]: # só se pode realizar alguma das outras operações (3/4/5/6/7/8/9) depois de se criar uma lista, ou seja, depois de passar pelo passo 1 ou 2 e depois de se ter criado a internalList
        print("""necessita de haver uma lista primeiro: 
    1) criar lista
    2) ler lista
    """) # funciona como um aviso, para que o utilizador perceba que tem de digitar o número 1 ou o 2 para o programa funcionar corretamente
    
    elif op==3:
        print(f"a soma dos valores da lista interna é {somaList(internalList)}")

    elif op==4:
        print(f"a média dos valores da lista interna é {médiaList(internalList)}")

    elif op==5:
        print(f"o maior valor da lista interna é {maxList(internalList)}")

    elif op==6:
        print(f"o menor valor da lista interna é {minList(internalList)}")

    elif op==7:
        estaOrdenadaMax(internalList)

    elif op==8:
        estaOrdenadaMin(internalList)

    elif op==9:
        elem=int(input("digite o valor que quer verificar se está na lista interna"))
        idx=procuraElemento(internalList,elem)
        if idx!=-1:
            print(f"o valor {elem} está na lista interna no índice {idx}")
        else:
            print(f"o valor {elem} não está na lista interna")
    print(f"a lista interna guardada é {internalList} ")
    op=menu() # dar return ao menu caso o utilizador queira realizar mais alguma operação

    
print ("ok, vamos encerrar o programa!")