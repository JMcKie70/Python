def coin_tosses():
	head_count = 0
	tail_count = 0
	for count in range(1,5001):
		import random
		toss = random.randint(1,2)
		if toss == 1:
			head_count += 1
			print "Throwing a coin... It's a head! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"
		else:
			tail_count += 1
			print "Throwing a coin... It's a tail! ... Got " + str(head_count) + " head(s) so far and " + str(tail_count) + " tail(s) so far"

coin_tosses()