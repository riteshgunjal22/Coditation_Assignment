from GameOfCells import GameOfCells

def userInput():
    live = input("Please enter symbol or value to define the state \nLive = ")
    dead = input("Dead = ")
    r, c = map(int, input("Number of rows and columns in board = ").strip().split())

    if r * c > 100:
        print("Maximum number of cells is 100\nPlease try again")
        raise ValueError("reached maximum limit")

    arr = []
    print("Enter space separated {0} rows".format(r))
    for i in range(r):
        temp = list(map(str, input().strip().split()))
        if len(temp) == c:
            arr.append(temp)
        else:
            print("number of cells in previous row is not equal to ", c)
            break

    return live, dead, arr


if __name__ == '__main__':
    check = int(input("Enter 1 for default/hard coded input \n2 for user input: "))
    live = '1'
    dead = '0'
    if check == 1:
        arr = [['0', '0', '0', '0', '0'], ['0', '0', '1', '0', '0'], ['1', '0', '0', '1', '0'],
               ['1', '0', '0', '0', '0'], ['0', '0', '1', '0', '0']]
    elif check == 2:
        live, dead, arr = userInput()
    else:
        print("Please enter valid input")
        raise ValueError("Invalid Input")

    print("\n\n\nInput Board: ")
    cell = GameOfCells(dead, live)
    cell.printBoard(arr)
    print("Live is represented as {0}\nDead is represented as {1}\n\n".format(live, dead))
    i = 1
    while True:
        print("Generation {0}:".format(i))
        i += 1
        board = []
        board = cell.getNextGeneration(arr)
        cell.printBoard(board)
        arr = board
        char = input("Press \nC to continue\nE to exit\nS to search element\n").upper()
        if char == 'C':
            pass

        elif char == 'S':
            name = input("Please enter name of cell in row_column format: ")
            row, col = map(int, name.split('_'))
            if row < 0 or row > len(board) or col < 0 or col > len(board[0]):
                print("Invalid cell name")
                break
            else:
                cell_state = "Live" if cell.Live == board[row][col] else "Dead"
                print("State of Cell {0}: {1}".format(name, cell_state))
                break


        elif char == 'E':
            break
        else:
            print("Invalid Input")
            break
        print("\n\n\n")
