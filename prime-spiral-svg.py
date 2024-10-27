import math
import sys
import sympy

def drawDot(x, y, radius, primeColor):
    circle = '<circle cx="{cx}" cy="{cy}" r="{r}" fill="#77727D" stroke="#77727D"/>'
    circle = circle.format(cx = x, cy = y, r = radius)
    return circle;

def svg(list, filename, scale, dimX, dimY, radius):
    origoX=int(dimX/2)
    origoY=int(dimY/2)

    f = open(filename, "a")
    svg = '<svg version="1.1" width="{x}" height="{y}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {x} {y}" preserveAspectRatio="slice">\n'
    svg = svg.format(x = dimX, y = dimY)
    f.write(svg)

    for i in list:
        x,y=calcXY(i, scale, origoX, origoY)
        if (x<dimX and x>0 and y<dimY and y>0): #skjekker at verdien ikke er utenfor canvas
            f.write(drawDot(x,y, radius, 'empty arg') + '\n')

    f.write('</svg>')
    f.close()

def calcXY(i, scale, origoX, origoY): #omregner (radius,radian) til (x,y)
    radius = i
    x = int(((radius*math.cos(i))*-1/scale)+(origoX))   #*-1 for å rette opp aksene
    y = int(((radius*math.sin(i))*-1/scale+(origoY)))
    return x,y

def calc(primeRange):
    print("Calculating primes ({range}).. ".format(range = primeRange))
    primeList = list(sympy.primerange(0, primeRange)) #tabell av primtall

    filename = 'PRIME_{range}.svg'
    filename = filename.format(range = str(primeRange))
    biggestPrime = primeList[-1]
    #bilde dimensjon, endre etter behov
    downScaler = downScale(primeRange)
    dimX=int(15360/downScaler)  #16k=15360x8640
    dimY=int(8640/downScaler)
    pixelRadius=int(math.sqrt((dimX/2)**2+(dimY/2)**2)) #Pytagoras for å få avstand fra origo til hjørnet
    scale = biggestPrime/pixelRadius
    print("generating svg...")
    svg(primeList, filename, scale, dimX, dimY, radiusScale(primeRange))
    print("done!")

def radiusScale(range):
    return 2

def downScale(range):
    if ranger(0, 128, range):
        return 16
    if ranger(128, 2048, range):
        return 8
    if ranger(2048, 65565, range):
        return 8
    if ranger(2048, 65536, range):
        return 4
    if ranger(65536, 524288, range):
        return 2
    return 1

def ranger(x, y, i):
    return i >= x and y > i


if __name__ == "__main__":
    #print(len(primeList))
    #print(primeList[-1])
    print("STARTING (svg) PrimeSpiral!")

    # primeRange = int(sys.argv[1])
    # downScaler = int(sys.argv[1])
    # radius = int(sys.argv[2])

    range = list(range(20))

    for i in range:
        calc(i)

