import pygame, sys, random, math
from pygame.locals import *
from opensimplex import OpenSimplex







#useful game dimensions
TILESIZE  = 3
MAPWIDTH  = 200
MAPHEIGHT = 200
#constants representing colours
BLACK = (0,   0,   0)
BROWN = (153, 76,  0)
GREEN = (80,   161, 55)
BLUE  = (0,   76,   153)
SANDY = (238, 217, 135)
SANDYGRASS = (204,204,102)
DGREEN = (74, 131, 57)
OCEANBLUEONE=(0,102,204)
OCEANBLUETWO=(0,128,255)
OCEANBLUETHREE=(51,153,255)
MGREEN=(40,48,41)
SNOW=(192,192,192)

#HEIGHTCOLORS
HRED = (255,51,51)
HORANGE = (255,153,51)
HYELLOW = (255,255,51)
HGREENONE = (153,255,51)
HGREENTWO = (51,255,51)     #Second Most Populous
HGREENTHREE = (51,255,153)  #Most Populous,so Water this point and below
HBLUEONE = (51,255,255)
HBLUETWO = (51,153,255)
HBLUETHREE = (51,51,255)

#constants representing the different resources
DIRT = 0
GRASS = 1
DEEPWATER = 2
MEDWATER = 3
SHALLOWWATER = 4
BEACHGRASS = 5
COAL = 6
SAND = 7
TALLGRASS = 8
MOUNTAIN = 9
SNOWCAP = 10

HEIGHTONE = 11
HEIGHTTWO = 12
HEIGHTTHREE = 13
HEIGHTFOUR = 14
HEIGHTFIVE = 15
HEIGHTSIX = 16
HEIGHTSEVEN = 17
HEIGHTEIGHT = 18
HEIGHTNINE = 19

#a dictionary linking resources to textures
color =   {
                DIRT:           BROWN,
                GRASS:          GREEN,
                DEEPWATER:      OCEANBLUEONE,
                MEDWATER:       OCEANBLUETWO,
                SHALLOWWATER:   OCEANBLUETHREE,
                COAL:           BLACK,
                SAND:           SANDY,
                TALLGRASS:      DGREEN,
                BEACHGRASS:     SANDYGRASS,
                MOUNTAIN:       MGREEN,
                SNOWCAP:        SNOW

    #HEIGHTMAP
                #HEIGHTONE:      HRED,
                #HEIGHTTWO:      HORANGE,
                #HEIGHTTHREE:    HYELLOW,
                #HEIGHTFOUR:     HGREENONE,
                #HEIGHTFIVE:     HGREENTWO,
                #HEIGHTSIX:      HGREENTHREE,
                #HEIGHTSEVEN:    HBLUEONE,
                #HEIGHTEIGHT:    HBLUETWO,
                #HEIGHTNINE:     HBLUETHREE
            }


test=1
mousepressed = False


def noise(nx, ny, gen):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

def generateNoise(height, width):
    '''
    :param height: Height of Matrix
    :param width: Width of Matrix
    :return: The full Matrix of values
    '''
    gen = OpenSimplex(seed=(random.randint(0,500)))
    fullvalue = []
    for y in range(height):
        #print("Went through y:", y)
        value = []
        for x in range(width):
            #print("Went through x", x)
            nx = x/width - 0.5
            ny = y/height - 0.5
            #e= random.uniform(0.3, 1.9)
            e = 1 * noise(1 * nx, 1 * ny,gen) +  0.5 * noise(2 * nx, 2 * ny,gen) + 0.25 * noise(4 * nx, 4 * ny,gen)
            math.pow(e, 2.75)
            value.append(round(e,2))
        fullvalue.append(value)
    return fullvalue

def veiwNoiseText(value):
    for y in value:
        print(y)

def matrixRatio(noiseMatrix):
    zero=0
    one=0
    two=0
    three=0
    four=0
    five=0
    six=0
    seven=0
    eight=0
    nine=0
    errorValue = 0
    for row in range(MAPHEIGHT):
    #loop through each column in that row
            for column in range(MAPWIDTH):
                if(noiseMatrix[row][column] > 0 and noiseMatrix[row][column] < 0.4):
                    zero+=1
                elif(noiseMatrix[row][column] >= 0.4 and noiseMatrix[row][column] < 0.5):
                    one+=1
                elif(noiseMatrix[row][column] >= 0.5 and noiseMatrix[row][column] < 0.6):
                    two+=1
                elif(noiseMatrix[row][column] >= 0.6 and noiseMatrix[row][column] < 0.7):
                    three+=1
                elif(noiseMatrix[row][column] >= 0.7 and noiseMatrix[row][column] < 0.8):
                    four+=1
                elif(noiseMatrix[row][column] >= 0.8 and noiseMatrix[row][column] < 0.9):
                    five+=1
                elif(noiseMatrix[row][column] >= 0.9 and noiseMatrix[row][column] < 1):
                    six+=1
                elif(noiseMatrix[row][column] >= 1 and noiseMatrix[row][column] < 1.1):
                    seven+=1
                elif(noiseMatrix[row][column] >= 1.1 and noiseMatrix[row][column] < 2):
                    eight+=1
                else:
                    errorValue+=1
    print("Percentage of Appearances:")
    print("0.0-0.4 =", (zero*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.4-0.5 =", (one*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.5-0.6 =", (two*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.6-0.7 =", (three*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.7-0.8 =", (four*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.8-0.9 =", (five*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("0.9-1.0 =", (six*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("1.0-1.1 =", (seven*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("1.1-2.0 =", (eight*(1/(MAPHEIGHT*MAPWIDTH))*100))
    print("Error values = ", errorValue)



def castleCreator(castleLocations):
    for location in castleLocations:
            #Made for TILESIZE 3, Map size 200x200
            castleLeft = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0], location[1], TILESIZE*1.7, TILESIZE*-3.5), 0)
            castleRight = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0]+10, location[1], TILESIZE*1.7, TILESIZE*-3.5), 0)
            castleMain = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0], location[1], TILESIZE*4, TILESIZE*-1.7), 0)

            #Made for TILESIZE 10, Map size 100x100
            #castleLeft = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0], location[1], TILESIZE*.65, TILESIZE*-1.20), 0)
            #castleRight = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0]+8, location[1], TILESIZE*.65, TILESIZE*-1.20), 0)
            #castleMain = pygame.draw.rect(DISPLAYSURF, (211,211,211), (location[0], location[1], TILESIZE*1.50, TILESIZE*-.75), 0)

def cityCreator(cityLocations):
    for city in cityLocations:
            #Made for TILESIZE 10, Map size 100x100
            newcity = pygame.draw.polygon(DISPLAYSURF, (205,133,63), [[city[0], city[1]], [city[0]-5, city[1]+7], [city[0]+5, city[1]+7]], 0)

def riverCreator(riverStart, riverEnd):
    if riverStart != (0,0) and riverEnd != (0,0):
        pygame.draw.lines(DISPLAYSURF, OCEANBLUETHREE, False, [riverStart,riverEnd],0)
        #pygame.draw.arc(DISPLAYSURF, BLACK,[210, 75, 150, 125], 0, 3.14/2, 2)



#a list of resources NOT USED
resources = [DIRT,GRASS,DEEPWATER,MEDWATER,SHALLOWWATER,COAL,SAND,TALLGRASS, SANDYGRASS, MOUNTAIN, SNOWCAP]
#use list comprehension to create our tilemap
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))




'''
Decent Example ratio 1000/1000
0.1 = 10.12 instances
0.2 = 12.70 instances
0.3 = 15.10 instances
0.4 = 16.53 instances
0.5 = 14.38 instances
0.6 = 14.45 instances
0.7 = 16.46 instances
0.8 = .26 instances
'''

def mainCreator(test):
    #loop through each row
    noiseMatrix = generateNoise(MAPHEIGHT,MAPWIDTH)
    #veiwNoiseText(noiseMatrix)
    #matrixRatio(noiseMatrix)
    for row in range(MAPHEIGHT):
        #loop through each column in that row
        for column in range(MAPWIDTH):
            if(noiseMatrix[row][column] > 0 and noiseMatrix[row][column] < 0.4):
                tile = SNOWCAP
            elif(noiseMatrix[row][column] >= 0.4 and noiseMatrix[row][column] < 0.5):
                tile = MOUNTAIN
            elif(noiseMatrix[row][column] >= 0.5 and noiseMatrix[row][column] < 0.6):
                tile = TALLGRASS
            elif(noiseMatrix[row][column] >= 0.6 and noiseMatrix[row][column] < 0.7):
                tile = GRASS
            elif(noiseMatrix[row][column] >= 0.7 and noiseMatrix[row][column] < 0.8):
                tile = BEACHGRASS
            elif(noiseMatrix[row][column] >= 0.8 and noiseMatrix[row][column] < 0.9):
                tile = SAND
            elif(noiseMatrix[row][column] >= 0.9 and noiseMatrix[row][column] < 1):
                tile = SHALLOWWATER
            elif(noiseMatrix[row][column] >= 1 and noiseMatrix[row][column] < 1.1):
                tile = MEDWATER
            elif(noiseMatrix[row][column] >= 1.1 and noiseMatrix[row][column] < 2):
                tile = DEEPWATER
            else:
                tile = COAL
            #set the position in the tilemap to the randomly chosen tile
            tilemap[row][column] = tile
    while True:
        #get all the user events
        for event in pygame.event.get():
            #if the user wants to quit
            if event.type == QUIT:
                #and the game and close the window
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #mousepressed = True
                x,y= event.pos
                colorCursor = DISPLAYSURF.get_at((x,y))
                pygame.draw.circle(DISPLAYSURF, (255,51,51), (x,y),TILESIZE+1)
                if restartButton.collidepoint((x,y)):
                    mainCreator(1)
                if exitButton.collidepoint((x,y)):
                    pygame.quit()
                    sys.exit()
                print((x, y))
                #print(colorCursor)
        #loop through each row
        screen=pygame.draw.rect(DISPLAYSURF, color[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
        castleCount = 5
        cityCount = 12
        tempCountCastle = 0
        tempCountCity = 0
        tempOcean = 0
        tempJungle = 0
        oceanShallowsLocation = (0,0)
        jungleLocation = (0,0)
        castleLocationArray=[]
        cityLocationArray=[]
        #castleImg = pygame.image.load('CastleNewResize.png')
        if(test==1):
            for row in range(MAPHEIGHT):
                #loop through each column in the row
                for column in range(MAPWIDTH):
                    #draw the resource at that position in the tilemap, using the correct image
                    screen=pygame.draw.rect(DISPLAYSURF, color[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
                    if((color[tilemap[row][column]] == DGREEN or color[tilemap[row][column]] == GREEN) and (random.randint(0,100) <= 10)):
                        tempCountCastle += 1
                        if tempCountCastle == 120:
                            #raise if size of map is increased 20 works well for TILESIZE 10 and Mapsize 100x100
                            if castleCount != 0:
                                castleLocationArray.append((screen.x,screen.y))
                                castleCount -= 1
                            tempCountCastle=0
                    if (color[tilemap[row][column]] == DGREEN or color[tilemap[row][column]] == GREEN) and (random.randint(0,100) <= 10):
                        tempCountCity += 1
                        if tempCountCity == 80:
                            #raise if size of map is increased 20 works well for TILESIZE 10 and Mapsize 100x100
                            if cityCount != 0:
                                cityLocationArray.append((screen.x ,screen.y))
                                cityCount -= 1
                            tempCountCity=0
                    if color[tilemap[row][column]] == OCEANBLUETHREE and (random.randint(0,10000) <= 5) and tempOcean==0:
                        oceanShallowsLocation = (screen.x ,screen.y)
                        tempOcean += 1
                    if color[tilemap[row][column]] == MGREEN and (random.randint(0,10000) <= 5) and tempJungle==0:
                        jungleLocation = (screen.x ,screen.y)
                        tempJungle += 1


            riverCreator(jungleLocation,oceanShallowsLocation)
            castleCreator(castleLocationArray)
            cityCreator(cityLocationArray)



        test+=1

        #Made for TILESIZE 10 and MAPSIZE 100x100
        #exitButton = pygame.draw.rect(DISPLAYSURF, (178,34,34), (screen.x-65, screen.y-12, TILESIZE+(TILESIZE*15), TILESIZE+50), 0)
        #restartButton = pygame.draw.rect(DISPLAYSURF, (127,255,212), (screen.x-65, screen.y-32, TILESIZE+(TILESIZE*15), TILESIZE+14), 0)
        exitButton = pygame.draw.rect(DISPLAYSURF, (178,34,34), (screen.x-65, screen.y-16, TILESIZE+(TILESIZE*25), TILESIZE+50), 0)
        restartButton = pygame.draw.rect(DISPLAYSURF, (127,255,212), (screen.x-65, screen.y-36, TILESIZE+(TILESIZE*25), TILESIZE+17), 0)


        #update the display
        pygame.display.update()

mainCreator(test)
