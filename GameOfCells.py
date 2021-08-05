class GameOfCells:
    Dead = 0
    Live = 1

    def __init__(self, d, l):
        self.Dead = d
        self.Live = l

    def printBoard(self, board):
        for i in board:
            print(" ".join(map(str, i)))
        print()

    def getNextGeneration(self, board):

        if len(board) == 0 or len(board[0]) == 0:
            raise ValueError("No row or column present in the board")

        nRows = len(board)
        nCols = len(board[0])

        buf = [[0 for j in range(nCols)] for i in range(nRows)]

        for i in range(nRows):
            for j in range(nCols):
                buf[i][j] = self.getNewCellState(board[i][j], self.getNumOfLiveNeighbours(i, j, board))
        return buf

    def getNewCellState(self, currState, liveNeighours):
        newState = currState

        if currState == self.Live:
            if liveNeighours < 2:
                newState = self.Dead
            elif liveNeighours == 2 or liveNeighours == 3:
                newState = self.Live
            elif liveNeighours > 3:
                newState = self.Dead

        elif currState == self.Dead:
            if liveNeighours == 3:
                newState = self.Live

        else:
            print(currState, " is not defined or incorrect state")
            raise ValueError(currState, " is not defined or incorrect state")

        return newState

    def getNumOfLiveNeighbours(self, cellR, cellC, board):
        count = 0
        rowEnd = min(len(board), cellR + 2)
        colEnd = min(len(board[0]), cellC + 2)

        for i in range(max(0, cellR - 1), rowEnd):
            for j in range(max(0, cellC - 1), colEnd):
                if (i != cellR or j != cellC) and board[i][j] == self.Live:
                    count += 1

        return count
