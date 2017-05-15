
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price, self.max_speed, self.miles

	def ride(self):
		print "Riding"
		self.miles += 10

	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0


bike1 = Bike(200, "25mph")
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2 = Bike(150, "35mph")
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(250, "45mph")
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()

