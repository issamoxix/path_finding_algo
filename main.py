import pygame,time
import math as m
import sys
creen=555 #screen size pixels
cr=creen//10
screen = pygame.display.set_mode((creen,creen))
stat = True
clock = pygame.time.Clock()
fs=25 #array's length
grid = [[0 for n in range(fs)] for i in range(fs)]
grid2 = [[0 for n in range(fs)] for i in range(fs)]
score = [[0 for n in range(fs)] for i in range(fs)]
for i in range(len(grid)):
    for r in range(len(grid[0])):
        size = cr*r+10+5
        size2= cr*i+15
        t = m.sqrt(size*size + size2*size2)
        score[i][r]=t//1
e,f = (20,17) #end point coor
#start point 
grid[1][1]=4
start=(1,1)
curr = start
#end point
grid[e][f]=2 
end = (e,f)
#path
path = {}

path2=[]
path2.append(start)
stop = 0
rx=0
gg2=score[e][f]#25*e+25*f
prev=[]
arr ={}
stop_for=1
while stat:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stat = False            
    screen.fill((0,0,0))
    for row in range(fs):
        for col in range(fs):
            color=(255,255,255)
            if grid[row][col] ==1:
                color=(255,0,255)
            elif grid[row][col] ==2:
                color=(255,0,0)
            elif grid[row][col]==3:
                color=(0,0,255)
            elif grid[row][col]==4:
                color=(0,255,0)
            pygame.draw.rect(screen,color,[(20+5)*col+5,(20+5)*row+5,20,20])

    #path finding algo

    if stop ==0:
        arr[curr]=[]
        if curr !=(1,1):
            prev.append(curr)
        if curr[0]==curr[1]:
            d1=curr[0]-1
            d2=curr[1]+2
            q1=d1
            q2=d2
        else:
            d1=curr[0]-1
            d2=curr[0]+2
            q1=curr[1]-1
            q2=curr[1]+2
        for i in range(d1,d2):
            for r in range(q1,q2):
                
                if i==start[1] and r==start[0]:
                    continue      
                if curr[0] ==i  and curr[1]==r:
                    grid2[i][r]=999
                    continue       
                if (i,r) in prev:
                    grid2[i][r]=888
                    f=888
                    continue
                if curr[1] ==i  or curr[0]==r:
                    tp = 2
                else:
                    tp = 1
                if score[i][r]-gg2 <= 0:
                    number=abs(score[i][r]-gg2)
                else:
                    number=abs(score[i][r]-gg2)
                if r==end[1] or i==end[0]:
                    f=end[0]-i+end[1]-r
                    
                else:
                    f = number+tp
                path[(i,r)]=f
                grid2[i][r]=f
                grid[i][r]=1

                
                if i ==end[0] and r==end[1]:
                    rx=0.5
                    curr=(i,r)
                    path2.append(curr)
                    break
                time.sleep(0.05) #u can remove the sleep , but its better for animation
            if rx==0.5:
                break
        
        if curr == (1,1):
            for i in path:
                arr[curr].append(path[i])
        else:
            for i in range(d1,d2):
                for r in range(q1,q2):
                    if rx ==0.5:
                        continue
                    if curr ==(i,r) or (i,r) in prev or (i,r)==start:
                        continue
                    if end==(i,r):
                        continue
                    
                    arr[curr].append(path[(i,r)])
                    
                    
        try:
            arr[curr].sort()
        except:
            mm="m"
        
        if rx != 0.5:
            for i in range(len(grid2)):
                if stop_for !=1:
                    stop_for=1
                    break
                for r in range(len(grid2[0])):
                    
                    if  arr[curr][0] == grid2[i][r] and curr !=(i,r):
                        if (i,r) in prev:
                            stop_for=1
                            continue
                        else:
                            curr=(i,r)
                            path2.append(curr)
                            stop_for=0
                            break
                        #print(i,r)
                        if i==end[0] and r==end[1]:
                            for i in range(len(path2)):
                                grid[path2[i][0]][path2[i][1]]=3
                            stop=1
                        break
            
        elif rx==0.5:
            for i in range(len(path2)):
                grid[path2[i][0]][path2[i][1]]=3
                
            stop=1
        
    clock.tick(60)
    pygame.display.update()