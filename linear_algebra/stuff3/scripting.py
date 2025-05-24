
import numpy as np

def euc_norm(a,b):
	return np.dot(a,b)

def other_norm(a,b):
	mat = np.array([[1,1],[1,2]])
	return np.dot(np.dot(a, mat), b.T)

def calc_ans(y, b, norm_function):
	return norm_function(y,b) / norm_function(y,y)

def s():
	# Do calculations
	y = np.array([1,2]).T
	b = np.array([1,1]).T

	# Now calculate the first answer

	alpha_euclidean = calc_ans(y, b, euc_norm)
	alpha_other = calc_ans(y, b, other_norm)

	print("Alpha for euclidean norm: "+str(alpha_euclidean))
	print("Alpha for other norm: "+str(alpha_other))

	return

if __name__=="__main__":
	s()
	exit(0)
