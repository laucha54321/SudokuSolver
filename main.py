import pygame,const,BoardFunction,sudoku,numpy
pygame.init()
WIN = pygame.display.set_mode((const.WIN_WIDTH,const.WIN_HEIGHT)) 
pygame.display.set_caption("SUDOKU")

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
       ]

def draw_Window():
    WIN.fill(const.GREEN)
    BoardFunction.drawBoardSudoku(WIN,const.WIN_WIDTH,const.WIN_HEIGHT,grid)
    #BoardFunction.drawBoardChess(WIN,const.WIN_WIDTH,const.WIN_HEIGHT,1)
    pygame.display.update()

def main():    
    clock = pygame.time.Clock()
    run = True
    
    while run:
        clock.tick(const.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(numpy.matrix(sudoku.solve(grid)))
        draw_Window()
    pygame.quit()
if __name__ == "__main__":
    main()
    input()
