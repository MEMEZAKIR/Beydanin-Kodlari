import numpy as np

def birbir():
    sıfır = np.zeros((5,5), dtype=int)
    print(sıfır)
    
    bir = np.ones((2,3), dtype=int)
    print(bir)

def iki():
    on = np.ones((2,3), dtype=int)*10
    print(on)
    
    yirmi = np.full((4,4), 20, dtype=int)
    print(yirmi)

def birim_matris():
    birim = np.eye(4)
    print(birim)

def diagonel_matris():
    diagon = np.diag([1,2,3,4,5])
    print(diagon)
    
