
import copy

def gen_bin_strings(n, length):
	out = []
	if n == 0:
		return out
	for i in range(2**n):
		listappend = [int(x) for x in list(bin(i)[2:])]
		listappend = [0]*(length-len(listappend)) + listappend
		assert len(listappend) == length
		out.append(listappend)
	return out

def count_one_bits(number, length): # Returns the number of on bits in this number.
	# This is because I implemented the numbers as an array of the integers 1 or 0. This is usually bad, but in this case it makes my job easier.
	return sum(1 for i in number if i == 1)

def count_zero_bits(number, length):
	return length - count_one_bits(number, length)

def check_part_a(numbers):
	# How many bit strings contain exactly four 0s and one 1?
	# Only get numbers which are 5 bits long.
	numbers = [x for x in numbers if len(x) == 5]
	n = 0 # How many integers satisfy the constraint?
	for i in numbers:
		# print(i)
		if count_one_bits(i, 5) == 1 and count_zero_bits(i, 5) == 4:
			n += 1
	# Should be five, because obvious reasons.
	# print("n: "+str(n))
	assert n == 5
	return n

def check_ones(number):
	if number[0] == 1: # This check here ensures that the first bit must be zero, because otherwise we basically have a one which is not followed up by a zero.
		return False
	should_be_zero = False
	for i in number:
		if should_be_zero:
			if i != 0:
				return False
		if i == 1:
			should_be_zero = True
		else:
			should_be_zero = False
	return True

def check_part_b(numbers):
	# How many bit strings contain exactly four 0s and one 1?
	# Only get numbers which are 12 bits long.
	numbers = [x for x in numbers if len(x) == 7+5]
	n = 0 # How many integers satisfy the constraint?
	for i in numbers:
		if count_one_bits(i, 7+5) == 5: # Check for zero bits is redundant
			if check_ones(i):
				n += 1
	return n

def part_b():
	# How many bit strings contain exactly seven 0s and five 1s if every 1 must be immediately followed by a 0?
	all_ints = gen_bin_strings(5+7,5+7)
	sol = check_part_b(all_ints)
	print("Solution to part b: "+str(sol))
	return


def check_part_c(numbers):
	# How many bit strings contain exactly four 0s and one 1?
	# Only get numbers which are 12 bits long.
	numbers = [x for x in numbers if len(x) == 7+5]
	n = 0 # How many integers satisfy the constraint?
	for i in numbers:
		if i[-1] != 1: # Very first bit is not one. (Here the "first bit" is actually the last bit.)
			continue
		if count_one_bits(i, 7+5) == 5: # Check for zero bits is redundant
			if check_ones(i):
				n += 1
	return n

def part_c():
	# How many bit strings contain exactly seven 0s and five 1s if every 1 must be immediately followed by a 0?
	all_ints = gen_bin_strings(5+7,5+7)
	sol = check_part_c(all_ints)
	print("Solution to part c: "+str(sol))
	return



def part_a():
	all_ints = gen_bin_strings(4+1, 5) # four 0s and one 1.
	print("gen_bin_strings == "+str(gen_bin_strings))
	sol = check_part_a(all_ints)
	print("Solution to part a: "+str(sol))
	return

def s():
	part_a()
	part_b()
	part_c()
	return

if __name__=="__main__":
	s()
	exit(0)
