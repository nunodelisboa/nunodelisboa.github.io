#!/usr/bin/python

import random
import Toll
import Car
import Truck


listOfVehicles = []
for i in range(1000):
	if random.randint(1,10) <= 8:
		listOfVehicles.append(Car.Car())
	else:
		listOfVehicles.append(Truck.Truck())

t = Toll.Toll()

for v in listOfVehicles:
	t.collect(v)

print t	
		


