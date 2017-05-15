
class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print self.price, self.max_speed, self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		return self
	def reverse(self):
		print "Reversing"
		self.miles -= 5
		if self.miles < 0:
			self.miles = 0
		return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(150, "35mph")
bike1.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(250, "45mph")
bike3.reverse().reverse().reverse().displayInfo()

