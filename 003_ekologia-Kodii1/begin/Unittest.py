import unittest

from World import World
from Position import Position
from Organisms.Antelope import Antelope
from Organisms.Lynx import Lynx
import os



class TestExercise4(unittest.TestCase):
    def test_first(self):
        pyWorld = World(10, 10)
        lynx = Lynx(position=Position(xPosition=1, yPosition=1), world=pyWorld)
        expected = 'Lynx: power: 6 initiative: 5 liveLength 18 position: (1, 1)'

        self.assertEqual(str(lynx), expected)

    def test_secound(self):
        pyWorld = World(10, 10)
        antelope = Antelope(position=Position(xPosition=1, yPosition=1), world=pyWorld)
        expected = 'Antelope: power: 4 initiative: 3 liveLength 11 position: (1, 1)'

        self.assertEqual(str(antelope), expected)

    def test_third(self):
        pyWorld = World(10, 10)
        antelope = Antelope(position=Position(xPosition=1, yPosition=1), world=pyWorld)
        pyWorld.addOrganism(antelope)
        lynx = Lynx(position=Position(xPosition=0, yPosition=0), world=pyWorld)
        pyWorld.addOrganism(lynx)
        pyWorld.makeTurn()
        result = antelope.position
        expected = Position(xPosition=3, yPosition=1)
        expectedv2 = Position(xPosition=1, yPosition=3)
        self.assertTrue(result.x == expected.x or result.x == expectedv2.x)
        self.assertTrue(result.y == expected.y or result.y == expectedv2.y)




    def test_fourth(self):
        pyWorld = World(10, 10)
        antelope = Antelope(position=Position(xPosition=0, yPosition=0), world=pyWorld)
        pyWorld.addOrganism(antelope)
        lynx = Lynx(position=Position(xPosition=1, yPosition=1), world=pyWorld)
        pyWorld.addOrganism(lynx)
        pyWorld.makeTurn()

        for x in range (0,10):
            for y in  range(0,10):
                if pyWorld.filterFreePositionsv2(Position(xPosition=x, yPosition=y)) != 'A':
                    result = True
                    
        expected = True
        self.assertEqual(result, expected)

    def test_fifth(self):
        pyWorld = World(10, 10)
        pyWorld.makeTurn()
        pyWorld.makeTurn()
        user_Y = 2
        user_X = 3
        newOrg = Antelope(position=Position(xPosition=user_X, yPosition=user_Y), world=pyWorld)
        pyWorld.addOrganism(newOrg)
        result = newOrg.position
        expected = Position(xPosition=3, yPosition=2)
        self.assertEqual(result.y, expected.y)
        
if __name__ == "__main__":
    unittest.main()