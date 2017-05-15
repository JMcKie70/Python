# print all the odd numbers from 1 to 1000
for count in range (1, 1001):
	if count % 2 != 0:
		print count

# print all the multiples of 5 from 5 to 1,000,000.
for count in range (5, 1000000):
	if count % 5 == 0:
		print count

# print the sum of all the values in the list
a = [1,2,5,10,255,3]
sum = 0
for element in a:
	sum += element
print sum

# print the average of the values in the list
a = [1, 2, 5, 10, 255, 3]
sum = 0
num = len(a)
for element in a:
	sum += element
avg = sum/num
print avg