# -'- coding: utf-8 -'-

class cannon:
    
    dir = 0
    din = 0
    arc = 22.5
    dirn = 16
    dirhalf = (dirn - 1) / 2
    dirmax = dirn - 1
    var = 0
    prevar = 1
    
    def __init__(self):
        self.varmat = [ 0 for x in range(0,self.dirn)]
        term = self.dirn / 4
        x = 0
        s = 1
        for i in range(0,self.dirn):
            self.varmat[i] = lambda y : s
            if 0 == i % term :
                x = 0
                self.varmat[i] = lambda y : self.getvar()
                s = -s
            else:
                x += 1
            
    '''        
    varmat = [ 
               1, #-11
               1, #-10
               1, #-09
               1, #-08
               1, #-07
               1,
               -1,  #-05
               -1,  #-04
               -1,  #-03
               -1,  #-02
               -1,  #-01
               0,
               1,  # 01
               1,  # 02
               1,  # 03
               1,  # 04
               1,  # 05
               1,
               -1, # 07
               -1, # 08
               -1, # 09
               -1, # 10
               -1  # 11
           ]
    '''

    def getdir(self):
        return self.dir
    
    def getvar(self):
        return self.var
    
    
    def setvar(self,i):
        delta = i - self.dir
        dltabs = abs(delta)
        if dltabs > self.dirhalf:
            delta = -1 * delta
            
        if delta == self.dirhalf:
            self.var = self.getvar()
        elif delta < 0 :
            self.var = -1
        elif delta > 0 :
            self.var = 1
        else:
            self.var = 0
        
        
    def mvdir(self):
        self.setvar(self.din)
        self.dir += self.getvar()
        if self.dir < 0:
            self.dir = cannon.dirmax
        elif self.dir > cannon.dirmax :
            self.dir = 0
    
    def draw(v):
        s = ''
        for i in range(0,v):
            s = s + ' '
        s = s + str(v)
        return s
        
    def test(self):
        while True:
            inp = input('in?')
            if inp == '' :
                pass
            else:
                self.din = inp
                
            self.mvdir()
        
            print('dir:' + cannon.draw(self.dir))
            print('in :' + cannon.draw(self.din))

        
  
c=cannon()
c.test()

