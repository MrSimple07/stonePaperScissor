# Write a program that lets the user play the game of Rock, Paper, Scissors against the computer. 
# The program should work as follows:
# When the program begins, a random number in the range of 1 through 3 is generated.
# If the number is 1, then the computer has chosen rock. If the number is 2,
# then the computer has chosen paper. If the number is 3, 
# then the computer has chosen scissors. (Don’t display the computer’s choice yet.)
# The user enters his or her choice of “rock, ” “paper, ” or “scissors” at the keyboard.
# The computer’s choice is displayed.

import random

print('Game of chance 1=Rock, 2=Paper, 3 = Scissor')
print('type 9 to exit')
compScore =0
playerScore=0

while 1:
    z=random.randint(2,3)
    a=int(input('1=Rock, 2= Paper, 3= Scissor: -----> '))
    if a ==z:
        print(z)
        print('TIE!!!!')
    if a==1 and z ==2:
        print('Computer choose: '+ str(z))
        print("Rock covers paper! So, You WIN!!!")
        playerScore+=1
    if a== 2 and z ==3:
        print('Computer choose: '+ str(z))
        print("Scissor cuts paper so You loose :(")
        compScore+=1
    if a ==3 and z==1:
        print('Computer choose: '+ str(z))
        print("Scissor cuts paper. So You win!!!")
        playerScore+=1

        print
    if a==9:
        break
    print('Your score is: ', playerScore)
    print("Computer's score is: ", compScore)
if playerScore>compScore:
    print('Your score is: ', playerScore)
    print("Computer's score is: ", compScore)
    print('You win!!! Congrats!')
else:
    print('Your score is: ', playerScore)
    print("Computer's score is: ", compScore)
    print('You loose( Try again!')
print('Thank you playing the game!')
