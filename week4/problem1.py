


def s():
	# Solution script.
	o = 0 # How many integers satisfy the conditions
	for i in range(1,500+1):
		# Check divisibility
		if i % 3 == 0 or i % 7 == 0:
			o += 1
	return o

if __name__=="__main__":
	sol = s()
	print(sol)
	exit(0)
