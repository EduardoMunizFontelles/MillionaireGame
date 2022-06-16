#ADD tips option
#ADD more questions

from readQuestionFile import searchQuestion
from rules import printRules

class Player:
    pass

class GameLogic:
    pass

printRules()

acertou = True
ganhou = False
contador = 1
prizes = [100,200,300,500,1000,2000,4000,16000,32000,64000,125000,250000,500000,1000000]
amountWon = 0

while (acertou) and (contador <= 15):
    print(f'Rodada {contador}!')
    print(f'Question prize: ${prizes[contador-1]}!\n')

    if (contador <= 5):
        level = 1
    elif (contador <= 10):
        level = 2
    else:
        level = 3

    gabarito = searchQuestion(level)
    decisao = int(input(f'Would you like to: 1-Answer, 2-Get a tip or 3-Leave with your money: ${amountWon}?\n'))
    if (decisao == 1):
        resposta = input('Very well, what is your guess then?').upper()

        if (resposta == gabarito):
            print('Certa Resposta!\n\n')
            amountWon = prizes[contador-1]
            contador += 1
        else:
            print('Resposta incorreta, burro!\n\n')
            acertou = False  
    elif (decisao == 2):
        pass
    else:
        print(f'Thanks for playing. You are leaving with: ${amountWon}!\n')          
        acertou = False

if (contador == 11):
    print('Congrats! You are a millionaire.')
    print(f'Amount: $1.000.000')

print('End of the game!')