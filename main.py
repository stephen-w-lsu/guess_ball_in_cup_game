from random import shuffle


def shuffled_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    guess = ""
    while guess not in ['0', '1', '2']:
        guess = input("Pick a number 0, 1 or 2: ")
    return int(guess)


def compare_list(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct!")
        print(mylist)
    else:
        print("Wrong!")
        print(mylist)

mylist = [' ',' ','O']
shuffled_mylist = shuffled_list(mylist)
guess = player_guess()
compare_list(shuffled_mylist,guess)
