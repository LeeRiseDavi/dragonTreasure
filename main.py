# this imports the random module
import random

# this imports the time module
import time

# this function provides a brief pause.
def sleep():
    time.sleep(2)

# gives game a title
title = 'Dragon Treasure'
# makes title uppercase
print(title.upper())

# this function helps format text by printing empty line
def space():
    print('')

space()

# program breather
sleep()

# this prints the setup for making a choice
def intro():
    print('You travel down the road. You are on your way back to town after running an errand for your neighbor. Unfortunately, the errand you ran took most of the day, and with it, the light of the sun.')
    space()
    sleep()
    print('You soon find yourself lost... \n \n \t Away from the main road, the tall trees of the dark forest disorients you. \n \n As the light fades, it grows colder. Indeed, each step seemed to take you out of the forest to an unfamiliar area where the forest was starting to give way to hills and cliffs. Eager for shelter from the encroaching cold of night, you begin to look around...')
    space()
    sleep()

intro()

# this allows for a slightly longer pause
def sleep2():
    time.sleep(3)

sleep2()

# this setups the player to make a choice
def choiceSetup():
    print('As you search for shelter, your eyes come to rest on two identical cave openings, side by side in the cliffside. You hesitate for a moment. This is a land of dragons after all. And dragon\'s love to use caves to store their hoarde.')
    space()
    sleep()
    print('You turn to leave. You correctly reasoned no treasure would be worth that kind death. Dragons protect their hoarde fiercely!')
    space()
    sleep()
    print('\n \n \t As you turn to leave a glint catches your eye. You scarcely believe it and your eyes return to examine the first cave more closely.')
    space()
    sleep()
    print('As you look again, you notice something twinkling in both caves. As luck would have it, curiousity gets the better of you. Certainly, there could not be a dragon in both caves...')
    space()
    sleep()
    print('\n \n \t A dragon\'s hoarde could revitalize an entire region... Certainly more than a life of farming could provide. Provided one could escape with it. Though surely a dragon would have made itself known b-', end='')
    print('NO!')
    space()
    sleep()
    print('It is simply impossible. The claws and fangs alone... Nevermind the near silent flight capabilities, brute strength, and unreal speed. But it could be out hunting or asle-', end='',)
    print('NO!')
    space()
    sleep()
    print('Aw hell! \n \n \t Which cave? \n \n \t The first or second?')

choiceSetup()

# this takes player input
# this ensures the player input is recognized as a number
playerChoice = int(input())

# if the playerChoice does not equal 1 or 2, invites the player to choose again
if playerChoice != 1 or playerChoice != 2:
    while playerChoice < 1 or playerChoice > 2:
        print('Please pick either 1 or 2.')
        playerChoice = int(input())

# this creates a random chance to win or lose regardless of which option the player picks
randomChance = random.uniform(0.00, 1.00)

# if the playerChoice indicates 1, this prints the bad ending
def badEnding():
    if playerChoice == 1 and randomChance > 0.21:
        print('You ventured into the first cave.')
        space()
        sleep2()
        print('What you had mistaken as the glint of treasure was actually the glint of light from the dragon\'s fangs. The dragon quickly overwhelms you...')
        space()
        sleep2()
        print('Death is not a hunter unbeknownst to its prey, one is always aware that it lies in wait.')

badEnding()

# this adds an additional chance of getting treasure when choose cave 1!
def badTossUp():
    if playerChoice == 1:
        if randomChance < 0.20:
            print('You ventured into the first cave.')
            space()
            sleep2()
            print('\n \n \t The glint of light you saw from the entrance turned out to be a hoarde of dragon treasure!')
            space()
            sleep2()
            print('As you rouse yourself from your stupor, you realize a dragon is also there. The dragon watches you with keen interest.')
            space()
            sleep2()
            print('The dragon discerns that you are not a threat and decides to return to basking in its treasure. \n \n \t You\'re not sure what happenened but you decide the best time and place to figure that out is later and somewhere else. At least, the dragon let you walk away.')

badTossUp()

# this adds an additional chance of getting eaten when choosing cave 2!
def goodTossUp():
    if playerChoice == 2:
        if randomChance < 0.20:
            print('You ventured into the second cave.')
            space()
            sleep2()
            print('\n \n \t The glint of light you saw from the entrance turned out to be a hoarde of dragon treasure!')
            space()
            sleep2()
            print('As you rouse yourself from your stupor, you realize a dragon is also there. The dragon watches you with keen interest.')
            space()
            sleep2()
            print('It flicks its tongue at you and lunges!')
            space()
            sleep()
            print('Death is not a hunter unbeknownst to its prey, one is always aware that it lies in wait.')

goodTossUp()

def goodEnding():
    if playerChoice == 2 and randomChance > 0.21:
        print('You ventured into the second cave.')
        space()
        sleep2()
        print('\n \n \t The glint of light you saw from the entrance turned out to be a hoarde of dragon treasure!')
        space()
        sleep2()
        print('As you rouse yourself from your stupor, you realize a dragon is also there. The dragon watches you with keen interest.')
        space()
        sleep2()
        print('It flicks its tongue at you and pounces on you. Before you realize it, the dragon is cuddling you! Practically begging you for pets.')
        space()
        sleep()
        print('It will be some time before you can leave the cave, but the dragon seems likely to let you leave with some of the treasure.')

goodEnding()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
