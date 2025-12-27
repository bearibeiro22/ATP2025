# o utilizador começa (jogo 1)

def jogo1(A):
    N=21
    while N>0:
        N=N-A
        print(f"Retiraste {A} fósforos. Sobram {N}")
        N=N-(5-A) # jogada do computador (ele tira N fósforos de forma a que a soma de N com A seja 5 de forma a que reponha um número par de fósforos para este ganhar)
        if N == 1:
            print(f"""O computador retira {5-A}. Sobra {N} fósforo.""")
            return ("perdeste...")
        else:
            A=int(input(f"""O computador retira {5-A}. Sobram {N} fósforos. Quantos fósforos tiras?
"""))
    

# o computador começa (jogo 2)

import random
def jogo2():
    N=21
    num=0 # nº de jogadas 
    winner=False #o computador não está na posição de vencedor
    while N>0:
        if N==21:
            B=random.randint(1,4) # "B" é o número que o computador escolhe
            N= N-B
            num=num+1
        elif N%5!=1 and winner==False: # se N%5!=1 significa que N é par
            if (X+B)>5:
                B= 10-(X+B) # isto é para evitar que o computador retire números negativos de fósforos (ex: retirar -2 fósforos)
            else:
                B=(5-X-B) # jogada "especial" que o computador vai ter de executar para compensar o erro do utilizador e para fazer com que o computador passe à posição de vencedor
            N=N-B         # fica "5-X-B" porque o computador vai ter de subtrair a 5 a sua jogada anterior e a jogada do utilizador já que este jogou mal e não introduziu "5-B" como deveria para ganhar
            num=num+1     # desta forma, mal o utilizador se engana 1 vez, o computador compensa esse engano e passa automaticamente para a posição de vencedor
            
            winner= True # o computador está na posição de vencedor
        elif N%5!=1:
            B=(5-X)
            N=N-B
            num=num+1
        else: # isto acontece se o utilizador nunca se enganar e, desta forma, quem ganha é o utilizador
            B=random.randint(1,4)
            N=N-B
            num=num+1
    
        if N>0:
            X=int(input(f"""O computador retira {B}. Sobram {N}. Quantos fósforos tiras?
 """))
            N=N-X
            num=num+1
            print(f"Retiraste {X} fósforos. Sobram {N}")
    if num%2==1: # número de jogadas é ímpar
        return ("gannhaste!!!")
    else:
        return ("perdeste...")

    

respondeu = False
while respondeu == False:

    print("""Jogo dos 21 fósforos: Quem retirar o último fósforo perde. Podes tirar entre 1 e 4 fósforos.
        Queres jogar primeiro? (s/n)""")
    resposta= input()
    if resposta=="s":
        print("Escolhe quantos fósforos queres tirar (1/2/3/4)")
        A=int(input())
        respondeu = True
        print(jogo1(A))
    elif resposta=="n":
        print("O computador vai começar a escolher um número de 1 a 4")
        respondeu = True
        print(jogo2())
    else:
        print("Opção desconhecida") # se respondermos algo para além de "s" e "n" vai voltar a dar print à pergunta inicial
   

