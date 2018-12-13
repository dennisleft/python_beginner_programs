## guess the number game
##instrucutions
import random

def instructions():
    name=input('Hey there! Welcome to THE GUESSING GAME.\n\nEnter your name: ')
    print('\nSo {},\nthe number is between 0 & 10.\nYou have 3 tries.\n'.format(name))

##instructions()
##def guess():
##    guess_1=int(input('Guess number: '))##first inpput it as a string
def space():
    print('-'*10,'\n'*2)
    
def play_again():
    play_again1=input('To play again press p and Enter\nTo exit press Enter\n\t')
    space()
    if play_again1=='p':
        game()
    else:
        exit()
    
def game():
    number = random.randint(1,9)
    ##debugging
    ##print(number)
    for i in range(3):
        guess = int(input('Guess the number: '))
        if guess > number:
            print('Lower\n')
        elif guess < number:
            print('Higher\n')
        else:
            print('CORRECT')
            space()
            break
    if guess!=number:
        print('\nThe corect guess was = {}.\nTry again later'.format(number))
        space()

    play_again()



instructions()
game()
    
##trials
##    if i>2:
##        print('ans = {}'.format(number))
##    elif i<=2:
##        print('You win')
##        
##        
        

    
##    if guess_1>number:
##        print('Go lower')
##        guess()
##    elif guess_1<number:
##        print('Go higher')
##        guess()
##    else:
##        print('CORRECT. The number = {} '.format(number))
##        

