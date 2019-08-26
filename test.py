import unittest
import game
import block
import numpy as np
from block import Block
from game import Player

class TestInitList(unittest.TestCase):

    blocks = block.createBlockList()

    def test_init_list(self):
        self.assertEqual(len(self.blocks), 144, "List should have 144 blocks.")
        
    def test_randomize_list_len(self):
        self.assertEqual(len(block.shuffleBlocks(self.blocks)), 144, "List should still have 144 blocks after shuffling.")


class TestDiceRoll(unittest.TestCase):

    players = [Player("", 0, [], 0, False), Player("", 1, [], 0, False), 
                    Player("", 2, [], 0, False), Player("", 3, [], 0, False)]

    def test_dice_roll_two(self):
        playerNum2, secondTotal = game.secondRoll(0, 2, self.players)
        self.assertEqual(playerNum2, 1)

    def test_dice_roll_three(self): 
        playerNum2, secondTotal = game.secondRoll(0, 3, self.players)
        self.assertEqual(playerNum2, 2)
    
    def test_dice_roll_four(self):
        playerNum2, secondTotal = game.secondRoll(0, 4, self.players)
        self.assertEqual(playerNum2, 3)

    def test_dice_roll_five(self):
        playerNum2, secondTotal = game.secondRoll(0, 5, self.players)
        self.assertEqual(playerNum2, 0)

    def test_dice_roll_six(self):
        playerNum2, secondTotal = game.secondRoll(0, 6, self.players)
        self.assertEqual(playerNum2, 1)
    
    def test_dice_roll_seven(self):
        playerNum2, secondTotal = game.secondRoll(0, 7, self.players)
        self.assertEqual(playerNum2, 2)
    
    def test_dice_roll_eight(self):
        playerNum2, secondTotal = game.secondRoll(0, 8, self.players)
        self.assertEqual(playerNum2, 3)

    def test_dice_roll_random_one(self):
        playerNum2, secondTotal = game.secondRoll(3, 10, self.players)
        self.assertEqual(playerNum2, 0)
    
    def test_dice_roll_random_two(self):
        playerNum2, secondTotal = game.secondRoll(1, 7, self.players)
        self.assertEqual(playerNum2, 3)





    

if __name__ == "__main__":
    unittest.main()