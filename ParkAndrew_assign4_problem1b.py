#change wording to match the sample on the website

"""
Assignment #4, Part 1b
Andrew Park
"""

#player1 starts
player1 = True

# input the number of sticks on the table
numSticks = int(input('How many sticks (10-100)? '))

# validate number of sticks on table, if invalid re-prompt until valid        
while numSticks < 10 or numSticks > 100:
    if numSticks > 100:
        print("Sorry, You have entered too many sticks. Try again.")
    else:
        print("Sorry, number of sticks entered is too little. Try again.")
            
    numSticks = int(input('How many sticks (10-100)? '))
    
print()
print("Great Let's play ...")
print()
    
# loop until no more sticks

while numSticks > 0:
    if player1 :
        print('Turn: Player 1')
    else:
        print('Turn: Player 2')

    if player1:
        print('There are ',numSticks,' sticks on the table.')
        sticksPicked = int(input('How many sticks do you want to take (1, 2 or 3)? '))
        print()
    else:
        print('There are ',numSticks,' sticks on the table.')
        sticksPicked = int(input('How many sticks do you want to take (1, 2 or 3)? '))
        print()

    if sticksPicked < 1 or sticksPicked > 3:
        print("Sorry, number entered is not valid.")
        print()
    elif sticksPicked > numSticks:
        print("Sorry, that would bring the total # of sticks below 0. Try again.")
        print()
    else: 
        numSticks -= sticksPicked
        if numSticks > 0:
            player1 = not player1

print('\nThere are no sticks left on the table!  Game over.')
if player1:
    print('Player 2 wins!')
else:
    print('Player 1 wins!')
