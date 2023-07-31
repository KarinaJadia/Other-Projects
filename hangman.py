import random

def print_list(lis, spaces): # prints out the list aesthetically
    if spaces:
        for i in lis:
            print(i, end=' ')
        print('\n')
    else:
        for i in lis:
            print(i, end='')
        print('\n')

play_again = True
print("Welcome to the word guessing game! To play, input a letter and hit enter.\n- If the letter is correct, it will show up on the spot(s) it's correct in. If it's wrong, it'll let you know.\n- If you put a letter you've already guessed, that turn won't count.")
while play_again:

    numero = random.randrange(0, 17)
    words = ['elephant', 'panther', 'strawberry', 'cicada', 'halogen', 'printer', 'asphalt', 'permutation', 'lingering', 'probable', 'additive', 'insignia', 'duplicate', 'adamant', 'pliable', 'repository', 'superior']
    word = words[numero]
    it = [] # this list does the underscore thing
    word_bank = [] # keeps track of incorrect letters
    turns = 0
    won = False

    for i in range(len(word)): # sets up the underscores in the list
        it.append('_')

    print('You have 15 turns to find the word. Good luck!')
    print_list(it, False)

    while turns < 15 and not won: # counts turns
        guess = input('guess: ')

        if guess in word_bank or guess in it: # catches if user already guessed that letter
            print("you've already guessed that letter so this turn doesn't count")
            turns -= 1

        for count, letter in enumerate(word): # goes through each letter in the word
            if guess == letter: # checks if the input is the same as the letter being tested
                it[count] = letter # updates list letter based on list index counter

        turns += 1
        print(f'turns completed: {turns}/15')
        if guess not in word and guess not in word_bank:
            word_bank.append(guess)
        print(f'incorrect letters guessed: ',end='')
        print_list(word_bank, True)

        if '_' not in it: # checks if the full word has been guessed and if so, breaks while loop
            won = True

        print_list(it, False)

    if won:
        print('Congratulations! You guessed the correct word!')
    else:
        print(f'Out of turns! The word was {word}.')

    print('Play again? Type [y] or [n].')
    yes = input()
    if yes == 'y':
        play_again = True
    else:
        play_again = False