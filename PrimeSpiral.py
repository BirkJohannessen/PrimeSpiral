import math
import numpy as np
import scipy.misc as smp
import sympy
from PIL import Image, ImageColor

dimX=4000
dimY=3000
origoX=int(dimX/2)
origoY=int(dimY/2)


def createGraph(list, name):
    img = Image.new('RGB', (dimX,dimY),(0,0,0))

    for i in list:
        x,y=calcXY(i)
        if(x<dimX and x>0 and y<dimY and y>0):
            drawPlus(x,y,img, 'white')

    img.save(name)


def drawPlus(x,y, img, color):
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter
    if x+1<dimX:
        img.putpixel((x+1, y), ImageColor.getcolor(color, 'RGB')) #høyre
    if x-1>0:
        img.putpixel((x-1, y), ImageColor.getcolor(color, 'RGB')) #venste
    if y+1<dimY:
        img.putpixel((x, y+1), ImageColor.getcolor(color, 'RGB')) #opp
    if y-1>0:
        img.putpixel((x, y-1), ImageColor.getcolor(color, 'RGB')) #ned


def calcXY(i):
    radius = i
    x = int(radius*math.cos(i)+origoX)
    y = int(radius*math.sin(i)+origoY)
    return x,y

def drawOrigo(img, color):
    img.putpixel((int(origoX), int(origoY)), ImageColor.getcolor(color, 'RGB')) #senter

def drawAxis(img, color):
    for i in range(0,dimX-1):
        img.putpixel((int(origoX),int(i)),ImageColor.getcolor(color, 'RGB'))
        img.putpixel((int(i),int(origoY)),ImageColor.getcolor(color, 'RGB'))

if __name__ == "__main__":
    primes=list(sympy.primerange(0,10000))
    naturals=list(range(0,10000))
    createGraph(primes, 'PrimeSpiral.png')
    createGraph(naturals, 'Nspiral.png')