

def fib(n):
	if n <= 2:
		return 1
	a, b ,c = 1, 1, 0
	for i in range(n-2):
		c = a # Intermediate
		a = a + b
		b = c
	return a



if __name__=="__main__":
	print(fib(10))
	print(fib(20))
	print(fib(30))
	exit()
