import random, time
import mcpi.minecraft as minecraft
import mcpi.block as block
import matrixkeypad
mc = minecraft.Minecraft.create()  

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

D2 = 17
D3 = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
D8 = 25
D9 = 4
D10 = 8
A3 = 7

#GPIO.setup(D3, GPIO.IN)
    
def volcano():
    loc = mc.player.getPos()

    #randomise the center of the volcano
    loc.x = loc.x + random.randrange(-7,8)
    loc.y = loc.y
    loc.z = loc.z + random.randrange(-7,8)

    mc.setBlocks(loc.x-3, loc.y, loc.z-3,
                 loc.x+3, loc.y+1, loc.z+3,
                 block.DIRT)
    time.sleep(2)

    mc.setBlocks(loc.x-2, loc.y+2, loc.z-2,
             loc.x+2, loc.y+3, loc.z+2,
             block.DIRT)
    time.sleep(2)

    mc.setBlocks(loc.x-1, loc.y+4, loc.z-1,
             loc.x+1, loc.y+5, loc.z+1,
             block.DIRT)
    time.sleep(2)

    mc.setBlock(loc.x, loc.y+6, loc.z, block.LAVA)

class Meteor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def fall(self):
        mc.setBlock(self.x,self.y,self.z,block.AIR)
        self.y -= 2
        mc.setBlock(self.x,self.y,self.z,block.OBSIDIAN)

    def checkImpact(self):
        #if block above!=AIR
        if mc.getBlock(self.x,self.y+1,self.z) != 0:
            return True
        else:
            return False

    def impact(self):
        #clear 3x3x3 space above meteor
        mc.setBlocks(self.x-1,self.y,self.z-1,
                     self.x+1,self.y+2,self.z+1,
                     block.AIR)
        
        #create some obsidian around impact area
        for i in range(random.randrange(6,10)):
            mc.setBlock(self.x+random.randrange(-2,2),
                        self.y+random.randrange(0,2),
                        self.z+random.randrange(-2,2),
                        [block.OBSIDIAN,block.OBSIDIAN,block.GLOWING_OBSIDIAN][random.randrange(0,3)])

def meteorShower():
    meteorList = []
    loc = mc.player.getPos()
    for _ in range(random.randrange(5,7)):
        #randomise the location of the meteor
        meteorList.append(Meteor(loc.x + random.randrange(-9,10), random.randrange(25,45), loc.z + random.randrange(-9,10)))
    #while there are still meteors
    while len(meteorList)>0:   
        for meteor in meteorList:
            meteor.fall()
            if meteor.checkImpact():
                meteor.impact()
                meteorList.remove(meteor)
        time.sleep(0.5)

def sinkhole():
    loc = mc.player.getPos()
    
    #if player is standing on solid ground
    if mc.getBlock(loc.x,loc.y-1,loc.z) not in [1,2,3,4,12,13,60,24]:
            return True
    #remove blocks below
    mc.setBlocks(loc.x-2,loc.y-4,loc.z-2,
                     loc.x+2,loc.y-16,loc.z+2,
                     block.AIR)
    mc.setBlocks(loc.x-4,loc.y-4,loc.z-2,
                     loc.x+4,loc.y-12,loc.z+2,
                     block.AIR)
    mc.setBlocks(loc.x-2,loc.y-4,loc.z-4,
                     loc.x+2,loc.y-12,loc.z+4,
                     block.AIR)
    mc.setBlocks(loc.x-4,loc.y-4,loc.z-6,
                     loc.x+4,loc.y-8,loc.z+6,
                     block.AIR)
    mc.setBlocks(loc.x-6,loc.y-4,loc.z-4,
                     loc.x+6,loc.y-8,loc.z+4,
                     block.AIR)
    #create gravel
    for i in range(-4,5):
        for j in range(-4,5):
            if mc.getBlock(loc.x+i,loc.y-2,loc.z+j)!=0:
                    mc.setBlock(loc.x+i,loc.y-2,loc.z+j,block.GRAVEL)
    for i in [5,6]:
        for j in range(-4,5):
            if mc.getBlock(loc.x+i,loc.y-2,loc.z+j)!=0:
                mc.setBlock(loc.x+i,loc.y-2,loc.z+j,block.GRAVEL)
    for i in [-5,-6]:
        for j in range(-4,5):
            if mc.getBlock(loc.x+i,loc.y-2,loc.z+j)!=0:
                mc.setBlock(loc.x+i,loc.y-2,loc.z+j,block.GRAVEL)
    for i in range(-4,5):
        for j in [5,6]:
            if mc.getBlock(loc.x+i,loc.y-2,loc.z+j)!=0:
                mc.setBlock(loc.x+i,loc.y-2,loc.z+j,block.GRAVEL)
    for i in range(-4,5):
        for j in [-5,-6]:
            if mc.getBlock(loc.x+i,loc.y-2,loc.z+j)!=0:
                mc.setBlock(loc.x+i,loc.y-2,loc.z+j,block.GRAVEL)
    
    #remove blocks on surface
    mc.setBlocks(loc.x-2,loc.y-1,loc.z-2,
                     loc.x+2,loc.y-1,loc.z+2,
                     block.AIR)
    time.sleep(0.5)
    mc.setBlocks(loc.x-4,loc.y-1,loc.z-2,
                     loc.x+4,loc.y-1,loc.z+2,
                     block.AIR)
    mc.setBlocks(loc.x-2,loc.y-1,loc.z-4,
                     loc.x+2,loc.y-1,loc.z+4,
                     block.AIR)
    mc.setBlocks(loc.x-2,loc.y-3,loc.z-2,
                     loc.x+2,loc.y-3,loc.z+2,
                     block.AIR)
    time.sleep(0.5)
    mc.setBlocks(loc.x-4,loc.y-1,loc.z-6,
                     loc.x+4,loc.y-1,loc.z+6,
                     block.AIR)
    mc.setBlocks(loc.x-6,loc.y-1,loc.z-4,
                     loc.x+6,loc.y-1,loc.z+4,
                     block.AIR)
    mc.setBlocks(loc.x-4,loc.y-3,loc.z-2,
                     loc.x+4,loc.y-3,loc.z+2,
                     block.AIR)
    mc.setBlocks(loc.x-2,loc.y-3,loc.z-4,
                     loc.x+2,loc.y-3,loc.z+4,
                     block.AIR)
    time.sleep(0.5)
    mc.setBlocks(loc.x-4,loc.y-3,loc.z-6,
                     loc.x+4,loc.y-3,loc.z+6,
                     block.AIR)
    mc.setBlocks(loc.x-6,loc.y-3,loc.z-4,
                     loc.x+6,loc.y-3,loc.z+4,
                     block.AIR)


def flood():
    loc = mc.player.getPos()
        
    for i in range(3):
        mc.setBlocks(loc.x-30,loc.y+i,loc.z-30,
                     loc.x-20,loc.y+i,loc.z+30,
                     block.WATER)
        mc.setBlocks(loc.x+30,loc.y+i,loc.z-30,
                     loc.x+20,loc.y+i,loc.z+30,
                     block.WATER)
        mc.setBlocks(loc.x-30,loc.y+i,loc.z-30,
                     loc.x+30,loc.y+i,loc.z-20,
                     block.WATER)
        mc.setBlocks(loc.x-30,loc.y+i,loc.z+30,
                     loc.x+30,loc.y+i,loc.z+20,
                     block.WATER)
        time.sleep(1)
        mc.setBlocks(loc.x-20,loc.y+i,loc.z-20,
                     loc.x-10,loc.y+i,loc.z+20,
                     block.WATER)
        mc.setBlocks(loc.x+20,loc.y+i,loc.z-20,
                     loc.x+10,loc.y+i,loc.z+20,
                     block.WATER)
        mc.setBlocks(loc.x-20,loc.y+i,loc.z-20,
                     loc.x+20,loc.y+i,loc.z-10,
                     block.WATER)
        mc.setBlocks(loc.x-20,loc.y+i,loc.z+20,
                     loc.x+20,loc.y+i,loc.z+10,
                     block.WATER)
        time.sleep(1)
        mc.setBlocks(loc.x-10,loc.y+i,loc.z-10,
                     loc.x,loc.y+i,loc.z+10,
                     block.WATER)
        mc.setBlocks(loc.x+10,loc.y+i,loc.z-10,
                     loc.x,loc.y+i,loc.z+10,
                     block.WATER)
        mc.setBlocks(loc.x-10,loc.y+i,loc.z-10,
                     loc.x+10,loc.y+i,loc.z,
                     block.WATER)
        mc.setBlocks(loc.x-10,loc.y+i,loc.z+10,
                     loc.x+10,loc.y+i,loc.z,
                     block.WATER)

def setBlock(i, x,y,z):
    if i==1: 
        mc.setBlock(x, y-1, z, block.REDSTONE_ORE)
    else:
        mc.setBlock(x, y-1, z, block.TNT)
    mc.setBlock(x, y-2, z, block.OBSIDIAN)
    

def tntRun():
    player = mc.player.getPos()
    total_blocks = random.randint(30, 50)

    #Initialize first block position
    pos_x = player.x
    pos_z = player.z
    pos_y = player.y + 30
    
    #Prime the first TNT block and support
    mc.setBlock(pos_x-1, pos_y, pos_z+1, block.TNT.id, 1)
    mc.setBlock(pos_x-1, pos_y-1, pos_z+1,block.REDSTONE_ORE)
    mc.setBlock(pos_x, pos_y-1, pos_z,block.REDSTONE_ORE)
    mc.player.setPos(pos_x, pos_y, pos_z)    

    path = random.randint(0,3)
    i = 0
    #Build run path
    for _ in range(total_blocks):
        ran = random.randint(-1,1)
        if path == 0:
            pos_x += 1
            if ran!=0:
                setBlock(i, pos_x,pos_y,pos_z)
                i = (i + 1) % 3
                pos_z += ran
        elif path == 1:
            pos_x -= 1
            if ran!=0:
                setBlock(i, pos_x,pos_y,pos_z)
                i = (i + 1) % 3
                pos_z += ran
        elif path == 2:
            pos_z += 1
            if ran!=0:
                setBlock(i, pos_x,pos_y,pos_z)
                i = (i + 1) % 3
                pos_x += ran
        else:
            pos_z -= 1
            if ran!=0:
                setBlock(i, pos_x,pos_y,pos_z)
                i = (i + 1) % 3
                pos_x += ran
            
        setBlock(i, pos_x,pos_y,pos_z)
        i = (i + 1) % 3
        
    #Build finish line
    mc.setBlocks(pos_x, pos_y-1, pos_z,
                 pos_x+3, pos_y-1, pos_z+3,
                 block.OBSIDIAN)

    mc.postToChat("Welcome to TNT Run!")
    time.sleep(1)
    mc.postToChat("Punch the TNT block to begin...")

def tntRoulette():
    player = mc.player.getPos()
    mc.setBlocks(player.x-2, player.y-1, player.z-2,
                 player.x+2, player.y-1, player.z+2,
                 block.OBSIDIAN)
    for i in range(3):
        for j in range(-2,3):
            mc.setBlock(player.x+j,player.y+i,player.z-2,block.TNT.id,[1,0,0][random.randrange(0,3)])
            mc.setBlock(player.x+j,player.y+i,player.z+2,block.TNT.id,[1,0,0][random.randrange(0,3)])
            mc.setBlock(player.x-2,player.y+i,player.z+j,block.TNT.id,[1,0,0][random.randrange(0,3)])
            mc.setBlock(player.x+2,player.y+i,player.z+j,block.TNT.id,[1,0,0][random.randrange(0,3)])
    mc.postToChat("Welcome to TNT Roulette!")
    time.sleep(1)
    mc.postToChat("Some of the TNT is primed and some is not.")
    mc.postToChat("Try to escape without blowing everything up!")

def tntCannon():
    player = mc.player.getPos()
    # Create Obsidian and glass shell
    mc.setBlocks(player.x-3, player.y-2, player.z+1,
                 player.x+6, player.y-1, player.z+1,
                 block.OBSIDIAN)
    mc.setBlocks(player.x-3, player.y-2, player.z+3,
                 player.x+6, player.y-1, player.z+3,
                 block.OBSIDIAN)
    mc.setBlocks(player.x-3, player.y-3, player.z+2,
                 player.x+6, player.y-3, player.z+2,
                 block.OBSIDIAN)
    mc.setBlocks(player.x-3, player.y-1, player.z+2,
                 player.x, player.y-1, player.z+2,
                 block.OBSIDIAN)
    mc.setBlocks(player.x+1, player.y+1, player.z+2,
                 player.x+5, player.y+1, player.z+2,
                 block.OBSIDIAN)
    mc.setBlocks(player.x+1, player.y, player.z+1,
                 player.x+5, player.y, player.z+1,
                 block.GLASS)
    mc.setBlocks(player.x+1, player.y, player.z+3,
                 player.x+5, player.y, player.z+3,
                 block.GLASS)
    mc.setBlocks(player.x-2, player.y-2, player.z+2,
                 player.x+5, player.y-2, player.z+2,
                 block.AIR)
    mc.setBlock(player.x-3, player.y-2, player.z+2, block.WATER)
    mc.setBlock(player.x-4, player.y-2, player.z+2, block.OBSIDIAN)
    mc.setBlock(player.x+7, player.y-2, player.z+2, block.OBSIDIAN)
    # Place TNT
    mc.setBlocks(player.x+1, player.y-1, player.z+2,
                 player.x+6, player.y-1, player.z+2,
                 block.TNT)
    # Prime first block
    mc.setBlock(player.x+1, player.y, player.z+2, block.TNT.id,1)
    mc.postToChat("This is the TNT Cannon.")
    time.sleep(1)
    mc.postToChat("Hit the exposed TNT to launch it!.")

def heatwave():
    player = mc.player.getPos()
    i = 30
    while i > 0:
        i-=1
        pos_x = player.x + random.randint(-4,4)
        pos_y = player.y + random.randint(-4,4)
        pos_z = player.z + random.randint(-4,4)
        checkBlock = mc.getBlock(pos_x, pos_y, pos_z)
        # if block is combustible
        if checkBlock in [5,6,8,9,17,18,30,31,35,37,38,39,40,47,53,54,58,64,65,81,83,85,107,53,59,96]:
            mc.setBlock(pos_x, pos_y, pos_z, block.AIR)
        # if block is smeltable
        elif checkBlock in [1,4,43,44,45,48,49,67,98]:
            mc.setBlock(pos_x, pos_y, pos_z, block.LAVA)
        # if block is meltable
        elif checkBlock in [78,79,80]:
            mc.setBlock(pos_x, pos_y, pos_z, block.WATER)
        # exception for clay
        elif checkBlock  == 82:
            mc.setBlock(pos_x, pos_y, pos_z, block.BRICK_BLOCK)
        # exception for grass
        elif checkBlock == 2:
            mc.setBlock(pos_x, pos_y, pos_z, block.DIRT)
        # exception for gravel and dirt
        elif checkBlock in [3,13,60]:
            mc.setBlock(pos_x, pos_y, pos_z, block.STONE)
        # exception for sand
        elif checkBlock == 12:
            mc.setBlock(pos_x, pos_y, pos_z, block.SANDSTONE)
        else:
            i+=1
def snowstorm():
    player = mc.player.getPos()
    for _ in range(random.randint(6,8)):
        for _ in range(random.randint(4,10)):
            pos_x = player.x + random.randint(-6,6)
            pos_z = player.z + random.randint(-6,6)
            pos_y = mc.getHeight(pos_x,pos_z)
            if mc.getBlock(pos_x,pos_y,pos_z)!=block.SNOW:
                mc.setBlock(pos_x,pos_y,pos_z,block.SNOW)
            else:
                mc.setBlock(pos_x,pos_y,pos_z,[block.SNOW_BLOCK,block.SNOW_BLOCK,block.ICE][random.randint(0,2)])
            time.sleep(0.5)

def emptySpaceFinder(x,y,z):
    for i in range(-1,1):
        for j in range(-1,1):
            if mc.getBlock(x+i,y-1,z+j) == 0:
                return [True, x+i,z+j]
    return [False]

def landslide():
    player = mc.player.getPos()
    for _ in range(random.randint(3,5)):
        for _ in range(random.randint(12,20)):
            pos_x = player.x + random.randint(-4,4)
            pos_z = player.z + random.randint(-4,4)
            pos_y = mc.getHeight(pos_x,pos_z) - 1
            checkBlock = mc.getBlock(pos_x,pos_y,pos_z) 
            if checkBlock in [1,2,3,4,12,13,24,48,49,60,82,98]:
                emptySpace = emptySpaceFinder(pos_x,pos_y,pos_z) 
                if emptySpace[0]:
                    mc.setBlock(pos_x,pos_y,pos_z,block.AIR)
                    mc.setBlock(emptySpace[1],mc.getHeight(emptySpace[1],emptySpace[2]),emptySpace[2],checkBlock)                
      
while True:
    choice = input("Make your choice")
    if choice == "1":    
        volcano()
    elif choice == "2":
        meteorShower()
    elif choice == "3":
        sinkhole()
    elif choice == "4":
        flood()
    elif choice == "5":
        heatwave()
    elif choice == "6":
        snowstorm()
    elif choice == "7":
        landslide()
    elif choice == "8":
        tntRun()
    elif choice == "9":
        tntRoulette()
    elif choice == "10":
        tntCannon()
    elif choice == "11":
        mc.saveCheckpoint()
    elif choice == "12":
        mc.restoreCheckpoint()
