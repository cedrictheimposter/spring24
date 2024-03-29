import matplotlib.pyplot as plt
import numpy as np
import math
import random


class Funktion():
    def __init__(self, start, slut,func_name):
        self.namn = "funktion"
        self.resolution = 1000
        self.start = start
        self.slut = slut
        self.X = np.linspace(start,slut,self.resolution)
        self.map = {x:None for x in self.X}
        self.scattered = 0
        self.Y = self.map.values()

        self.func_name = func_name
        self.functions = {"":None, 
                          "square":self.squared, 
                          "square root":self.sqrt, 
                          "sine":self.sine, 
                          "e^-x":self.inv_exponential, 
                          "half circle":self.upper_halfcircle,
                          "slumpa":self.slumpa}
        self.function = self.functions[self.func_name]

    def def_func(self, func):
        self.func_name = func
        self.function = self.functions[self.func_name]
        self.exec()
    
    def exec(self):
        self.namn = self.func_name
        for x in self.map:
            self.map[x] = self.function(x)
        self.Y = self.map.values()
    
    def do_scatter(self,y1,y2,n):
        self.scattered = 1
        self.function(y1,y2,n)

    def add_params(self,params):
        '''Here params are taken in as list'''
        pass

    def add_params_manually(self):
        '''allows user to put in params manually'''
        pass

    def squared(self,x):
        return x**2

    def sqrt(self,x):
        return x**(1/2)
    
    def sine(self,x):
        return math.sin(x)
    
    def inv_exponential(self,x):
        return 1/math.exp(x)  

    def upper_halfcircle(self,x):
        return math.sqrt(1-x**2)

    '''This became a bit to incompatible with the rst of the class, with do-method
        redefining X,Y and map
        and to have to have another plot function
        
        Maybe make another class for data? with coloring points...'''
    def slumpa(self,y1,y2,n):
        self.X = list()
        self.Y = list()#{x:None for x in self.X}
        self.map = {}
        for i in range(n):
            random_x = random.uniform(self.start,self.slut)
            random_y = random.uniform(y1,y2)
            self.X.append(random_x)
            self.Y.append(random_y)
            self.map[random_x] = random_y


    '''Kanske ha en basic-plot funktion utanför klassen som klassmetoden använder'''
    def plotta(self):
        if self.scattered == 1:
            plt.scatter(self.X,self.Y,c="b")
        else:
            plt.figure(figsize=(8,8))
        plt.plot(self.X,self.Y,c="b")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self.namn)
        plt.show()
