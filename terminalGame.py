from random import randint
from rules import printRules

class Player:
    pass

class GameLogic:
    pass

printRules()

def buscarPergunta(level):
    with open("questions.txt", "r") as arquivo:
        linhas = arquivo.readlines()
        if level == 1:
            indexSorteado = randint(0,3)
        elif level == 2:
            indexSorteado = randint(4,7)
        else:
            indexSorteado = randint(8,len(linhas))        
        pergunta = linhas[indexSorteado].split(',')
        enunciado = pergunta[0]
        alternativas = pergunta[1]
        gabarito = pergunta[2]
        print(enunciado)
        print(alternativas)
        return gabarito

level = int(input('Digite o nivel: '))            
buscarPergunta(level)