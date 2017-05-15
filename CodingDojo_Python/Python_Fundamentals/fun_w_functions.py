#create a function that identifies odd and even numbers from 1 to 2000
def odd_even():
	for count in range(1,2000):
		if count % 2 != 0:
			print "Number is " + str(count) + ". This is an odd number."
		else:
			print "Number is " + str(count) + ". This is an even number."

odd_even()

#create a function that returns a list multiplied by 5
def multiply(list, num):
	output = []
	for element in list:
		output.append(element * num)
	return output

a = [2,4,10,16]
x = 5

b = multiply(a, x)
print b

'''write a function that takes the multiply function call as an argument and returns
 the multiplied list as a two-dimensional list.  Each list should contain
 as many ones as the number in the original list'''
def layered_multiples(multiply(list,num)):
	mult_list = multiply(list, num)
	new_list = []
	num_sub_lists = len(mult_list)
	for count in range(1, num_sub_lists):
		new_list.append([])
	for element in mult_list:
		for count in range(1, mult_list[element])
			new_list[[]].append(1)
		
	return new_list

x = layered_multiples(multiply([2,4,5],3))
print x
