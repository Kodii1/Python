import random
from Action import Action
from ActionEnum import ActionEnum
from .Animal import Animal
from Position import Position


class Antelope(Animal):

	def __init__(self, antelope=None, position=None, world=None):
		super(Antelope, self).__init__(antelope, position, world)

	def clone(self):
		return Antelope(self, None, None)
	

	def move(self):
		result = []
		pomPositions = self.getNeighboringPosition()
		newPosition = None

		if pomPositions:
			newPosition = random.choice(pomPositions)
			for aroundPosition in self.world.getNeighboringPositions(self.position): # moje
				metOrganism = self.world.getOrganismFromPosition(aroundPosition)
				afterPosition = Position(xPosition=self.position.x, yPosition=self.position.y)

				if metOrganism is not None and metOrganism.sign == 'R':
					diff_x = afterPosition.x - aroundPosition.x
					diff_y = afterPosition.y - aroundPosition.y
					if diff_x == 0 and diff_y < 0:
						afterPosition.y -= 2
					elif diff_x == 0 and diff_y > 0:
						afterPosition.y += 2
					elif diff_y == 0 and diff_x < 0:
						afterPosition.x -= 2
					elif diff_y == 0 and diff_x > 0:
						afterPosition.x += 2
					elif diff_x < 0 and diff_y < 0:
						afterPosition.x -= 2
						afterPosition.y -= 2
					elif diff_x < 0 and diff_y > 0:
						afterPosition.x -= 2
						afterPosition.y += 2
					elif diff_x > 0 and diff_y < 0:
						afterPosition.x += 2
						afterPosition.y -= 2
					elif diff_x > 0 and diff_y > 0:
						afterPosition.x += 2
						afterPosition.y += 2
					if self.world.positionOnBoard(afterPosition) and (self.world.getOrganismFromPosition(afterPosition)is None):
						result.append(Action(ActionEnum.A_MOVE, afterPosition, 0, self))
						self.lastPosition = afterPosition
						return result
					else:
						result.extend(self.consequences(metOrganism))
						self.lastPosition = self.position
						return result
			result.append(Action(ActionEnum.A_MOVE, newPosition, 0, self))
			metOrganism = self.world.getOrganismFromPosition(newPosition)
			if metOrganism is not None:
				result.extend(metOrganism.consequences(self))
		return result


	def action(self):
		result = []
		newAnimal = None
		birthPositions = self.getNeighboringBirthPosition()

		if self.ifReproduce() and birthPositions:
			newAnimalPosition = random.choice(birthPositions)
			newAnimal = self.clone()
			newAnimal.initParams()
			newAnimal.position = newAnimalPosition
			self.power = self.power / 2

			for aroundPosition in self.world.getNeighboringPositions(newAnimalPosition): # moje
				metOrganism = self.world.getOrganismFromPosition(aroundPosition)
				afterPosition = Position(xPosition=newAnimalPosition.x, yPosition=newAnimalPosition.y)

				if metOrganism is not None and metOrganism.sign == 'R':
					diff_x = afterPosition.x - aroundPosition.x
					diff_y = afterPosition.y - aroundPosition.y
					if diff_x == 0 and diff_y < 0:
						afterPosition.y -= 2
					elif diff_x == 0 and diff_y > 0:
						afterPosition.y += 2
					elif diff_y == 0 and diff_x < 0:
						afterPosition.x -= 2
					elif diff_y == 0 and diff_x > 0:
						afterPosition.x += 2
					elif diff_x < 0 and diff_y < 0:
						afterPosition.x -= 2
						afterPosition.y -= 2
					elif diff_x < 0 and diff_y > 0:
						afterPosition.x -= 2
						afterPosition.y += 2
					elif diff_x > 0 and diff_y < 0:
						afterPosition.x += 2
						afterPosition.y -= 2
					elif diff_x > 0 and diff_y > 0:
						afterPosition.x += 2
						afterPosition.y += 2
					if self.world.positionOnBoard(afterPosition) and (self.world.getOrganismFromPosition(afterPosition)is None):
						result.append(Action(ActionEnum.A_ADD, afterPosition, 0, newAnimal))
						return result
					else:
						result.extend(self.consequences(metOrganism))
						return result
			result.append(Action(ActionEnum.A_ADD, afterPosition, 0, newAnimal))


		return result

	

	def initParams(self):
		self.power = 4
		self.initiative = 3
		self.liveLength = 11
		self.powerToReproduce = 5
		self.sign = 'A'

	def getNeighboringPosition(self):
		return self.world.filterPositionsWithoutAnimals(self.world.getNeighboringPositions(self.position))


