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
    

def dealBlocks(startStack, startPlayer, players, blocks):

    #first round
    playerNum = startPlayer
    for currStack in range(startStack, startStack-8, -2):
        stack1 = blocks[(currStack-1)*3:(currStack)*3]
        stack2 = blocks[(currStack-2)*3:(currStack-1)*3]

        playerStacks = [stack1, stack2]

        players[playerNum].blocks.append([block for stack in playerStacks for block in stack])

        playerNum += 1

        if(playerNum >= 4):
            playerNum %= 4
    

    #secondRound
    playerNum = startPlayer
    for currStack in range(startStack-8, startStack-16, -2):
        stack1 = blocks[(currStack-1)*3:(currStack)*3]
        stack2 = blocks[(currStack-2)*3:(currStack-1)*3]

        playerStacks = [stack1, stack2]

        players[playerNum].blocks.append([block for stack in playerStacks for block in stack])

        playerNum += 1

        if(playerNum >= 4):
            playerNum %= 4

    currStack = startStack - 16
    #last round
    players[startPlayer].blocks.append([blocks[(currStack-1)*3], blocks[(currStack-2)*3]])
    players[(startPlayer + 1) % 4].blocks.append([blocks[(currStack-1)*3+1]])
    players[(startPlayer + 2) % 4].blocks.append([blocks[(currStack-1)*3+2]])
    players[(startPlayer + 3) % 4].blocks.append([blocks[(currStack-2)*3+1]])

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

    playerNum1, total1 = firstRoll(players)

    playerNum2, total2 = secondRoll(playerNum1, total1, players)

    drawStartStack = 12 * (playerNum2 + 1)
    drawStartStack = drawStartStack - total1 - total2 + 1



    players, startDraw = dealBlocks(drawStartStack, playerNum1, players, blocks)

    #test cases laters
    print(playerNum1)
    print(total1)
    print(playerNum2)
    print(total2)
    print(drawStartStack)

    block.printBlocks(blocks)
    print("Player 0: ")
    block.printBlocks(players[0].blocks)

    print("Player 1: ")
    block.printBlocks(players[1].blocks)
    
    print("Player 2: ")
    block.printBlocks(players[2].blocks)

    print("Player 3: ")
    block.printBlocks(players[3].blocks)
