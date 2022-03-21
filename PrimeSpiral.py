import math
import sympy
from PIL import Image, ImageColor
primerange=100000000
scale=30000

dimX=6000
dimY=3000
origoX=int(dimX/2)
origoY=int(dimY/2)

def createGraph(list, name):
    img = Image.new('RGB', (dimX,dimY),(0,0,0))

    for i in list:
        x,y=calcXY(i)
        x=int(x)
        y=int(y)
        if(x<dimX and x>0 and y<dimY and y>0):
            drawPlus(x,y,img, 'turquoise')

    img.save(name)


def drawPlus(x,y, img, color): #tegner en + i grafen.
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter
    if x+1<dimX and x-1>0 and y+1<dimY and y-1>0:
        img.putpixel((x+1, y), ImageColor.getcolor(color, 'RGB')) #høyre
        img.putpixel((x-1, y), ImageColor.getcolor(color, 'RGB')) #venste
        img.putpixel((x, y+1), ImageColor.getcolor(color, 'RGB')) #opp
        img.putpixel((x, y-1), ImageColor.getcolor(color, 'RGB')) #ned

def drawStar(x,y, img, color): #tegner en stor piksel i grafen.
    if x+2<dimX and x-2>0 and y+2<dimY and y-2>0:
        img.putpixel((x, y), ImageColor.getcolor(color, 'RGB'))  # senter

        img.putpixel((x+1, y), ImageColor.getcolor(color, 'RGB')) #høyre
        img.putpixel((x-1, y), ImageColor.getcolor(color, 'RGB')) #venste
        img.putpixel((x, y+1), ImageColor.getcolor(color, 'RGB')) #opp
        img.putpixel((x, y-1), ImageColor.getcolor(color, 'RGB')) #ned

        img.putpixel((x, y-2), ImageColor.getcolor(color, 'RGB')) #nedned
        img.putpixel((x, y+2), ImageColor.getcolor(color, 'RGB')) #oppopp
        img.putpixel((x+2, y), ImageColor.getcolor(color, 'RGB')) #høyhøy
        img.putpixel((x-2, y), ImageColor.getcolor(color, 'RGB')) #venven

        img.putpixel((x+1, y-1), ImageColor.getcolor(color, 'RGB')) #oppven
        img.putpixel((x+1, y+1), ImageColor.getcolor(color, 'RGB')) #opphøy
        img.putpixel((x-1, y+1), ImageColor.getcolor(color, 'RGB')) #nedven
        img.putpixel((x-1, y-1), ImageColor.getcolor(color, 'RGB')) #nedhøy



def calcXY(i): #omregner (radius,radian) til (x,y)
    radius = i
    x = int((radius*math.cos(i))/scale+origoX)
    y = int((radius*math.sin(i))/scale+origoY)
    return x,y

if __name__ == "__main__":
    primes=list(sympy.primerange(0,primerange))
    print(len(primes))
    createGraph(primes, 'PrimeSpiral5mill2.png')
