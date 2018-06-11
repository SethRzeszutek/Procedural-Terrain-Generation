import pygame, sys, random, math
from pygame.locals import *
from opensimplex import OpenSimplex





#useful game dimensions
TILESIZE  = 1
MAPWIDTH  = 500
MAPHEIGHT = 500

test=1
mousepressed = False

gen = OpenSimplex(seed=(random.randint(0,500)))
def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5
def generateNoise(height, width):
    fullvalue = []
    for y in range(height):
        #print("Went through y:", y)
        value = []
        for x in range(width):
            #print("Went through x", x)
            nx = x/width - 0.5
            ny = y/height - 0.5
            e = 1 * noise(1 * nx, 1 * ny) +  0.5 * noise(2 * nx, 2 * ny) + 0.25 * noise(4 * nx, 4 * ny);
            math.pow(e, 2.75)
            value.append(round(e,2))
        fullvalue.append(value)
    return fullvalue

def veiwNoiseText(value):
    for y in value:
        print(y)

def matrixRatio(matrix):
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

textures =   {
                #DIRT   : pygame.image.load('dirt.png'),
                #GRASS : pygame.image.load('grass.png'),
                #WATER : pygame.image.load('water.png'),
                #COAL  : pygame.image.load('coal.png')
            }

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



#a list of resources
resources = [DIRT,GRASS,DEEPWATER,MEDWATER,SHALLOWWATER,COAL,SAND,TALLGRASS, SANDYGRASS, MOUNTAIN, SNOWCAP]
#use list comprehension to create our tilemap
tilemap = [[DIRT for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#set up the display
pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILESIZE,MAPHEIGHT*TILESIZE))




noiseMatrix = generateNoise(MAPHEIGHT,MAPWIDTH)
#veiwNoiseText(noiseMatrix)
matrixRatio(noiseMatrix)

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

#loop through each row
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
        '''
        if(noiseMatrix[row][column] > 0 and noiseMatrix[row][column] < 0.4):
            tile = HEIGHTONE
        elif(noiseMatrix[row][column] >= 0.4 and noiseMatrix[row][column] < 0.5):
            tile = HEIGHTTWO
        elif(noiseMatrix[row][column] >= 0.5 and noiseMatrix[row][column] < 0.6):
            tile = HEIGHTTHREE
        elif(noiseMatrix[row][column] >= 0.6 and noiseMatrix[row][column] < 0.7):
            tile = HEIGHTFOUR
        elif(noiseMatrix[row][column] >= 0.7 and noiseMatrix[row][column] < 0.8):
            tile = HEIGHTFIVE
        elif(noiseMatrix[row][column] >= 0.8 and noiseMatrix[row][column] < 9):
            tile = HEIGHTSIX
        elif(noiseMatrix[row][column] >= 0.9 and noiseMatrix[row][column] < 1):
            tile = HEIGHTSEVEN
        elif(noiseMatrix[row][column] >= 1 and noiseMatrix[row][column] < 1.1):
            tile = HEIGHTEIGHT
        elif(noiseMatrix[row][column] >= 1.1 and noiseMatrix[row][column] < 2):
            tile = HEIGHTNINE
        else:
            tile = COAL
        '''
        tilemap[row][column] = tile






'''
    for column in range(MAPWIDTH):
        if(noiseMatrix[row][column] > 0 and noiseMatrix[row][column] < 0.4):
            tile = WATER
        elif(noiseMatrix[row][column] >= 0.4 and noiseMatrix[row][column] < 0.5):
            tile = WATER
        elif(noiseMatrix[row][column] >= 0.5 and noiseMatrix[row][column] < 0.6):
            tile = SAND
        elif(noiseMatrix[row][column] >= 0.6 and noiseMatrix[row][column] < 0.7):
            tile = GRASS
        elif(noiseMatrix[row][column] >= 0.7 and noiseMatrix[row][column] < 0.8):
            tile = TALLGRASS
        elif(noiseMatrix[row][column] >= 0.9 and noiseMatrix[row][column] < 1):
            tile = GRASS
        elif(noiseMatrix[row][column] >= 1 and noiseMatrix[row][column] < 1.1):
            tile = SAND
        elif(noiseMatrix[row][column] >= 1.1 and noiseMatrix[row][column] < 2):
            tile = WATER
        else:
            tile = WATER
        '''
        #set the position in the tilemap to the randomly chosen tile
        #tilemap[row][column] = tile

while True:
    #get all the user events
    for event in pygame.event.get():
        #if the user wants to quit
        if event.type == QUIT:
            #and the game and close the window
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepressed = True
            x,y= event.pos
            print((x, y))
        if event.type == pygame.MOUSEBUTTONUP:
            mousepressed = False
    #print("You Made it almost to the end!")

    #loop through each row
    if(test==1):
        for row in range(MAPHEIGHT):
            #loop through each column in the row
            for column in range(MAPWIDTH):
                #draw the resource at that position in the tilemap, using the correct image
                #DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILESIZE,row*TILESIZE))
                screen=pygame.draw.rect(DISPLAYSURF, color[tilemap[row][column]], (column*TILESIZE,row*TILESIZE,TILESIZE,TILESIZE))
    test+=1
    if mousepressed:
        x,y= event.pos
        #print((x, y))

    #update the display
    pygame.display.update()
