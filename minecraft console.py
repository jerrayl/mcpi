import random, time
import mcpi.minecraft as minecraft
import mcpi.block as block
import RPi.GPIO as GPIO
mc = minecraft.Minecraft.create()

D2 = 17
D3 = 18
D4 = 27
D5 = 22
D6 = 23
D7 = 24
D8 = 25
D9 = 4
D10 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(D7,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(D6,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(D5,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(D4,GPIO.IN,pull_up_down=GPIO.PUD_UP)

snowing = -1

def toggleSnow(channel):
    snowing *= -1

def letThereBeLight(channel):
    print("light")
    player = mc.player.getPos()
    
    for x in range(-3,4):
        for y in range(0,3):
            for z in range(-3,4):
                mc.setBlock(player.x+x, player.y+y, player.z+z, 50)

def lavaChallenge(channel):
    print("lava")
    mc.postToChat("Welcome to Lava Challenge! Can you survive?")
    time.sleep(1)
    mc.postToChat("Game starting in 3...")
    time.sleep(1)
    mc.postToChat("2...")
    time.sleep(1)
    mc.postToChat("1...")
    time.sleep(1)

    #get starting position
    sp = mc.player.getPos()

    #clear space above
    mc.setBlocks(sp.x+5, sp.y, sp.z+5,
                 sp.x-5, sp.y+5, sp.z-5,    
                 block.AIR)

    #Create lava container
    mc.setBlocks(sp.x+5, sp.y-2, sp.z+5,
                 sp.x-5, sp.y-1, sp.z-5,    
                 block.LAPIS_LAZULI_BLOCK)
    #create lava
    mc.setBlocks(sp.x+4, sp.y-1, sp.z+4,
                 sp.x-4, sp.y-1, sp.z-4,
                 block.LAVA)
    #create middle block
    mc.setBlock(sp.x, sp.y-1, sp.z,
                block.DIAMOND_BLOCK)

    #add cacti above lava to increase difficulty
    for x in [-4,-2,2,4]:
        for z in [-4,-2,0,2,4]:
            mc.setBlock(sp.x+x, sp.y+1, sp.z+z, block.CACTUS)

    #enter game loop
    while True:
        #get player's current position
        player = mc.player.getPos()

        if sp.y != player.y:
            #game over
            mc.postToChat("GAME OVER!")
            break

        #change block underneath player to obsidian as a warning
        mc.setBlock(player.x, player.y-1, player.z, block.OBSIDIAN)

        #Wait 1 second
        time.sleep(1)

        #change block in random direction to Diamond
        direction = random.randrange(1,5)
        if direction == 1:  #North
            mc.setBlock(player.x, player.y-1, player.z-1, block.DIAMOND_BLOCK)
        elif direction == 2:  #East
            mc.setBlock(player.x+1, player.y-1, player.z, block.DIAMOND_BLOCK)
        elif direction == 3:  #South
            mc.setBlock(player.x, player.y-1, player.z+1, block.DIAMOND_BLOCK)
        else:  #West
            mc.setBlock(player.x-1, player.y-1, player.z, block.DIAMOND_BLOCK)

        #Wait 1.5 seconds
        time.sleep(1.5)
        
        #change block underneath original position to air
        mc.setBlock(player.x, player.y-1, player.z, block.AIR)

        #Wait 1 second
        time.sleep(1)


def talkingTree(channel):
    print("tree")
    player = mc.player.getPos()
    phrases = ["Are you oak-ay?",
               "Someone to talk to, I'm so rweleafed!",
               "Please don't leaf me",
               "Wood you talk to me a while?",
               "Be leaf in yourself!",
               "You're under arrest for treeson!",
               "I don't know what to say, I'm stumped.",
               "What kind of tree fits in your hand? A palm tree!"]

    #advanced test to see if tree is in range:
    #tests to see if player is within 4 blocks of a tree
    for x in range(-3,4):
        for z in range(-3,4):
            blocktype = mc.getBlock(player.x+x, player.y, player.z+z)
            if blocktype == 17:
                rng = random.randrange(0,len(phrases))
                phrase = phrases[rng]
                mc.postToChat(phrase)

    #wait 0.5 seconds to prevent chat spam
    time.sleep(0.5)

GPIO.add_event_detect(D7, GPIO.FALLING, callback=letThereBeLight, bouncetime=500)
GPIO.add_event_detect(D6, GPIO.FALLING, callback=talkingTree, bouncetime=500)
GPIO.add_event_detect(D5, GPIO.FALLING, callback=lavaChallenge, bouncetime=500)
GPIO.add_event_detect(D4, GPIO.FALLING, callback=toggleSnow, bouncetime=500)


while True:
    if snowing == 1:
        mc.setBlock(player.x, player.y, player.z, block.SNOW)

