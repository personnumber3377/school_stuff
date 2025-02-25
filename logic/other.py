
import itertools

def impl(a,b) -> bool: # Implication. Python doesn't have an implication operator internally, so we define it like so.
	return not a or b

def f(p,q,r) -> bool: # The function we want to evaluate
	return (impl(p or q, ((q or r) or (not p or not r))))

def generate_all_inputs(n): # Generates all possible combinations of True and False of length n
	return list(itertools.product([False, True], repeat=n))

def check_tautology(function, num_args) -> bool: # False means not a tautology, True means it is
	all_inps = generate_all_inputs(num_args) # Generate all possible boolean inputs
	for args in all_inps: # Iterate over them
		if not f(*args): # If the statement evaluates to false
			return False # Then return False since not a tautology
	return True # Else if there does not exist an input which evaluates to False, then it must be a tautology

def s(): # Main function
	res = check_tautology(f, 3)
	print(res) # Is tautology?
	return

if __name__=="__main__":
	s() # Run program
	exit(0)
