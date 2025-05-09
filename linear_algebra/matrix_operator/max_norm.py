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

def s():
	# Solve the problem: Run the tests
	test_max_entry_norm()  # Run the max-entry norm counterexample test

if __name__ == "__main__":
	s()
