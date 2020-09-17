import pygame,time
screen = pygame.display.set_mode((255,255))
stat = True
clock = pygame.time.Clock()
grid = [[0 for n in range(10)] for i in range(10)]
grid2 = [[0 for n in range(10)] for i in range(10)]
e,f = (9,5)
#start point 
grid[1][1]=1
start=(1,1)
curr = start
#end point
grid[e][f]=2 
end = (e,f)
#path
path = {}
arr = []
path2=[]
path2.append(start)
for i in range(len(grid)):
    print(grid2[i])
stop = 0
rx=0
while stat:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stat = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0]//(20+5)
            row = pos[1]//(20+5)
            grid[row][col] = 1
            print("Click ", pos, "Grid coordinates: ", row, col)
            
    screen.fill((0,0,0))
    for row in range(10):
        for col in range(10):
            color=(255,255,255)
            if grid[row][col] ==1:
                color=(0,255,0)
            elif grid[row][col] ==2:
                color=(255,0,0)
            elif grid[row][col]==3:
                color=(0,0,255)
            pygame.draw.rect(screen,color,[(20+5)*col+5,(20+5)*row+5,20,20])

    #path finding algo
    if stop ==0:
        for i in range(curr[0]-1,curr[1]+2):
            for r in range(curr[0]-1,curr[1]+2):
                if curr[1]==i and curr[0]==r:
                    continue            
                if curr[1] ==i  or curr[0]==r:
                    tp = 2
                else:
                    tp = 1
                x = abs(r-end[0])
                y = abs(i-end[1])
                g = x+y
                if end[0]==i and end[1]==r:
                    g1=g+2
                else:
                    g1=g+1
                f = g1+tp
                if f ==1:
                    print(path2)

                path[(i,r)]=f
                grid2[i][r]=f
                grid[i][r]=1
                print('the coordinate is : ',i,r, 'the score is ',f)
                if i ==end[0] and r==end[1]:
                    rx=0.5
                    curr=(i,r)
                    path2.append(curr)
                    break
                time.sleep(0.1)
            if rx==0.5:
                break
        
        for i in path:
            arr.append(path[i])
        arr.sort()
        if rx != 0.5:
            for i in range(len(grid2)):
                for r in range(len(grid2[0])):
                    if grid2[i][r] == arr[0]:
                        curr=(i,r)
                        path2.append(curr)
                        print(i,r)
                        if i==end[0] and r==end[1]:
                            for i in range(len(path2)):
                                grid[path2[i][0]][path2[i][1]]=3
                            stop=1
                        break
        elif rx==0.5:
            print(path2)
            for i in range(len(path2)):
                grid[path2[i][0]][path2[i][1]]=3
            stop=1
                
    clock.tick(60)
    pygame.display.update()

for i in range(len(grid)):
    print(grid2[i])
print('###############################')
for i in range(len(grid)):
    print(grid[i])
# arr = []
# for i in path:
#     arr.append(path[i])
#     #print(path[i])
# arr.sort()
# print(arr[0])
# for i in range(len(grid2)):
#     for r in range(len(grid2[0])):
#         if grid2[i][r] == arr[0]:
#             print(i ,r)
