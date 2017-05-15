class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.display_all()
		
	def display_all(self):
		if self.price > 10000:
			tax = .15
		else:
			tax = .12
		print "Price: " + str(self.price)
		print "Speed: " + self.speed
		print "Fuel: " + self.fuel
		print "Mileage: " + str(self.mileage) + "mpg"
		print "Tax: " + str(tax)

car1 = Car(2000, "35mph", "Full", 15)


car2 = Car(2000, "5mph", "Not Full", 105)


car3 = Car(2000, "15mph", "Kind of Full", 95)


car4 = Car(2000, "25mph", "Full", 25)


car5 = Car(2000, "25mph", "Half Full", 5)


car6 = Car(1000, "10mph", "Full", 90)


