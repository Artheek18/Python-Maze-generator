import pygame
import random
WIDTH = 500
HEIGHT = 500
FPS = 30
# initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Grid")
clock = pygame.time.Clock()
white = [255, 255, 255]
black = [0,0,0]
grey = [128, 128, 128]
pink = [255, 192, 203]
screen.fill(white)
a = 0
b = 0
w = 100
grid = []
stack = []
visit = []


def drawGrid(a,b,n):
    for x in range(1,6):
        a = 0
        b = b + 100
        for y in range(1,6):
            pygame.draw.line(screen, black, [a, b], [a + WIDTH/n, b])           
            pygame.draw.line(screen, black, [a + (WIDTH/n), b], [a + (WIDTH/n), b + (HEIGHT/n)])  
            pygame.draw.line(screen, black, [a + (WIDTH/n), b + (HEIGHT/n)], [a, b + (HEIGHT/n)])   
            pygame.draw.line(screen, black, [a, b + (HEIGHT/n)], [a, b])   
            grid.append((a,b))
            a = a + 100

def push_up(a,b):
    pygame.draw.rect(screen, grey, (a+1, b-w+1, 99, 199), 0)
    pygame.display.update()

def push_down(a, b):
    pygame.draw.rect(screen, grey, (a + 1, b+ 1, 99, 199), 0)
    pygame.display.update()


def push_left(a, b):
    pygame.draw.rect(screen, grey, (a - w +1, b +1, 199, 99), 0)
    pygame.display.update()


def push_right(a, b):
    pygame.draw.rect(screen, grey, (a +1, b +1, 199, 99), 0)
    pygame.display.update() 

def single_cell(a, b):
    pygame.draw.rect(screen, pink, (a +1, b +1, 99, 99), 0)          
    pygame.display.update()

def backtracking_cell(a, b):
    pygame.draw.rect(screen, grey, (a +1, b +1, 99, 99), 0)        
    pygame.display.update()    


def carve_out_maze(a,b):
    single_cell(a, b)                                              
    stack.append((a,b))                                            
    visit.append((a,b))                                         
    while len(stack) > 0:                                         
        cell = []                                                  
        if (a + w, b) not in visit and (a + w, b) in grid:      
            cell.append("right")                                  

        if (a - w, b) not in visit and (a - w, b) in grid:       
            cell.append("left")

        if (a , b + w) not in visit and (a, b + w) in grid:     
            cell.append("down")

        if (a, b - w) not in visit and (a , b - w) in grid:      
            cell.append("up")

        if len(cell) > 0:                                          
            cell_chosen = (random.choice(cell))                    

            if cell_chosen == "right":                             
                push_right(a, b)                                   
                a = a + w                                         
                visit.append((a, b))                              
                stack.append((a, b))                                

            elif cell_chosen == "left":
                push_left(a, b)
                a = a - w
                visit.append((a, b))
                stack.append((a, b))

            elif cell_chosen == "down":
                push_down(a, b)
                b = b + w
                visit.append((a, b))
                stack.append((a, b))

            elif cell_chosen == "up":
                push_up(a, b)
                b = b - w
                visit.append((a, b))
                stack.append((a, b))
        else:
            a, b = stack.pop()                                    
            single_cell(a, b)                                        
            backtracking_cell(a, b)                              



a, b = 0,0
drawGrid(0, -100, 5)
carve_out_maze(a,b)

running = True
while running:
# keep running at the at the right speed
    clock.tick(FPS)
# process input (events)
    
    for event in pygame.event.get():
# check for closing the window
         pygame.display.update()   
         if event.type == pygame.QUIT:
             running = False


