import pygame
import const
BLACK = (0,0,0)
WHITE =  (255,255,255)
def drawBoardChess(WIN,width,height,white):
    if height > width:
        res = width
    else:
        res = height
    squaresize = res//8
    if white==False:
        WIN.fill(WHITE)
        for i in range(0,8):
            for j in range(0,8):
                if ((i%2==0) & (j%2==0))^((i%2==1) & (j%2==1)):
                    pygame.draw.rect(WIN,const.BLACK,(i*squaresize,j*squaresize,squaresize,squaresize))
    if white==True:
        WIN.fill(BLACK)
        for i in range(0,8):
            for j in range(0,8):
                if ((i%2==0) & (j%2==0))^((i%2==1) & (j%2==1)):
                    pygame.draw.rect(WIN,const.WHITE,(i*squaresize,j*squaresize,squaresize,squaresize))
def drawBoardSudoku(WIN,width,height,numbers):
    if height > width:
        res = width
    else:
        res = height
    WIN.fill(WHITE)
    cellsize = res//9
    for i in range(0,10):
        linesize = 1
        if (i/3==1) or (i/3 == 2) or (i/3==3):
            linesize = 4
        pygame.draw.line(WIN,BLACK,(i*cellsize,0),(i*cellsize,cellsize*9),linesize)
        pygame.draw.line(WIN,BLACK,(0,i*cellsize),(cellsize*9,i*cellsize),linesize)
    writeBoardSudoku(WIN,numbers,cellsize)

def writeBoardSudoku(WIN,numbers,cellsize):
    offsetx = 10
    offsety = 10
    for i in range(0,9):
        for j in range(0,9):
            text = const.FONT.render(str(numbers[j][i]),False,BLACK)
            if(numbers[j][i]!=0):
                WIN.blit(text,(i*cellsize + offsetx,j*cellsize + offsety))


        
                