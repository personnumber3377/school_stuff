
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

def tria(t):
	# The triangular wave function
	if -1 <= t and t < 0:
		return 1 + t
	elif 0 <= t and t <= 1:
		return 1 - t
	return 0

# This is needed to make the function usable in sympy
class Tria(Function):
	@classmethod
	def eval(cls, t):
		if t.is_Number:
			return tria(t)

def s():
	# Problem 1
	# Solve the thing...
	t = symbols("t") # Define the t symbol
	x1_t = 2*Tria((t - 1/2) / (1/2))
	x2_t = -2*Tria((t+1/2)/(1/2))

	# Convert symbolic expressions to numerical functions
	x1 = lambdify(t, x1_t, modules=["numpy", {"Tria": np.vectorize(tria)}])
	x2 = lambdify(t, x2_t, modules=["numpy", {"Tria": np.vectorize(tria)}])

	# Define time range
	t_vals = np.linspace(-2, 2, 1000)

	# Evaluate the functions
	x1_vals = x1(t_vals)
	x2_vals = x2(t_vals)

	print("x1_vals: "+str(x1_vals))

	# Plotting
	plt.figure()
	plt.plot(t_vals, x1_vals, label='x1(t)')
	plt.plot(t_vals, x2_vals, label='x2(t)')
	plt.title("Triangular Functions")
	plt.xlabel("t")
	plt.ylabel("Amplitude")
	plt.grid(True)
	plt.legend()
	plt.show()

	return


if __name__=="__main__":
	s()
	exit()
