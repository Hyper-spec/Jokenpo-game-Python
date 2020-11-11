import random
import time
yesno = "Yes"
win = 0
compwin = 0
print('-_'*8)
print('JOKENPÔ GAME')
print('_-'*8)
player = int(input('Choose between rock, paper and scissors:\n[1]Rock\n[2]Paper\n[3]Scissors\nYour choice: '))
while player > 3 or player < 1:
    player = int(input('Please, digit between Rock[1], Paper[2] and Scissors[3]: '))
while yesno == "Yes":
    time.sleep(0.2)
    computer = random.randint(1, 3)
    print('Loading...')
    time.sleep(2.2)
    print('\033[36mJô')
    time.sleep(1)
    print('Ken')
    time.sleep(1)
    print('Pô\033[m')
    time.sleep(0.6)

    rps = ['rock', 'paper', 'scissors']
    # Rock
    if player == 1:
        if computer == player:
            print('Computer: rock \nPlayer: rock')
            print('\033[36mDraw \033[m')
        elif computer == 3 and player == 1:
            print('Computer: scissors\nPlayer: rock')
            print('\033[36mPlayer win\033[m')
            win += 1
        elif computer == 2 and player == 1:
            print('Computer: paper\nPlayer: rock')
            print('\033[36mComputer win\033[m')
            compwin += 1
    # Rock

    # paper
    if player == 2:
        if computer == 2 and player == 2:
            print('Computer: paper\nPlayer: paper')
            print('\033[35mDraw\033[m')
        elif computer == 1 and player == 2:
            print('Computer: rock\nPlayer: paper')
            print('\033[35mPlayer win\033[m')
            win += 1
        elif computer == 3 and player == 2:
            print('Computer: scissors\nPlayer: paper')
            print('\033[35mComputer win\033[m')
            compwin += 1
    # paper

    # scissors
    if player == 3:
        if computer == 3 and player == 3:
            print('Computer: scissors\nPlayer: scissors')
            print('\033[33mDraw\033[m')
        elif computer == 2 and player == 3:
            print('Computer: paper\nPlayer: scissors')
            print('\033[33mPlayer win\033[m')
            win += 1
        elif computer == 1 and player == 3:
            print('Computer: rock\nPlayer: scissors')
            print('\033[33mComputer win\033[m')
            compwin += 1
    # scissors
    time.sleep(1)
    yesno = str(input('Do you wish to play again?(yes or no): ')).capitalize()
    if yesno == "Yes":
        print('-_' * 20)
        print('\033[1:32mPlayer Victories: {}'.format(win))
        print('\033[1:32mComputer Victories: {}\033[m'.format(compwin))
        player = int(input('Choose between rock, paper and scissors:\n[1]Rock\n[2]Paper\n[3]Scissors\nYour choice: '))
    while yesno != 'Yes' and yesno != 'No':
        yesno = str(input('INVALID OPTION!!! Do you wish to play again (Only yes or No)?: ')).capitalize()
time.sleep(0.6)
print('\033[31mGame\033[m')
time.sleep(0.6)
print('\033[31mOver\033[m')
time.sleep(0.6)
if win == 0:
    print('What?, don´t you won from computer? :0↔\nYou´re a loser, loser :/ ')
if win == 1:
    print('You has won just 1 match :(\nI´m so sorry.')
if win == 2:
    print('You has won twice, congratulations! ;)')
if win > 2:
    print('You has won {} times, congratulations! XD'.format(win))






