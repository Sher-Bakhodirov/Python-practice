# A simple program that randomly picks a number from 1 to 100. User has to guess the number. There is no limit of tries

from random import randint
computer = randint(1,101)
user = []
# A while loop was used to avoid interruption of the game after a user enters unexpexted value(this can not be avoided by exeption handling because exeption handiling would mean that user has to start evering again)
while True:
    command = input('Enter your number\n')
    if not command.isdigit():
        print('only numbers are allowed ')
        continue
    elif int(command) < 1 or int(command) > 100:
        print('out of boundiries')
        continue
    else:
        user.append(int(command))
    if user[-1] == computer:
        print('Win')
        print(f'It took you {len(user)} attempts')
    elif len(user) == 1:
        if abs(user[0]-computer) <= 10:
            print('Warm')
            continue
        else:
            print('Cold')
            continue
    elif len(user) > 1:
        if abs(user[-1]-computer) < abs(user[-2]-computer):
            print('Warmer')
            continue
        else:
            print('Colder')
            continue
        
