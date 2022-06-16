from readQuestionFile import buscarPergunta
from rules import printRules

class Player:
    pass

class GameLogic:
    pass

printRules()

acertou = True
ganhou = False
contador = 1
prize = 100

while (acertou) and not(ganhou):
    print(f'Rodada {contador}!')
    print(f'Question prize: ${prize}!')

    if (contador <= 5):
        level = 1
    elif (contador <= 10):
        level = 2
    else:
        level = 3

    gabarito = buscarPergunta(level)

    resposta = input('Digite a sua resposta: ').upper()

    if (resposta == gabarito):
        print('Certa Resposta!')
        if (contador == 15):
            print('Parabens you won!')
            ganhou = True
        contador += 1
        prize *= 2
    else:
        print('Resposta incorreta, burro!')
        acertou = False    

