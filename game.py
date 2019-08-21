import numpy as np

class Block:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Player:
    def __init__(self, name, num, pieces, points, win):
        self.name = name
        self.num = num
        self.pieces = pieces
        self.points = points
        self.win = win

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


    
if __name__ == "__main__":

    #Initializes list of all blocks in mahjong. Length of the list must be 144 pieces.
    blocks = createBlockList()

    #randomize the order of the blocks
    blocks = shuffleBlocks(blocks)

    #create players
    playerEast = Player("East", 0, [], 0, 0)
    playerSouth = Player("South", 1, [], 0, 0)
    playerWest = Player("West", 2, [], 0, 0)
    playerNorth = Player("North", 3, [], 0, 0)

    players = [playerEast, playerSouth, playerWest, playerNorth]

    #determine who gets first roll
    firstRollPlayer = None
    maxTotal = 0

    for player in players:
        roll1 = np.random.randint(1, 7)
        roll2 = np.random.randint(1, 7)
        total = roll1 + roll2
        if(total > maxTotal):
            maxTotal = total
            firstRollPlayer = player
        
    #first roll
    playerNum = firstRollPlayer.num
    roll1 = np.random.randint(1, 7)
    roll2 = np.random.randint(1, 7)
    total1 = roll1 + roll2
    
    #determine who rolls next
    playerNum = (playerNum + ((total % 4) - 1)) % 4 #write test cases later
    roll1 = np.random.randint(1, 7)
    roll2 = np.random.randint(1, 7)
    total2 = roll1 + roll2

    drawStartStack = (36 * (playerNum + 1)) / 3
    drawStartStack = drawStartStack - total2








    








    
    
