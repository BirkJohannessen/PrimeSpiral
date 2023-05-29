import math
import sys
import sympy
from PIL import Image, ImageColor


backgroundColor=(0,0,0)
primeColor= 'Turquoise'  #Turquoise




def createGraph(list, name, scale, dimX, dimY, dotType):
    #noen faste brukte verdier
    origoX=int(dimX/2)
    origoY=int(dimY/2)
    img = Image.new('RGB', (dimX,dimY),backgroundColor) #canvas

    if dotType == "1":
        for i in list:
            x,y=calcXY(i, scale, origoX, origoY)
            if(x<dimX and x>0 and y<dimY and y>0): #skjekker at verdien ikke er utenfor canvas
                drawDot(x,y,img, primeColor)
    if dotType == "2":
        for i in list:
            x,y=calcXY(i, scale, origoX, origoY)
            if(x<dimX and x>0 and y<dimY and y>0): #skjekker at verdien ikke er utenfor canvas
                drawPlus(x,y,img, primeColor, dimX, dimY)
    if dotType == "3":
        for i in list:
            x,y=calcXY(i, scale, origoX, origoY)
            if(x<dimX and x>0 and y<dimY and y>0): #skjekker at verdien ikke er utenfor canvas
                drawStar(x,y,img, primeColor, dimX, dimY)
    img.save(name)


def calcXY(i, scale, origoX, origoY): #omregner (radius,radian) til (x,y)
    radius = i
    x = int(((radius*math.cos(i))*-1/scale)+(origoX))   #*-1 for å rette opp aksene
    y = int(((radius*math.sin(i))*-1/scale+(origoY)))
    return x,y

#litt forskjellige former å tegne på
def drawDot(x,y,img,color):
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter

def drawPlus(x,y, img, color, dimX, dimY): #tegner en + i grafen.
    img.putpixel((x, y), ImageColor.getcolor(color, 'RGB')) #senter
    if x+1<dimX and x-1>0 and y+1<dimY and y-1>0:
        img.putpixel((x+1, y), ImageColor.getcolor(color, 'RGB')) #høyre
        img.putpixel((x-1, y), ImageColor.getcolor(color, 'RGB')) #venste
        img.putpixel((x, y+1), ImageColor.getcolor(color, 'RGB')) #opp
        img.putpixel((x, y-1), ImageColor.getcolor(color, 'RGB')) #ned

def drawStar(x,y, img, color, dimx, dimY): #tegner en stor piksel i grafen.
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
    #print(len(primeList))
    #print(primeList[-1])
    print("STARTING PrimeSpiral!")

    primeRange = int(sys.argv[1])
    downScaler = int(sys.argv[2])

    print("Calculating primes .. ")
    primeList = list(sympy.primerange(0, primeRange)) #tabell av primtall

    dotRadius = sys.argv[3]
    filename = 'PRIME_' + str(primeRange) + '.png'
    biggestPrime = primeList[-1]
    #bilde dimensjon, endre etter behov
    dimX=int(15360/downScaler)  #16k=15360x8640
    dimY=int(8640/downScaler)
    pixelRadius=int(math.sqrt((dimX/2)**2+(dimY/2)**2)) #Pytagoras for å få avstand fra origo til hjørnet
    scale = biggestPrime/pixelRadius


    print("Drawing the canvas ..")






    createGraph(primeList, filename, scale, dimX, dimY, dotRadius)

