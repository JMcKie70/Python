str = "If monkeys like bananas, then I must be a monkey"

monkey_index = str.find("monkey")
print monkey_index

print str.replace("monkey","alligator")

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x.pop(0)
print x.pop()

x = ["hello",2,54,-2,7,12,98,"world"]
x_new = []
x_new.append(x.pop(0))
x_new.append(x.pop())
print x_new

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x_1 = x.sort()
print x_1

new_list = []
for element in x_1:
	if element < 0:
		new_list.append(element)
		x_1.pop(element)
x_1.insert(0, new_list)

