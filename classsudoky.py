import numpy
grid1 = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]

class sudoku:
    def __init__(self,grid=False):
        self.board = []
        if grid:
            self.board = grid
        else:
            for i in range(0,9):
                self.board.append([0,0,0,0,0,0,0,0,0])

    #Checks if it is Solved
    def isSolved(self):
        board = self.board
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]==0:
                    return False
        return True
    

    #Checks COLUMN for POSIBLE ELEMENTS
    def checkColumn(self,n):
        grid = self.board
        possibleNums = [1,2,3,4,5,6,7,8,9]
        possibilitiesColumns = possibleNums
        for i in range(0,9):
            if (grid[i][n] != 0) & (grid[i][n] in possibilitiesColumns):
                possibilitiesColumns.remove(grid[i][n])
        return possibilitiesColumns

    #Checks ROW for POSIBLE ELEMENTS
    def checkRow(self,n): 
        grid = self.board
        possibleNums = [1,2,3,4,5,6,7,8,9]
        possibilitiesRows = possibleNums
        for i in range(0,9):
            if (grid[n][i] != 0) & (grid[n][i] in possibilitiesRows):
                possibilitiesRows.remove(grid[n][i])
        return possibilitiesRows

    #FINDS the SECTION with the coordinates and check POSIBLE ELEMENTS
    def checkSection(self,x0,y0):
        grid = self.board
        possibleNums = [1,2,3,4,5,6,7,8,9]  
        possibilitiesSection = possibleNums
        sectionX = x0//3
        sectionY = y0//3
        for x in range(0,3):
            for y in range(0,3):
                xc = sectionX*3+x
                yc = sectionY*3+y
                if (grid[yc][xc]!=0) & (grid[yc][xc] in possibilitiesSection):
                    possibilitiesSection.remove(grid[yc][xc])
        return possibilitiesSection
    
    
    #Calculate the POSIBILITIES of a CELL by finding the intersection of posibilities 
    def whatpossible(self,y,x):
        grid = self.board
        possibleNums = [1,2,3,4,5,6,7,8,9]
        possibleRow = self.checkRow(y)
        possibleColumn = self.checkColumn(x)
        possibleSection = self.checkSection(x,y)
        intersection = list(set(possibleRow).intersection(set(possibleColumn),set(possibleSection)))
        return intersection



