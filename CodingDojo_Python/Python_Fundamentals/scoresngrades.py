def scoresngrades():
	for count in range (1,11):
		import random
		score = random.randint(60,100)
		grade = ""
		if score > 89:
			grade = "A"
		elif score > 79:
			grade = "B"
		elif score > 69:
			grade = "C"
		else:
			grade = "D"
		print "Score: " + str(score) + "; Your grade is " + grade
scoresngrades()