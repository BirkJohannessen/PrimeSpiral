import math
import numpy as np
import scipy.misc as smp
import sympy
from PIL import Image, ImageColor

dimX=4000
dimY=4000
origoX=dimX/2
origoY=dimY/2


def createPrimeSpiral():
    primes=list(sympy.primerange(2,int((dimY/2))))
    img = Image.new('RGB', (dimX,dimY),(0,0,0))

    for prime in primes:
        x,y=calcXY(prime)
        drawPlus(x,y,img, 'white')

    img.save('PrimeSpiral.png')

def createNSpiral():
    N=list(range(0,int(origoY)))
    img = Image.new('RGB', (dimX,dimY),(0,0,0))

    for n in N:
        x, y = calcXY(n)
        if n==397:
            drawPlus(x,y,img,'red')
        else:
            drawPlus(x,y,img,'white')

    img.save('Nspiral.png')

def drawPlus(x,y, img, color):
    img.putpixel((int(origoX + x), int(origoY + y)), ImageColor.getcolor(color, 'RGB')) #senter
    img.putpixel((int(origoX + x+1), int(origoY + y)), ImageColor.getcolor(color, 'RGB')) #høyre
    img.putpixel((int(origoX + x-1), int(origoY + y)), ImageColor.getcolor(color, 'RGB')) #venste
    img.putpixel((int(origoX + x), int(origoY + y+1)), ImageColor.getcolor(color, 'RGB')) #opp
    img.putpixel((int(origoX + x), int(origoY + y-1)), ImageColor.getcolor(color, 'RGB')) #ned


def calcXY(prime):
    radius = prime
    x = radius*math.cos(prime)
    y = radius*math.sin(prime)
    return x,y

def drawOrigo(img, color):
    img.putpixel((int(origoX), int(origoY)), ImageColor.getcolor(color, 'RGB')) #senter

def drawAxis(img, color):
    for i in range(0,dimX-1):
        img.putpixel((int(origoX),int(i)),ImageColor.getcolor(color, 'RGB'))
        img.putpixel((int(i),int(origoY)),ImageColor.getcolor(color, 'RGB'))

if __name__ == "__main__":
    createPrimeSpiral()
    createNSpiral()