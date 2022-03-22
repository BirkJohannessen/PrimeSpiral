import math
import sympy
from PIL import Image, ImageColor


primeRange=50000


#bilde dimensjon, endre etter behov
dimX=int(15360/2)  #16k=15360x8640
dimY=int(8640/2)
backgroundColor=(0,0,0)
primeColor= 'white'  #Turquoise


#noen faste brukte verdier
primeList = list(sympy.primerange(0, primeRange)) #tabell av primtall
origoX=int(dimX/2)
origoY=int(dimY/2)
pixelRadius=int(math.sqrt((dimX/2)**2+(dimY/2)**2)) #Pytagoras for å få avstand fra origo til hjørnet
biggestPrime = primeList[-1]
scale=biggestPrime/pixelRadius



def createGraph(list, name):
    img = Image.new('RGB', (dimX,dimY),backgroundColor) #canvas
    #for i in range(0,primeRange):
    #    x,y=calcXY(i)
    #    if(x<dimX and x>0 and y<dimY and y>0):
    #        drawStar(x,y,img, 'blue')
    for i in list:
        x,y=calcXY(i)
        if(x<dimX and x>0 and y<dimY and y>0): #skjekker at verdien ikke er utenfor canvas
            drawStar(x,y,img, primeColor)

    img.save(name)


def calcXY(i): #omregner (radius,radian) til (x,y)
    radius = i
    x = int(((radius*math.cos(i))*-1/scale)+(origoX))   #*-1 for å rette opp aksene
    y = int(((radius*math.sin(i))*-1/scale+(origoY)))
    return x,y

#litt forskjellige former å tegne på
def drawDot(x,y,img,color):
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter

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



if __name__ == "__main__":
    print(len(primeList))
    print(primeList[-1])
    createGraph(primeList, 'Prime8ktest.png')
