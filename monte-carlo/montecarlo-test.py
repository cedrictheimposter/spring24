import matplotlib.pyplot as plt
import numpy as np
import math
import random

'''Add possibility of paramaters'''
'''Now, either function name is given at conception, and exec command is needed'''
'''If function name is given later, exec is not needed but is done at naming'''
'''Current functions available: 
    square, square root, sine, e^-x, half circle, slumpa'''
class Funktion():
    def __init__(self, start, slut,func_name):
        self.namn = "funktion"
        self.resolution = 1000
        self.start = start
        self.slut = slut
        self.X = np.linspace(start,slut,self.resolution)
        self.map = {x:None for x in self.X}
        self.Y = self.map.values()
        self.scattered = 0

        self.func_name = func_name
        self.functions = {"":None, 
                          "square":self.squared, 
                          "square root":self.sqrt, 
                          "sine":self.sine, 
                          "e^-x":self.inv_exponential, 
                          "half circle":self.upper_halfcircle,
                          "slumpa":self.slumpa,
                          "param circle":self.param_circle}
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

    def do_circle(self,mid_point,r,n):
        self.function(mid_point,r,n)

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
    
    def param_circle(self,mid_point,r,n):
        self.X = list()
        self.Y = list()#{x:None for x in self.X}
        self.map = {}
        for i in range(n):
            x = mid_point[0] + r*math.cos(2*math.pi*i/n) 
            y = mid_point[1] + r*math.sin(2*math.pi*i/n)
            self.X.append(x)
            self.Y.append(y)
            self.map[x] = y


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
    '''hade kunnat ändra så att scatter/continuous är ett attribut och så behövs bara en plotfunktion'''
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

def closest(x,interval):
    dist = 10**10
    min_point = 0
    for i in interval:
        if abs(x-i) < dist:
            dist = abs(x-i)
            min_point = i
    return min_point

'''n är antalet slumppunkter, a start och b slut på intervallet som integreras'''
'''Hade kunnat ha slumppunkterna som ett funktionsobjekt...'''
def montecarlo(a,b,n,funktion):
    y_min = min(funktion.Y)
    y_max = max(funktion.Y)
    space_area = (b-a)*(y_max-y_min)

    '''Previous code, which is probably better to use in this case'''
    #random_x = list()
    #random_y = list()
    #for i in range(n):
        #random_x.append(random.uniform(a,b))
        #random_y.append(random.uniform(y_min,y_max))
    randoms = Funktion(a,b,"slumpa")
    randoms.do_scatter(y_min,y_max,n)
    

    '''Sätt ihop dessa två loopar'''
    inner_points = 0
    under_points = dict()
    over_points = dict()
    for i in range(n):
        closest_x = closest(randoms.X[i],funktion.X)
        curve_y = funktion.map[closest_x]
        if abs(randoms.Y[i])<=abs(curve_y):
            if (curve_y >= 0 and randoms.Y[i] >= 0) or (curve_y <= 0 and randoms.Y[i] <= 0):
                inner_points += 1
                under_points[randoms.X[i]] = randoms.Y[i]
            else:
                over_points[randoms.X[i]] = randoms.Y[i]
        else:
            over_points[randoms.X[i]] = randoms.Y[i]
    
    estimated_integral = space_area*(inner_points/n)

    print("out of ",n," points, ", inner_points, "were found under the curve.")
    print("\n the integral was approximated to be ",estimated_integral)

    plt.figure(figsize=(8,8))
    plt.xlim([a-1,b+1])
    plt.ylim([y_min-1,y_max+1])
    #plt.scatter(random_x,random_y,c="b")
    plt.scatter(under_points.keys(),under_points.values(),c="b")
    plt.scatter(over_points.keys(),over_points.values(),c="r")
    plt.plot(funktion.X,funktion.Y,c="b")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("monte carlo för " + funktion.namn)
    plt.show()

    return estimated_integral,inner_points

def main():
    a,b = -1,1
    n = 1000

    #scatt = Funktion(a,b,"scatter")
    #scatt.do_scatter(-1,1,n)
    #scatt.punkt_plotta()

    #f = Funktion(a,b,"half circle")
    #f.def_func()
    #f.exec()
    #f.plotta()
    #montecarlo(a,b,n,f)

    circle = Funktion(a,b,"param circle")
    circle.do_circle([0,0],1,n)
    circle.plotta()
    montecarlo(a,b,n,circle)

main()


#python3 montecarlo-test.py
