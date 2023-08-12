from World import World
from Position import Position
from Organisms.Grass import Grass
from Organisms.Sheep import Sheep
from Organisms.Antelope import Antelope
from Organisms.Lynx import Lynx
import os



if __name__ == '__main__':
	pyWorld = World(10, 10)

	newOrg = Grass(position=Position(xPosition=9, yPosition=9), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Grass(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Sheep(position=Position(xPosition=4, yPosition=2), world=pyWorld)
	pyWorld.addOrganism(newOrg)
	
	#dopisane przezmnie :D 
	newOrg = Lynx(position=Position(xPosition=0, yPosition=0), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	newOrg = Antelope(position=Position(xPosition=1, yPosition=1), world=pyWorld)
	pyWorld.addOrganism(newOrg)

	print(pyWorld)

	for _ in range(0, 50):
		user_input = input("Wpisz polecenie: ")
		if user_input in ['Antylopa', 'Trawa', 'Rys', 'Owca']:
			print("Pole musi być wolne")
			user_X = int(input("Wpisz miejsce x: "))
			user_Y = int(input("Wpisz miejsce y: "))
			if pyWorld.positionOnBoard(Position(xPosition=user_X, yPosition=user_Y)) and pyWorld.filterFreePositionsv2(Position(xPosition=user_X, yPosition=user_Y)):
				if user_input == "Antylopa":
					newOrg = Antelope(position=Position(xPosition=user_X, yPosition=user_Y), world=pyWorld)
					pyWorld.addOrganism(newOrg)
				elif user_input == "Trawa":
					newOrg = Grass(position=Position(xPosition=user_X, yPosition=user_Y), world=pyWorld)
					pyWorld.addOrganism(newOrg)
				elif user_input == "Owca":
					newOrg = Sheep(position=Position(xPosition=user_X, yPosition=user_Y), world=pyWorld)
					pyWorld.addOrganism(newOrg)
				elif user_input == "Rys":
					newOrg = Lynx(position=Position(xPosition=user_X, yPosition=user_Y), world=pyWorld)
					pyWorld.addOrganism(newOrg)
			print(pyWorld)
		if user_input == "Plaga":
			pass
		input('')
		os.system('cls')
		pyWorld.makeTurn()
		print(pyWorld)

					
