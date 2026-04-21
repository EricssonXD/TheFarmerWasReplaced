from helpers import timer

# 11
def myfunc():
	# Your code here
	# item = {"x":5, "y":10}
	a = 1
	b = 2
	c = 3
	for i in range(2):
		if i == 1:
			a = 3
			b = 4
			c = 6
		quick_print(a+b+c)


def myfunc2():
	# Your code here
	item = [1, 2, 3]
	for i in range(2):
		if i == 1:
			item = [4, 5, 6]
		quick_print(item[0]+item[1]+item[2])
timer(myfunc2)