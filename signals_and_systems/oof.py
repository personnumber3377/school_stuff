
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

def x1_t(t):
	return 2*tria((t - 1/2) / (1/2))

def x2_t(t):
	return -2*tria((t+1/2)/(1/2))

def s():
	# Problem 1
	# Solve the thing...

	# Define time range
	t_vals = np.linspace(-2, 2, 1000)

	# Evaluate the functions
	x1_vals = np.array([x1_t(t_val) for t_val in t_vals])
	x2_vals = np.array([x2_t(t_val) for t_val in t_vals])

	# Plotting
	plt.figure()
	plt.plot(t_vals, x1_vals, label='x1(t)')
	plt.plot(t_vals, x2_vals, label='x2(t)')
	plt.title("Plotted functions")
	plt.xlabel("t")
	plt.ylabel("Amplitude")
	plt.grid(True)
	plt.legend()
	plt.savefig('plotted.eps', format='eps') # Save as file.
	plt.show()

	return


if __name__=="__main__":
	s()
	exit()
