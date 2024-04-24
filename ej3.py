
from matricesRalas import *
import numpy as np

def getMatD(W:MatrizRala)->MatrizRala:

    pass
def getMatNump(W:np.ndarray)->np.ndarray:
    
    pass

def mainNumpy():
    N = 11
    W = np.zeros((N,N))

    # CITAS A-0
    W[0][2] = 1
    W[0][3] = 1
    W[0][4] = 1

    # CITAS B-1
    W[1][0] = 1

    # CITAS C-2

    # CITAS D-3

    # CITAS E-4
    W[4][10] = 1

    # CITAS F-5
    W[5][0] = 1
    W[5][6] = 1

    # CITAS G-6
    W[6][7] = 1
    W[6][8] = 1

    # CITAS H-7
    W[7][8] = 1

    # CITAS I-8
    W[8][5] = 1

    # CITAS J-9
    W[9][8] = 1
 

    # CITAS K-10

    print(W)
    print(W[0,:])
    print(np.sum(W[0,:]))





    

    # print(W)
    # print(type(W))

    pass

def main():
    N = 11
    W = MatrizRala(N,N)
    print(W.__repr__())

    pass

if __name__ == "__main__":
    mainNumpy()
    # main()