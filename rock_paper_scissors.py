'''
create a rock paper scissors game
vs computer
'''

###Think of how you can use keys and values
import random

rock, paper, scissors='rock','paper','scissors'
options=['rock','paper','scissors']
comments_draw=['We had the same thought.\n\tNot as shabby as I thought :D',
          'Same!!How now',
          'Same! My mind and yours are linked.',
          'Are we related? Same thinking']
comments_user_win=['OK smart guy. You WIN',
              'You WIN. Dont get too comfortable though.',
              'You WIN. All hail the great one! ',
              'You WIN.']
comments_comp_win=['You LOSE :D.',
                   'Take the L.',
                   'LOSER.',
                   'I own this game :D.']


def space():
    print('='*20,'\n')
def play_again():
    play_choice=input('To play again Press p\nTo exit press ENTER: ')
    if play_choice=='p':
        play()
    else:
        exit()

print('Hello human, insert evil laugh :D\nLet us play ROCK PAPER SCISSORS\n')
print('\tINSTRUCTIONS:\n1. Type your option, ie. rock / paper /scissors, when prompted.\n2. Type in small letters ONLY\n3. Best of 3\n\t\t\t\t ENJOY\n\n')

def play():
    user_score=0
    comp_score=0
    for games_played in range(3):
        
        print('I have already selected mine.\nYour turn:')

        #to select random item from list
        ans=random.choice(options)
        human=input()
        

        if human!=rock and human!=paper and human!=scissors:
            print('\tEnter a valid option')
            space()
        elif human==ans:
            print(random.choice(comments_draw))
            space()
        elif (ans==paper and human==rock) or (ans==rock and human==scissors) or (ans==scissors and human==paper):#comp wins
            print(random.choice(comments_comp_win)+'\nI picked {}.'.format(ans))
            comp_score+=1
            space()
        elif (human==paper and ans==rock) or (human==rock and ans==scissors) or (human==scissors and ans==paper):
            print(random.choice(comments_user_win)+'\nI picked {}.'.format(ans))
            user_score+=1
            space()

    print('Final score:\n\tME: {}\tYOU: {}'.format(comp_score,user_score))
    if user_score>comp_score:
        print('\nDamn! You are good at this.')
    elif user_score==comp_score:
        print('Draw!!')
    else:
        print('\n I win!!:D')

    play_again()

play()
