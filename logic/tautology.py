
import itertools

def impl(a,b) -> bool: # Implication
	return not a or b

def f(p,q,r) -> bool: # The function
	return (impl(p or q, ((q or r) or (not p or not r))))

def generate_all_inputs(n):
	return list(itertools.product([False, True], repeat=n))

def check_tautology(function, num_args) -> int: # 0 is always false, 1 is always true and 2 means that it is not a tautology
	all_inps = generate_all_inputs(num_args)
	for args in all_inps:
		if not f(*args):
			return False
	return True

def show_impl():
	all_inps = generate_all_inputs(2)
	for args in all_inps:
		print(args)
		print(impl(*args))
	return

def s():
	res = check_tautology(f, 3)
	print(res)
	show_impl()
	return
if __name__=="__main__":
	s()
	exit(0)
