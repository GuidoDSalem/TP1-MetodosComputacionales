
from matricesRalas import *
import numpy as np

def getMatD(W:MatrizRala)->MatrizRala:

    pass
def getMatDNump(W:np.ndarray)->np.ndarray:
    D = np.zeros_like(W)
    for i in range(D.shape[0]):
        D[i,i] = sum(W[i,:])
    return D
    
def nextP(P:np.ndarray,W,D,d)->np.ndarray:
    termino_1 = 1-d / W.shape[0]
    termino_1 = np.zeros_like(P) + 1 * termino_1
    termino_2 = d * W @ D @ P
    return termino_1 + termino_2


def mainNumpy():
    N = 11
    d = 0.85
    W = np.zeros((N,N))
    P = np.zeros((N,1)) + 1

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

    print(W,sep="\n")
    print(P)
    
    D = getMatDNump(W)
    print(D)

    print("INICIO: \n")
    print(P)
    for i in range(10):
        newP = nextP(P,W,D,d)
        # print(newP - P)
        print("DIF: ")
        print(sum(newP - P))
        P = newP









    

    # print(W)
    # print(type(W))

    pass

def main():
    N = 11
    d = 0.85
    W = MatrizRala(N,N)

    

    print(W.__repr__())

    pass

if __name__ == "__main__":
    mainNumpy()
    # main()