''' create a fun typing test that displays the user speed, accuracy, and words per minute '''

import time

def print_pretty(list, row = None): # prints the matrix in a pretty way, mostly 
    if row != None: # prints one row
        for i in range(len(list[row])):
            print(list[row][i], end=' ')
        print('\n')
    else: # if the call doesn't specify row, prints whole matrix
        for j in range(len(list)):
            for i in range (len(list[0])):
                print(list[j][i], end=' ')
            print('\n')

rows = 4 # row 1 - word, row 2 - length, row 3 - incorrect letters
columns = 20 # 20 words
words = [[0 for x in range(columns)] for y in range(rows)] # initializes matrix
'''     initializes as: 
              0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19

        0  [ [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      tracks the word
        1    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      tracks length of word
        2    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],      tracks user's input
        3    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]     tracks user's incorrect letters
'''

# initializes the words to type
words[0][0] = 'back'
words[0][1] = 'draw'
words[0][2] = 'watch'
words[0][3] = 'line'
words[0][4] = 'cuticle'
words[0][5] = 'manage'
words[0][6] = 'sick'
words[0][7] = 'forest'
words[0][8] = 'issue'
words[0][9] = 'abstract'
words[0][10] = 'oak'
words[0][11] = 'sickle'
words[0][12] = 'mostly'
words[0][13] = 'without'
words[0][14] = 'school'
words[0][15] = 'of'
words[0][16] = 'line'
words[0][17] = 'mean'
words[0][18] = 'fixer'
words[0][19] = 'dropping'

print("I'm going to time how long it takes for you to type a bunch of words and also test your accuracy. Hit enter to start. Good luck!")
enter = input()

start = time.time() # gets time at the beginning
for i in range(len(words[0])):
    print(words[0][i])
    words[2][i] = input()
    print('\n')
end = time.time() # gets time at the end

print(f'That took {end-start:.2f} seconds!\n\nstats')
print(f'words per minute: {len(words[0])/((end-start)/60):.2f}') # calculates words per minute
print('\n')