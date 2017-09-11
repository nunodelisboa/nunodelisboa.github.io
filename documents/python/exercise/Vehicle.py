class Vehicle:
	__population = 0

	def __init__(self):
		Vehicle.__population += 1
		self.__identification = Vehicle.__population

	def tariff(self): pass

	def id(self):
		return self.__identification
