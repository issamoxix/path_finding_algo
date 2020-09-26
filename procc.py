import math as m
class root:
    def __init__(self, row, col):
        self.row, self.col  = (row,col)
    def square_ana(self):
        self.from_row=self.row-1
        self.to_row=self.row+2
        self.from_col=self.col-1
        self.to_col=self.col+2
    def h(self, r, c):
        screen = 255
        cr = screen//10
        size=cr*c+15
        size2=cr*r+15
        t = m.sqrt(size*size + size2*size2)
        return t//1
    def g(self, i ,r):
        if self.row == i or self.col == r:
            return 2
        else:
            return 1
        
#  grid and procc stuff
class procc:
    def __init__(self, grid):
        fs = 10
        self.row = None
        self.col  = None
        self.root = (self.row,self.col)
        self.e_row = None
        self.e_col = None
        self.grid = grid
    def set_val(self, row, col,y,z):
        r = root(row,col)
        if self.e_row == None and self.e_col == None:
            self.e_row=y
            self.e_col= z
            
        if self.row == None and self.col == None:
            self.root = r
            self.row = r.row 
            self.col = r.col
            
    creen=555 #screen size pixels
    cr=creen//10
    
    grid2 = [[0 for n in range(25)] for i in range(25)]
    score = [[0 for n in range(25)] for i in range(25)]
    for i in range(len(score)):
        for r in range(len(score[0])):
            size = cr*r+15
            size2= cr*i+15
            t = m.sqrt(size*size + size2*size2)
            score[i][r]=t//1
    
    def procced(self,path):
        self.root.square_ana()
        current_p_array ={}
        current_p_array[(self.root.row,self.root.col)] = []
        
        for i in range(self.root.from_row,self.root.to_row):
            for r in range(self.root.from_col,self.root.to_col):
                if self.root.row ==i and self.root.col ==r:
                    continue
                h = abs(self.root.h(i,r)-self.score[self.e_row][self.e_col])
                g = self.root.g(i,r)
                if self.grid[i][r] ==4:
                    continue
                self.grid[i][r]=1
                if self.e_row ==i or self.e_col == r:
                    f= abs(self.e_row-i+self.e_col-r)
                else:
                    f = h + g 
                
                current_p_array[(self.root.row,self.root.col)].append(f)
                self.grid2[i][r]=f
                if i==self.e_row and r==self.e_col:
                    return 0
        current_p_array[(self.root.row,self.root.col)].sort()
        for i in range(len(self.grid2)):
            for r in range(len(self.grid2[0])):
                if current_p_array[(self.root.row,self.root.col)][0] == self.grid2[i][r]:
                    min_c = (i,r)
        
        if min_c[0]==self.e_row and min_c[1]==self.e_col:
            return 0

        path.append(min_c)
        u = procc(self.grid)
        u.set_val(min_c[0],min_c[1],self.e_row,self.e_col)
        u.procced(path)
        return path
                


            