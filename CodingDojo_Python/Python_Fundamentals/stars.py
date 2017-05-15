# Create a function called draw_stars() that takes a list of numbers and prints out *.
def draw_stars(list):
	for element in list:
		if element > 0:
			print element * "*"

draw_stars([0, 4, 10, -1, 5, -2])

# When a string is passed, instead of displaying *, 
# display the first letter of the string according to the example below. 
# You may use the .lower() string method for this part.

def draw_stars2(list):
	for element in list:
		if type(element) is int and element > 0:
			print element * "*"
		elif type(element) is str:
			print element[0].lower() * len(element)

draw_stars2([1,-1,2, "happy", "Mad"])