import math
import numpy as np
import scipy.misc as smp
import sympy

dimX=1024
dimY=1024

origoX=dimX/2
origoY=dimY/2


def main():
    primes=list(sympy.primerange(0,500))
    primetall={3,5,7,11,13,17,19}
    data= np.zeros((dimX,dimY,3), dtype=np.uint8)


    for prime in primetall:
        x,y=calcXY(prime)
        data[origoX+x,origoY+y] = [0,0,255]

    #img = smp.toimage( data )
    #img.show()

def calcXY(prime):
    radius = prime
    x = radius*math.cos(prime)
    y = radius*math.sin(prime)
    return x,y

if __name__ == "__main__":
    main()