import numpy as np

class Block:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

def createBlockList():
    blocks = []
    for _ in range(4):
        for i in range(1, 10):
            numberBlock = Block("Number", i)
            blocks.append(numberBlock)

    for _ in range(4):
        for i in range(1, 10):
            wheelBlock = Block("Wheel", i)
            blocks.append(wheelBlock)
    
    for _ in range(4):
        for i in range(1, 10):
            stickBlock = Block("Stick", i)
            blocks.append(stickBlock)
    
    winds = ["East", "South", "West", "North"]

    for wind in winds:
        for i in range(4):
            windBlock = Block("Wind", wind)
            blocks.append(windBlock)
    
    dragons = ["red", "green", "white"]

    for dragon in dragons:
        for i in range(4):
            dragonBlock = Block("Dragon", dragon)
            blocks.append(dragonBlock)
    
    for i in range(4):
        flowerBlock = Block("Flower", i)
        blocks.append(flowerBlock)
    
    for i in range(4):
        seasonBlock = Block("Season", i)
        blocks.append(seasonBlock)
    
    return blocks

def shuffleBlocks(blocks):
    indices = np.arange(len(blocks))
    np.random.shuffle(indices)
    shuffledBlocks = np.array(blocks)[indices]
    return shuffledBlocks

def printBlocks(blocks):
    for block in blocks:
        print("( " + block.suit + " , " + str(block.value) + " )")


    