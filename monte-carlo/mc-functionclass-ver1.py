import matplotlib.pyplot as plt
import numpy as np
import math
import random

'''Add possibility of paramaters, and possibility of directly entering function name'''
'''With and execute command to take the given function in action'''
'''Now, either function name is given at conception, and exec command is needed'''
'''If function name is given later, exec is not needed but is done at naming'''
class Funktion():
    def __init__(self, start, slut,func_name):
        self.namn = "funktion"
        self.resolution = 1000
        self.start = start
        self.slut = slut
        self.X = np.linspace(start,slut,self.resolution)
        self.map = {x:None for x in self.X}
        self.Y = self.map.values()

        self.func_name = func_name
        self.functions = {"":None, "square":self.sq}
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

    def sq(self,x):
        return x**2

    def squared(self):
        self.namn = "square"
        for x in self.map:
            self.map[x] = x**2
        self.Y = self.map.values()

    def sqrt(self):
        self.namn = "square root"
        for x in self.map:
            self.map[x] = x**(1/2)
    
    def sine(self):
        self.namn = "sine wave"
        for x in self.map:
            self.map[x] = math.sin(x)
    
    def inv_exponential(self):
        self.namn = "inverse exponential"
        for x in self.map:
            self.map[x] = 1/math.exp(x)  

    def upper_halfcircle(self):
        self.namn = "half circle" 
        for x in self.map:
            self.map[x] = math.sqrt(1-x**2)


    '''Kanske ha en basic-plot funktion utanför klassen som klassmetoden använder'''
    def plotta(self):
        plt.figure(figsize=(8,8))
        plt.plot(self.X,self.Y,c="b")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title(self.namn)
        plt.show()
