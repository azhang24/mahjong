import numpy as np
import block
from block import Block

class Player:
    def __init__(self, name, num, blocks, points, win):
        self.name = name
        self.num = num
        self.blocks = blocks
        self.points = points
        self.win = win

def firstRoll(players):
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

    return playerNum, total1

def secondRoll(playerNum, total1, players):
    #determine who rolls next
    playerNum = (playerNum + ((total1 % 4) - 1)) % 4 #write test cases later
    roll1 = np.random.randint(1, 7)
    roll2 = np.random.randint(1, 7)
    total2 = roll1 + roll2

    return playerNum, total2
    

def dealBlocks(startStack, players, blocks):

    #first round
    playerNum = 0
    for currStack in range(startStack, startStack-8, -2):
        stack1 = blocks[(currStack-1)*3:(currStack)*3]
        stack2 = blocks[(currStack-2)*3:(currStack-1)*3]

        playerStacks = [stack1, stack2]

        players[playerNum].blocks.append([block for stack in playerStacks for block in stack])

        playerNum += 1

    #secondRound
    playerNum = 0
    for currStack in range(startStack-8, startStack-16, -2):
        stack1 = blocks[(currStack-1)*3:(currStack)*3]
        stack2 = blocks[(currStack-2)*3:(currStack-1)*3]

        playerStacks = [stack1, stack2]

        players[playerNum].blocks.append([block for stack in playerStacks for block in stack])

        playerNum += 1

    currStack = startStack - 16
    #last round
    players[0].blocks.append([blocks[(currStack-1)*3], blocks[(currStack-2)*3]])
    players[1].blocks.append([blocks[(currStack-1)*3+1]])
    players[2].blocks.append([blocks[(currStack-1)*3+2]])
    players[3].blocks.append([blocks[(currStack-2)*3+1]])

    #flatten each players list of pieces
    for player in players:
        player.blocks = [block for blocklist in player.blocks for block in blocklist]
    
    startDraw = (currStack-2)*3+2
    
    return players, startDraw


if __name__ == "__main__":

    #Initializes list of all blocks in mahjong. Length of the list must be 144 pieces.
    blocks = block.createBlockList()

    #randomize the order of the blocks
    blocks = block.shuffleBlocks(blocks)

    #create players
    playerEast = Player("East", 0, [], 0, 0)
    playerSouth = Player("South", 1, [], 0, 0)
    playerWest = Player("West", 2, [], 0, 0)
    playerNorth = Player("North", 3, [], 0, 0)

    players = [playerEast, playerSouth, playerWest, playerNorth]

    playerNum, total1 = firstRoll(players)

    playerNum, total2 = secondRoll(playerNum, total1, players)

    drawStartStack = 12 * (playerNum + 1)
    drawStartStack = drawStartStack - total2 + 1

    players, startDraw = dealBlocks(drawStartStack, players, blocks)

    #test cases laters
    block.printBlocks(players[0].blocks)
    print(len(players[3].blocks))
    print(startDraw)

