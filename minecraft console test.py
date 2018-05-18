import random, time
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()

phrases = ["Are you oak-ay?",
               "Someone to talk to, I'm so rweleafed!",
               "Please don't leaf me",
               "Wood you talk to me a while?",
               "Be leaf in yourself!",
               "You're under arrest for treeson!",
               "I don't know what to say, I'm stumped.",
               "What kind of tree fits in your hand? A palm tree!"]

snowing = -1
tree = -1

def toggleSnow(channel):
    snowing *= -1

def toggleTree(channel):
    tree *= -1

while True:
    player = mc.player.getPos()
    blocks = mc.getBlocks(player.x, player.y, player.z, player.x, player.y, player.z+1)
    print(blocks)
    # snow day code
    if snowing == 1:
        mc.setBlock(player.x, player.y, player.z, block.SNOW)

    # tree code
    if tree == 1:
        if 17 in blocks:
            mc.postToChat(phrases[random.randrange(0,len(phrases))])

    # diamond code
    print(blocks.count(56))
    
    #wait 2s 
    time.sleep(2)

