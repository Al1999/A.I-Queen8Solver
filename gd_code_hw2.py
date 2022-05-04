import numpy as np 

def function(x, y):
    z =  5*x*x + 40*x + y*y - 12*y + 127
    return z

def grad_function(x, y): 
    g = np.array([ 10*x + 40, 2*y - 12]) 
    return g

def gd( x0, n):
    Xp = x0

    for i in range(500):
        Xn = Xp - n * grad_function( Xp[0], Xp[1] ) 
        Xp = Xn 
    return Xp 

def trails(n): 
    best = None 

    for t in range(10): 
        x0 = np.random.uniform(low =- 10, high = 10, size=(2,))  # 𝑥0 ∈[−10,10]×[−10,10]
        x = gd(x0, n) 

        if (best is None) or (function(x[0], x[1]) < function(best[0], best[1])): 
            best = x 
    return x 

for exp in range(3):  
    print(f'Experiment: {exp+1}') 
    for n in [0.1, 0.01, 0.001]: 
        x = trails(n) 
        print(f'\tη: {n}')
        print('\t\tPoint:',(x[0], x[1]),'\n\t\tf(x, y):' ,function(x[0], x[1]))
