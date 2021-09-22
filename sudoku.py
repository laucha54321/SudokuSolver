
#Checks COLUMN for POSIBLE ELEMENTS
def checkColumn(grid,n):
    possibleNums = [1,2,3,4,5,6,7,8,9]
    possibilitiesColumns = possibleNums
    for i in range(0,9):
        if (grid[i][n] != 0) & (grid[i][n] in possibilitiesColumns):
            possibilitiesColumns.remove(grid[i][n])
    return possibilitiesColumns

#Checks ROW for POSIBLE ELEMENTS
def checkRow(grid,n): 
    possibleNums = [1,2,3,4,5,6,7,8,9]
    possibilitiesRows = possibleNums
    for i in range(0,9):
        if (grid[n][i] != 0) & (grid[n][i] in possibilitiesRows):
            possibilitiesRows.remove(grid[n][i])
    return possibilitiesRows

#FINDS the SECTION with the coordinates and check POSIBLE ELEMENTS
def checkSection(grid,x0,y0):
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

def whatpossible(grid,x,y):
    possibleNums = [1,2,3,4,5,6,7,8,9]
    possibleRow = checkRow(grid,y)
    possibleColumn = checkColumn(grid,x)
    possibleSection = checkSection(grid,x,y)
    intersection = list(set(possibleRow).intersection(set(possibleColumn),set(possibleSection)))
    return intersection

def solve(grid):
    possibleNums = [1,2,3,4,5,6,7,8,9]
    for i in range(0,9):
        for j in range(0,9):
            if grid[j][i] == 0:
                whatp = whatpossible(grid,i,j)
                if len(whatp) == 1:
                    grid[j][i] = whatp[0]
    return grid
