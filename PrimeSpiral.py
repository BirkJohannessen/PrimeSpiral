import math
import sympy
from PIL import Image, ImageColor
dimBigX=6000
dimBigY=3000
scale=19

dimX=7000
dimY=4000
origoX=int(dimX/2)
origoY=int(dimY/2)

def createBigGraph(list, name):
    img = Image.new('RGB', (dimBigX, dimBigY), (0, 0, 0))

    for i in list:
        x, y = calcXY(i)
        x=int(((x-origoX)+(dimBigX/2)))
        y=int(((y-origoY)+(dimBigY/2)))
        if (x < dimBigX and x > 0 and y < dimBigY and y > 0):
            drawStar(x, y, img, 'turquoise')

    img.save(name)

def createGraph(list, name):
    img = Image.new('RGB', (dimX,dimY),(0,0,0))

    for i in list:
        x,y=calcXY(i)
        x=int(x)
        y=int(y)
        if(x<dimX and x>0 and y<dimY and y>0):
            drawStar(x,y,img, 'white')

    img.save(name)


def drawPlus(x,y, img, color): #tegner en + i grafen.
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter
    if x+1<dimX and x-1>0 and y+1<dimY and y-1>0:
        img.putpixel((x+1, y), ImageColor.getcolor(color, 'RGB')) #høyre
        img.putpixel((x-1, y), ImageColor.getcolor(color, 'RGB')) #venste
        img.putpixel((x, y+1), ImageColor.getcolor(color, 'RGB')) #opp
        img.putpixel((x, y-1), ImageColor.getcolor(color, 'RGB')) #ned

def drawStar(x,y, img, color): #tegner en stor piksel i grafen.
    if x+2<dimBigX and x-2>0 and y+2<dimBigY and y-2>0:
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

def drawOrigo(img, color): #legg til i koden for å få en prikk i origo.
    img.putpixel((int(origoX), int(origoY)), ImageColor.getcolor(color, 'RGB')) #senter

def drawAxis(img, color): #legg til i koden for å få koordinatakser
    for i in range(0,dimX-1):
        img.putpixel((int(origoX),int(i)),ImageColor.getcolor(color, 'RGB'))
        img.putpixel((int(i),int(origoY)),ImageColor.getcolor(color, 'RGB'))

if __name__ == "__main__":
    primes=list(sympy.primerange(0,150000))
    naturals=list(range(0,150000))
    createGraph(primes, 'PrimeSpiral.png')
    createGraph(naturals, 'Nspiral.png')
    #createBigGraph(primes, 'bigPrimeSpiral.png')
    createBigGraph(naturals, 'bigNspiral.png')