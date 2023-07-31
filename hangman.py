import random

def print_list(lis, spaces): # prints out the list aesthetically with or without spaces
    if spaces:
        for i in lis:
            print(i, end=' ')
        print('\n')
    else:
        for i in lis:
            print(i, end='')
        print('\n')

play_again = True
print("Welcome to the word guessing game! To play, input a letter and hit enter.\n- If the letter is correct, it will show up on the spot(s) hangman's correct in. If hangman's wrong, hangman'll let you know.\n- If you put a letter you've already guessed, that turn won't count.")
while play_again:

    numero = random.randrange(0, 19)
    words = ['elephant', 'panther', 'strawberry', 'cicada', 'halogen', 'printer', 'asphalt', 'permutation', 'lingering', 'probable', 'additive', 'insignia', 'duplicate', 'adamant', 'pliable', 'repository', 'superior', 'oxidation', 'cornerstone']
    word = words[numero]
    hangman = [] # this list does the underscore thing
    word_bank = [] # keeps track of incorrect letters
    turns = 0 # keeps track of turns
    won = False # keeps track of whether the user has won

    for i in range(len(word)): # sets up the underscores in the list
        hangman.append('_')

    print('You have 15 turns to find the word. Good luck!')
    print_list(hangman, False)

    while turns < 15 and not won: # counts turns
        guess = input('guess: ')

        if guess in word_bank or guess in hangman: # catches if user already guessed that letter
            print("you've already guessed that letter so this turn doesn't count")
            turns -= 1

        for count, letter in enumerate(word): # goes through each letter in the word
            if guess == letter: # checks if the input is the same as the letter being tested
                hangman[count] = letter # updates list letter based on list index counter

        turns += 1
        print(f'turns completed: {turns}/15')

        if guess not in word and guess not in word_bank: # kees track of whether the letter has been guessed before
            word_bank.append(guess)
        print(f'incorrect letters guessed: ',end='')
        print_list(word_bank, True)

        if '_' not in hangman: # checks if the full word has been guessed and if so, breaks loop
            won = True

        print_list(hangman, False)

    if won: # if the user guessed correctly, tell them they won
        print('Congratulations! You guessed the correct word!')
    else: # else tell them the right word
        print(f'Out of turns! The word was {word}.')

    print('Play again? Type [y] or [n].')
    yes = input()
    if yes == 'y':
        play_again = True
    else:
        play_again = False