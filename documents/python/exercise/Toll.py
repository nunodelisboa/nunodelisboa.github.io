class Toll:

	def __init__(self):
		self.__charged = 0
		self.__vehicles = 0
		self.__log = []

	def collect(self, vehicle):
		self.__charged += vehicle.tariff()
		self.__vehicles += 1
		self.__log.append(vehicle.id())

	def __str__(self):
		return """
		 	TOTAL CHARGED: %d
			TOTAL VEHICLES: %d
			COMPLETE LOG:
			%s
		""" % (self.__charged, self.__vehicles, '\t'.join(map(str,self.__log)))
