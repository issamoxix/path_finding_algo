import pygame
import procc as p
import sys
print("############## Welcome to path_finding algo ##############")
print('## You can add walls by holding space and drawing ')
print('### add points by typing py main.py -from 5,5 -to 20,20')
print('####Press "S" to start the algo ENjoy !!')
print('###################################################')
screen = pygame.display.set_mode((555,555))
clock = pygame.time.Clock()
f=25
grid = [[0 for n in range(f)] for i in range(f)]
stat =True
x = sys.argv[2]
x_f = (int(x[0:x.find(',')]),int(x[x.find(',')+1:len(x)]))
y = sys.argv[4]
y_f=(int(y[0:y.find(',')]),int(y[y.find(',')+1:len(y)]))
start = x_f
end = y_f
grid[start[0]][start[1]]=1
grid[end[0]][end[1]]=2
while stat:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stat = False
        
        #event when mouse click grid=5 to change color to white 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0]//(20+5)
            row = pos[1]//(20+5)
            grid[row][col]=5
            print(row,col)

        if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_e:
                    pos = pygame.mouse.get_pos()
                    col = pos[0]//(20+5)
                    row = pos[1]//(20+5)
                    grid[row][col]=1
                    
                if event.key==pygame.K_r:
                    pos = pygame.mouse.get_pos()
                    col = pos[0]//(20+5)
                    row = pos[1]//(20+5)
                    grid[row][col]=2
                if event.key == pygame.K_s:

                    print('Algo Started !!')
                    if len(start)==0 or len(end) ==0:
                        print('Add a from point and to point by typing, -from x,y -to x,y')
                    else:
                        proc = p.procc(grid)
                        proc.set_val(start[0],start[1],end[0],end[1])
                        x = proc.procced([])
                        for i in x:
                            grid[i[0]][i[1]]=3
                    print(start)
                    print(end)
                    print(x)
                if event.key == pygame.K_t:
                    for i in range(len(grid)):
                        for r in range(len(grid[0])):
                            grid[i][r]=5
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pos = pygame.mouse.get_pos()
            row = pos[1]//(20+5)
            col = pos[0]//(20+5)
            grid[row][col]=4
        if keys[pygame.K_d]:
            pos = pygame.mouse.get_pos()
            row = pos[1]//(20+5)
            col = pos[0]//(20+5)
            grid[row][col]=5          
                    
    screen.fill((0,0,0))
    for row in range(f):
        for col in range(f):
            color=(255,255,255)
            if grid[row][col] ==1:
                color=(0,255,0)
            elif grid[row][col] ==2:
                color=(255,0,0)
            elif grid[row][col]==3:
                color=(0,0,255)
            elif grid[row][col]==4:
                color=(0,0,0)
            elif grid[row][col]==5:
                color=(255,255,255)
            pygame.draw.rect(screen,color,[(20+5)*col+5,(20+5)*row+5,20,20])
    
    clock.tick(60)
    pygame.display.update()