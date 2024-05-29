A collection of tiny Python projects. They are very simple and little and basically just tiny easy pet projects. Here's a quick summary:

----------------------------------------------------------------------------------------------------------

pygame-tests:

balls-random.py & balls-not-random.py - Just some quick moving circle simulators for fun. Uses pygame, but I looked up so much stuff so it was a joint effort between the internet and I.

dodgeball.py - A continuation of balls-random.py where user controls a tiny red ball and tries to avoid the random bigger balls. I'm gonna try to make it with sprites later because currently the draw function is making this weird.

sudoku-solver.py - WIP, supposedly you give it a board and hit enter and it solves the board for you.

----------------------------------------------------------------------------------------------------------

speed-typing:

speed-accuracy-typer.py - Gets the user to type words as fast as possible and calculates their speed and accuracy, using the Time module to track time. This is mostly matrix and number-crunching practice.

speed-accuracy-typer-v2.py - Basically a more accurate version of the speed-accuracy-typer.py, but with more accurate results. It doesn't use the matrix as heavily and is literally only for fun.

----------------------------------------------------------------------------------------------------------

renaming:

renamer.py & renamed.py - This is a silly little guessing game inspired by something I saw on Instagram. I just wanted to see how funny it would be to make a project using meme lingo, so for example instead of calling print() it calls none_pizza_left_beef().

----------------------------------------------------------------------------------------------------------

IEEE-32-bit-maker.py - Takes user input and converts it to IEEE 754 32-bit precision floating point format. Can only handle decimals and catches if user enters an int or "cheats" by entering an int disguised as a decimal (for example, 12.0). A lot of converting to string and float and int and back to make it work and look pretty.

matrix-solver.py - Very simple program to solve an augmented matrix. Cannot handle any errors in inputs and not properly tested, but theoretically should be able to solve most augmented matrices.

hangman.py - Very similar to hangman where it makes the user guess a word letter by letter within a certain number of turns. The word(s) are randomly generated from a list of hardcoded words and this project is mostly while loop and list practice.

decimal-numbers.py - Takes user input and either converts to or from binary or hexadecimal depending on which they select, using my little algorithm. Uses lists and a little math.

bad-calculator.py - As the name implies, it is a really janky calculator. I had to make a calculator using classes to model composition, aggregation, and inheritance so I made this. It does get the right answer when the inputs are perfect, but if you try to trick it with inoperable inputs it will just break. Does work when used correctly though, which is nice.

gfc.py - Finds the greatest common factor. It's not very efficient but it helps with my homework!

mantissa-maker.py - Generates the first 23 binary bits of a decimal inputted (for floating point precision blah blah blah). This is just for homework help!