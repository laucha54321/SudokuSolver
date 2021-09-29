import classsudoky,numpy
from copy import copy

grid3 = classsudoky.sudoku()
grid3.board =[
[0,0,0,8,0,0,4,2,0],
[5,0,0,6,7,0,0,0,0],
[0,0,0,0,0,9,0,0,5],
[7,4,0,1,0,0,0,0,0],
[0,0,9,0,3,0,7,0,0],
[0,0,0,0,0,7,0,4,8],
[8,0,0,4,0,0,0,0,0],
[0,0,0,0,9,8,0,0,3],
[0,9,5,0,0,3,0,0,0]]

print('This is the starting grid: ')
print(numpy.matrix(grid3.board))
print('Press any key')
input()

def solve(grid):
    minlen = [10,0,0]
    for y in range(0,9):
        for x in range(0,9):
            if grid.board[y][x] == 0:
                whatp = grid.whatpossible(y,x)
                if len(whatp) <= minlen[0]:
                    minlen[0] = len(whatp)
                    minlen[1] = y
                    minlen[2] = x
                    if len(whatp) == 1:
                        grid.board[y][x] = whatp[0]
    if minlen[0] == 1:
        solve(grid)
    if minlen[0] > 1:
        multiplesolve(grid,minlen)
    if minlen[0] & grid.isSolved() == True:
        return grid

def multiplesolve(grid,minlen):
    y = minlen[1]
    x = minlen[2]
    whatp = grid.whatpossible(y,x)
    possb = []
    #This for solves the stupid issues with references and stupid python, fuck python is so stupid to do this i hate it. At least now I know that C# is better.
    for t in range (0,minlen[0]):
        possb.append([])
        for i in range(0,9):
            possb[t].append([])
            for j in range(0,9):
                possb[t][i].append(int(grid.board[i][j]))
        print(numpy.matrix(possb[t]))   
    for i in range (0,2):
        if len(whatp) >=1:    
            possb[i][y][x] = whatp[i]
            possb[i] = classsudoky.sudoku(possb[i])
            solve(possb[i])
    

solve(grid3)

















