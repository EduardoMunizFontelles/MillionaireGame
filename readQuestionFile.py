from random import choice

with open("questions.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    easyQuestions = linhas[0:6]
    mediumQuestions = linhas[6:12]
    difficultQuestions = linhas[13:len(linhas)-1]

        
def searchQuestion(level):        
        if level == 1:
            pergunta = choice(easyQuestions)
            easyQuestions.remove(pergunta)
        elif level == 2:
            pergunta = choice(mediumQuestions)
            mediumQuestions.remove(pergunta)
        else:
            pergunta = choice(difficultQuestions)
            difficultQuestions.remove(pergunta)        
        pergunta = pergunta.split(',')
        enunciado = pergunta[0]
        alternativas = pergunta[1]
        gabarito = pergunta[2]
        print(enunciado)
        print(alternativas)
        return gabarito