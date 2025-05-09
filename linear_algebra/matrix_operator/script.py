



import numpy as np

def frob_norm(A): # Frobenius norm thing....
	return np.sqrt(np.sum(np.abs(A)**2))

def max_entry_norm(A):
	"""
	Compute the max-entry norm of a matrix A, i.e., max(|a_ij| for all i, j)
	"""
	return np.max(np.abs(A))



def l2_norm(x): # Just euclidean norm as an example
	return np.sqrt(np.sum(x**2))


def check_norm(A, B=None, vector_norm=None, operator_norm=None, verbose=True):
	"""
	Checks whether the norm satisfies:
	1. ||Ax|| <= ||A|| * ||x||  for x on the unit circle
	2. ||AB|| <= ||A|| * ||B||  (if B is provided)
	3. ||I|| == 1

	Parameters:
		A (np.ndarray): Matrix A (2x2)
		B (np.ndarray): Optional matrix B (2x2)
		vector_norm (function): Function to compute vector norm
		operator_norm (function): Function to compute operator norm
		verbose (bool): Whether to print intermediate results

	Returns:
		dict: Dictionary with results of checks
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
		if lhs > rhs + 1e-8:  # allow small numerical error
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


def operator_norm_2d(A, vector_norm, step_degrees=0.1): # vector_norm is assumed to be the function which calculates the thing...
	"""
	Compute the operator norm of a 2x2 matrix A by sweeping over unit circle directions.

	Parameters:
		A (np.ndarray): A 2x2 matrix.
		vector_norm (callable): Function to compute vector norm.
		step_degrees (float): Step size in degrees for angle sweep.

	Returns:
		float: Estimated operator norm.
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


def s():
	# Solve the problem
	A = np.random.rand(2, 2) # Generate a random matrix to check the stuff...
	B = np.random.rand(2, 2) # Generate another random matrix

	# def check_norm(A, B=None, vector_norm=None, operator_norm=None, verbose=True):

	# Now check the things...

	# check_norm(A, B=B, vector_norm=l2_norm, operator_norm=max_entry_norm)
	# check_norm(A, B=B, vector_norm=l2_norm, operator_norm=frob_norm)

	check_norm(A, B=B, vector_norm=l2_norm, operator_norm_func=operator_norm_2d)
	check_norm(A, B=B, vector_norm=l2_norm, operator_norm_func=operator_norm_2d)

	return

if __name__=="__main__":
	s()
	exit()
