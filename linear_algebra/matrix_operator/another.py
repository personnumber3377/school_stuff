import numpy as np

def frob_norm(A): 
	# Frobenius norm: sqrt(sum(abs(A)**2))
	return np.sqrt(np.sum(np.abs(A)**2))

def max_entry_norm(A):
	# Max-entry norm: max(|a_ij| for all i, j)
	return np.max(np.abs(A))

def l2_norm(x): 
	# Euclidean norm: sqrt(sum(x**2))
	return np.sqrt(np.sum(x**2))

def operator_norm_2d(A, vector_norm, step_degrees=0.1):
	"""
	Compute the operator norm of a 2x2 matrix A by sweeping over unit circle directions.
	"""
	assert A.shape == (2, 2), "Only works for 2x2 matrices"

	max_stretch = 0.0
	for deg in np.arange(0, 360, step_degrees):
		theta = np.deg2rad(deg)
		x = np.array([np.cos(theta), np.sin(theta)])
		Ax = A @ x
		stretch = vector_norm(Ax)
		max_stretch = max(max_stretch, stretch)

	return max_stretch

def check_norm(A, B=None, vector_norm=None, operator_norm=None, verbose=True):
	"""
	Checks whether the norm satisfies:
	1. ||Ax|| <= ||A|| * ||x||  for x on the unit circle
	2. ||AB|| <= ||A|| * ||B||  (if B is provided)
	3. ||I|| == 1
	"""

	assert A.shape == (2, 2)
	if B is not None:
		assert B.shape == (2, 2)

	# 1. ||Ax|| <= ||A|| * ||x|| for all unit x
	opA = operator_norm(A, vector_norm)
	holds_1 = True
	for deg in np.arange(0, 360, 1):
		theta = np.deg2rad(deg)
		x = np.array([np.cos(theta), np.sin(theta)])
		Ax = A @ x
		lhs = vector_norm(Ax)
		rhs = opA * vector_norm(x)
		if lhs > rhs + 1e-8:
			holds_1 = False
			break

	# 2. ||AB|| <= ||A|| * ||B||
	holds_2 = None
	if B is not None:
		opB = operator_norm(B, vector_norm)
		AB = A @ B
		opAB = operator_norm(AB, vector_norm)
		holds_2 = opAB <= opA * opB + 1e-8

	# 3. ||I|| = 1
	I = np.eye(2)
	opI = operator_norm(I, vector_norm)
	holds_3 = abs(opI - 1.0) < 1e-8

	if verbose:
		print(f"||A|| = {opA:.4f}")
		if B is not None:
			print(f"||B|| = {opB:.4f}")
			print(f"||AB|| = {opAB:.4f}, ||A||·||B|| = {opA * opB:.4f}")
		print(f"||I|| = {opI:.4f}")
		print(f"Check 1 (||Ax|| ≤ ||A||·||x||): {'PASS' if holds_1 else 'FAIL'}")
		if holds_2 is not None:
			print(f"Check 2 (||AB|| ≤ ||A||·||B||): {'PASS' if holds_2 else 'FAIL'}")
		print(f"Check 3 (||I|| = 1): {'PASS' if holds_3 else 'FAIL'}")

	return {
		"Ax_bound": holds_1,
		"AB_bound": holds_2,
		"I_norm_one": holds_3
	}

# Counterexample check for max-entry norm and Frobenius norm
def test_max_entry_norm():
	# Example matrices A and B for max-entry norm counterexample
	A = np.random.rand(2, 2)
	B = np.random.rand(2, 2)

	# Calculate max-entry norms
	maxA = max_entry_norm(A)
	maxB = max_entry_norm(B)

	# Compute AB and check max-entry norm
	AB = A @ B
	maxAB = max_entry_norm(AB)

	print("\nTesting max-entry norm counterexample:")
	print(f"||A||max = {maxA}")
	print(f"||B||max = {maxB}")
	print(f"||AB||max = {maxAB}")
	print(f"Check ||AB||max <= ||A||max * ||B||max: {maxAB <= maxA * maxB}")
	
def test_frobenius_norm():
	# Example matrices A and B for Frobenius norm counterexample
	A = np.random.rand(2, 2)
	B = np.random.rand(2, 2)

	# Calculate Frobenius norms
	frobA = frob_norm(A)
	frobB = frob_norm(B)

	# Compute AB and check Frobenius norm
	AB = A @ B
	frobAB = frob_norm(AB)

	print("\nTesting Frobenius norm counterexample:")
	print(f"||A||F = {frobA}")
	print(f"||B||F = {frobB}")
	print(f"||AB||F = {frobAB}")
	print(f"Check ||AB||F <= ||A||F * ||B||F: {frobAB <= frobA * frobB}")

def s():
	# Solve the problem: Run the tests
	test_max_entry_norm()  # Run the max-entry norm counterexample test
	test_frobenius_norm()  # Run the Frobenius norm counterexample test

if __name__ == "__main__":
	s()