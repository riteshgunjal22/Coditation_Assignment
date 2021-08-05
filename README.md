# Coditation Assignment - Game Of Life
## Problem Statement
Imagine an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two
possible states, live or dead. Every cell interacts with its eight neighbors, which are the cells that are
directly horizontally, vertically, or diagonally adjacent.
### At each step in time (tick), the following transitions occur:
1. Any live cell with fewer than two live neighbors dies, as if by loneliness.
2. Any live cell with more than three live neighbors dies, as if by overcrowding.
3. Any live cell with two or three live neighbors lives, unchanged, to the next generation.
4. Any dead cell with exactly three live neighbors comes to life.
The initial pattern constitutes the 'seed' (randomly placed 500 cells) of the system. The first generation is
created by applying the above rules simultaneously to every cell in the seed — births and deaths happen
simultaneously, and the discrete moment at which this happens is called a tick. (In other words, each
generation is a pure function of the one before.)
### Write a program in the language(s) of your choice with following guidelines:
1. Accept a user input of new cells (max 100 at every step/tick) to be placed; each cell should have a
unique name which is to be accepted by the user. This input can be accepted through a CLI or
HTML element or any other form of user interface
2. Acceptance of the user input represents a tick and program is expected to calculate the state of
every cell
3. The program should output the state of the cells and changes - representation (UI/CLI et al.) of
the state of the cells can be decided by the developer
4. The program should provide a way to search by the name of the cell and show the current state of
the cell
5. The program should end on termination through appropriate OS specific signals

## Programming Language used - Python
### How to Run
This project is built using Python 3.5 and requires that the user has at least Python 3 installed in order to run the program.
In order to run this project the user must open a terminal/console and navigate to the project folder and then into the script directory. Once inside of the script directory simply run python main.py in order to begin the program.
Once the program has been started the user will get 2 options wheteher to continue with hard coded input or manual input.
#### Input format guidlines
1. Enter number of rows and columns in space separated format. User can create board of maximum 100 cells.
2. Enter each row of grid in space separated format.
3. After each generation user will get 3 options - Continue, Exit or Search
4. In search option user has to enter cell name as row_column format. Example '2_1' will represent cell with row number 2 and column number 1. Any invalid name will give error.(Row will be in the range 0 to n-1 and columns will be in the range 0 to m-1)

