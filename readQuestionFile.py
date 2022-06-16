from random import randint

def buscarPergunta(level):
    with open("questions.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if level == 1:
            indexSorteado = randint(0,5)
        elif level == 2:
            indexSorteado = randint(6,11)
        else:
            indexSorteado = randint(12,len(linhas)-1)        
        pergunta = linhas[indexSorteado].split(',')
        enunciado = pergunta[0]
        alternativas = pergunta[1]
        gabarito = pergunta[2]
        print(enunciado)
        print(alternativas)
        return gabarito