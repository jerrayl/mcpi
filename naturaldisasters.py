import random, time
import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()  

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

import matrixkeypad

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

jokeList = ["Q: Hear about the creeper that went to a party?","A: He had a BLAST!","Q: Which musical instrument do skeletons play?","A: Trom-Bone","Q: Why didn’t the skeleton go to the prom?","A: He had no body to dance with?","Q: What kind of music do Minecraft players listen to?","A: Bed-rock and roll.","Q: What do Australian Creepers use to hunt?","A: BOOM-a-rangs","Q: What do they teach in witch school?","A: Spelling.","Q: What did Steve say when he was angry at a skeleton?","A: I’ve got a bone to pick with you!","Q: What do skeletons order at the village restaurant?","A: Spare ribs","Q: What kind of makeup do witches wear?","A: Mas-scare-a","Q: What did the zombie say to the villager?","A: Nice to eat you.","Q: What is a Creepers favorite food?","A: Ssssssssalad","Q: Do you hear about the Minecraft movie?","A: It’s a blockbuster.","Q: What is a witch with poison ivy called?","A: An itchy witchy.","Q: Which band always plays at the Minecraft New Year’s party?","A: The Village People","Q: Why can’t the Ender Dragon ever understand a book?","A: Because he always starts at the end.","Q: How are ocelots like m&m’s.","A: You can’t just have one.","Q: What do witches put in their hair?","A: Scare spray","Q: Why didn’t the enderman cross the road?","A: Because he teleported.","Q: How do zombies get so good at Minecraft?","A: DEADication.","Q: Where does Steve rent movies?","A: Blockbuster","Q: What kind of parties do Minecraft players have?","A: Block parties.","Q: What did Charlie Brown say when Steve broke his baseball bat?","A: You Blockhead!","Q: Why did the mushroom make such a good roommate?","A: It’s a real fungi.","Q: What is Cobblestone’s favorite type of music?","A: Rock music.","Q: What did the chicken say to the cow?","A: Nice to meat you.","Q: What tops off a Creeper’s ice cream sundae?","A: Whipped scream.","Q: How does Steve measure his shoe size?","A: In Square Feet.","Q: Why did the Creeper cross the road?","A: To get to the other Sssssssssside","Q: What did the chicken say to the sheep?","A: Nice to meet ewe.","Q: Which rock band do skeletons like most?","A: The Grateful Dead","Q: How did Steve make the skeleton laugh?","A: He tickled it’s funny bone.","Q: Which country do ghasts like the most?","A: The Nether-Lands!","Q: What city do most wolves live?","A: Howllywood, California","Q: Where do miners sleep?","A: On their bed-rocks","Q: What do you call a skeleton that sits around all day?","A: A lazy bone.","Q: What did the chicken say to the ocean?","A: Nothing, it just waved.","Q: Why did the sailor bring gold, silver and iron into his boat?","A: He needed ores (oars).","Q: What was the name of the Minecraft boy band?","A: New Kids on the Block.","Q: Why can’t you score against Minecraft basketball players?","A: They know how to block.","Q: What is the official sport of Minecraft?","A: Boxing.","Q: Why did the creeper cross the road?","A: Because there was an ocelot chasing him.","Q: Why aren’t there cars in Minecraft?","A: The streets are blocked off.","Q: Why didn’t the skeleton like to fly?","A: He had no guts","Q: Why couldn’t the minecraft player join the army?","A: He was a miner.","Q: What did Steve say to his girlfriend?","A: I dig you.","Q: How do villagers stay fit?","A: They jog around the block.","Q: What did the sheep say after trying to eat a cactus?","A: Accidents Wool happen.","Q: What’s the difference between a crazy rabbit and a counterfeit dollar bill?","A: One is bad money, the other is a mad bunny","Q: Where do you shear a sheep?","A: At the baa-baa shop.","Q: Who won the skeleton beauty contest?","A: No body.","Q: What time is it when ten ocelots chase Steve?","A: Ten after One.","Q: Why didn’t the skeleton cross the road?","A: He didn’t have the guts.","Q: How does Steve avoid getting sunburn?","A: SunBLOCK.","Q: What did the skeleton say to the hungry wolf?","A: Bone Appetit","Q: What did the minecraft turkey say?","A: Cobble, cobble, cobble!","Q: How do you make things change direction in Minecraft?","A: You block their way.","Q: How does Steve get exercise?","A: By running around the block.","Q: What is a creeper’s favorite subject?","A: HissssSSSSStory","Q: What do minecraft friends do for fun on the weekend?","A: Go to square dances.","Q: Why could’t the miner get to his diamonds?","A: Something blocked his way","Q: What do skeletons say before they begin dining?","A: Bone appetit."]

    
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

def overgrowth():
    player = mc.player.getPos()
    for _ in range(15):
        x_pos = player.x+random.randint(-6,6)
        z_pos = player.z+random.randint(-6,6)
        mc.setBlock(x_pos,mc.getHeight(x_pos,z_pos),z_pos,[6,31,37,38,39,40,81,103][random.randint(0,7)])

    for _ in range(random.randint(6,12)):
        ran_x = random.randint(-8,8)
        ran_z = random.randint(-8,8)
        mc.setBlocks(player.x+ran_x-1, player.y+2, player.z+ran_z-1,
                 player.x+ran_x+1, player.y+4, player.z+ran_z+1,
                 block.LEAVES)
        mc.setBlocks(player.x+ran_x, player.y, player.z+ran_z,
                 player.x+ran_x, player.y+4, player.z+ran_z,
                 block.WOOD)

def cyclone():
    for _ in range(random.randint(3,5)):
        player = mc.player.getPos()
        mc.player.setTilePos(player.x+random.randint(-20,20),player.y+random.randint(10,15),player.z+random.randint(-20,20))
        time.sleep(0.3)

def tntLauncher():
    player = mc.player.getPos()
    mc.setBlock(player.x+1,player.y,player.z,block.TNT.id,1)
    mc.setBlock(player.x+1,player.y-1,player.z,block.WATER)
    mc.postToChat("Stand on the TNT and detonate it for blastoff")
        

def joke():
    ran = random.randint(0,60)
    mc.postToChat(jokeList[ran*2])
    time.sleep(0.5)
    mc.postToChat(jokeList[ran*2+1])

while True:
    choice = matrixkeypad.checkKeypress()
    if choice == 1:
        mc.postToChat("Volcano")
        volcano()
    elif choice == 2:
        mc.postToChat("Meteor Shower")
        meteorShower() 
    elif choice == 3:
        mc.postToChat("Sinkhole")
        sinkhole()
    elif choice == 4:
        mc.postToChat("Flood")
        flood()
    elif choice == 5:
        mc.postToChat("Heatwave")
        heatwave() 
    elif choice == 6:
        mc.postToChat("Snowstorm")
        snowstorm()
    elif choice == 7:
        mc.postToChat("Landslide")
        landslide()
    elif choice == 8:
        mc.postToChat("Overgrowth")
        overgrowth()
    elif choice == 9:
        mc.postToChat("Cyclone")
        cyclone()
    elif choice == "A":
        tntRun()
    elif choice == "B":
        tntRoulette()
    elif choice == "C":
        tntCannon()
    elif choice == "D":
        tntLauncher()
    elif choice == 0:
        joke()
    elif choice == "*":
        mc.postToChat("Saved")
        mc.saveCheckpoint()
    elif choice == "#":
        mc.restoreCheckpoint()
        mc.postToChat("Loaded")
    time.sleep(1)
