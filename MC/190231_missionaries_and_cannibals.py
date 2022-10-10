#program for missionaries and cannibals game

def input_section():
    global LeftMissionaries, LeftCannibals, RightMissionaries, RightCannibals, boat
    number_of_m = int(input('\nEnter the number of M in the boat: '))
    number_of_c = int(input('Enter the number of C in the boat: '))

    if number_of_m+number_of_c < 1 or number_of_m+number_of_c > 2:          #A boat only contains minimum 1 and maximum 2 objects
        print('A boat only contains minimum 1 and maximum 2 objects')
        return input_section()

    if boat == 0:
        if number_of_m > LeftMissionaries or number_of_c > LeftCannibals:   #check for taking extra missionaries or cannibals for left side
            print(f'You can not take extra objects...There are {LeftMissionaries} M & {LeftCannibals} C in Left Side....')
            return input_section()
    else:
        if number_of_m > RightMissionaries or number_of_c > RightCannibals:     #check for taking extra missionaries or cannibals for right side
            print(f'You can not take extra objects...There are {RightMissionaries} M & {RightCannibals} C in Right Side....')
            return input_section()

    return number_of_m, number_of_c


def processing(m, c):
    global LeftMissionaries, LeftCannibals, RightMissionaries, RightCannibals, boat, moves
    if boat == 0:
        leftMissionaries = LeftMissionaries - m         #variables start with small letter indicates the temp value
        leftcannibals = LeftCannibals - c               #variables start with capital letter indicates the Actual value
        rightmissionaries = RightMissionaries + m
        rightcannibals = RightCannibals + c
        if (rightcannibals > rightmissionaries != 0) or (leftcannibals > LeftMissionaries != 0):
            print('\nWrong Move...')
            return False
        else:
            LeftMissionaries = leftMissionaries
            LeftCannibals = leftcannibals
            RightMissionaries = rightmissionaries
            RightCannibals = rightcannibals
            boat = 1
            moves += 1
            return True
    else:
        rightmissionaries = RightMissionaries - m
        rightcannibals = RightCannibals - c
        LeftMissionaries = LeftMissionaries + m
        leftcannibals = LeftCannibals + c
        if (rightcannibals > rightmissionaries != 0) or (leftcannibals > LeftMissionaries != 0):
            print('\nWrong Move...')
            return False
        else:
            LeftMissionaries = LeftMissionaries
            LeftCannibals = leftcannibals
            RightCannibals = rightcannibals
            RightMissionaries = rightmissionaries
            boat = 0
            moves += 1
            return True


print('\nMissionaries are represented as M and Cannibals are represented as C\nLives Given 3\n')

LeftMissionaries, LeftCannibals, RightMissionaries, RightCannibals, boat, moves = 3, 3, 0, 0, 0, 0  # boat = 0 means left and 1 means right
game_over = False
lives = 3           #players have three chances
print('Left_Side       River      Right_Side')
while game_over is not True:
    print('-------------------------------------')
    if boat == 0:
        print(f'M={LeftMissionaries} & C={LeftCannibals} Boat|              |M={RightMissionaries} & C={RightCannibals}')
    else:
        print(f'M={LeftMissionaries} & C={LeftCannibals}|              |Boat M={RightMissionaries} & C={RightCannibals}')

    num_m, num_c = input_section()

    if not processing(num_m, num_c):        #these will work when the player gave wrong move
        lives = lives - 1
        if lives == 0:
            print('\nSorry...Better Luck Next Time...')
            print(f'Total Moves: {moves + (3 - lives)}\nRight Moves: {moves}\nWrong Moves: {3 - lives}')
            game_over = True
        else:
            print(f'Your Remaining Lives = {lives}')
    if RightMissionaries == 3 & RightCannibals == 3:
        print('\nCongratulations!!! You Have Won!!!!')
        print(f'M={LeftMissionaries} & C={LeftCannibals}||Boat M={RightMissionaries} & C={RightCannibals}')
        print(f'Total Moves: {moves+(3-lives)}\nRight Moves: {moves}\nWrong Moves: {3-lives}')
        game_over = True

















