#!/bin/python3

# These next two libraries are purely for displaying the result...
import matplotlib.pyplot as plt
import numpy as np
from spline import *
from scipy.interpolate import CubicSpline

def evaluate_spline(x, x_i, a, b, c, d):
	return a + b * (x - x_i) + c * (x - x_i)**2 + d * (x - x_i)**3

def correct_interval(x, intervals):
	#assert all([intervals[i+1]>=intervals[i] for i in range(len(intervals)-1)]) # Should be sorted.
	#assert x >= intervals[0] and x <= intervals[-1] # Should be within the shit.
	
	# Now loop over each element and check the thing.
	for i in range(len(intervals)-1):
		# Now calculate the shit here...
		if x >= intervals[i] and x <= intervals[i+1]:
			return i, intervals[i] # Return the index thing... 
	assert False

'''
def calculate_spline(x, x_stuff, splines):
	# This function checks the correct interval and then evaluates the thing...

	i, x0 = correct_interval(x, x_stuff) # This is the index into the bullshit.
	# a, b, c, d, _ = splines[0][i], splines[1][i], splines[2][i], splines[3][i], splines[4][i]
	a, b, c, d, _ = splines[0][i], splines[1][i], splines[2][i], splines[3][i], splines[4][i]
	# Now evaluate.

	return evaluate_spline(x, x0, a, b, c, d)


get_spline_natural_fifth_degree_one
'''


def calculate_spline(x, t_knots, splines):
	i, t0 = correct_interval(x, t_knots)
	#print("Correct interval: "+str(i))
	if len(splines[0]) == 5:
			a, b, c, d, _ = splines[0][i], splines[1][i], splines[2][i], splines[3][i], splines[4][i]
	else:
		a, b, c, d = splines[0][i], splines[1][i], splines[2][i], splines[3][i]# , splines[4][i]
	return evaluate_spline(x, t0, a, b, c, d)


def compute_t_knots(points):
	""" Computes t values based on cumulative distance along the curve. """
	t_knots = [0]
	for i in range(1, len(points)):
		dist = np.sqrt((points[i][0] - points[i - 1][0])**2 + (points[i][1] - points[i - 1][1])**2)
		t_knots.append(t_knots[-1] + dist)  # Accumulate distances
	return t_knots

def render_result(x_splines: list, y_splines: list, points: list, t_knots: list) -> None:
	x_knots = [p[0] for p in points] # Something like this????
	y_knots = [p[1] for p in points]

	n = len(points)
	# t_knots = np.linspace(-3, 3, n)

	t_values = np.linspace(max(t_knots), min(t_knots), 20000)

	# Compute interpolated x and y values
	x_things = [calculate_spline(t, t_knots, x_splines) for t in t_values]
	y_things = [calculate_spline(t, t_knots, y_splines) for t in t_values]


	plt.plot(x_things, y_things, label="Cubic Spline Curve")
	plt.scatter(x_knots, y_knots, color="red", label="Control Points")
	#plt.scatter(t_knots, y_knots, color="green", label="Tknots, yknots")
	#plt.scatter(t_knots, x_knots, color="brown", label="Tknots, xknots")

	#plt.scatter(y_knots, t_knots, color="green", label="Tknots, yknots")
	#plt.scatter(x_knots, t_knots, color="brown", label="Tknots, xknots")
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.title('Spline Graph Using Manually Calculated Coefficients')
	plt.grid(True)
	plt.show()
	return

from math import sqrt

def compute_t_range(points):
	t_knots = [0]
	for i in range(1, len(points)):
		dist = sqrt((points[i][0] - points[i - 1][0])**2 + (points[i][1] - points[i - 1][1])**2)
		t_knots.append(t_knots[-1] + dist)  # Accumulate distances
	return t_knots

if __name__=="__main__":
	x_vals=[-0.83,0.14,-1.09,1.09,-0.54,2.03,3.0]
	y_vals=[-2.03,-2.06,0.71,1.49,2.06,2.43,3.0]

	assert len(x_vals) == len(y_vals)
	assert all([isinstance(x, float) for x in x_vals])
	assert all([isinstance(x, float) for x in y_vals])
	points = [[x_vals[i], y_vals[i]] for i in range(len(x_vals))] # Just do the thing...
	# splines = get_spline_natural_fifth_degree(points) # This function is taken from spline.py in this directory.
	x_knots = [p[0] for p in points]
	y_knots = [p[1] for p in points]

	t_i = compute_t_knots(points)

	# t_i = np.linspace(-3,3, 10000) # compute_t_range(points)

	#x_splines = get_spline_natural_fifth_degree_one(x_vals)
	#y_splines = get_spline_natural_fifth_degree_one(y_vals)
	# spline_x = get_spline_natural_fifth_degree_one(t_knots, x_knots)
	# spline_y = get_spline_natural_fifth_degree_one(t_knots, y_knots)
	assert len(t_i) == len(points) == len(x_knots) == len(y_knots)
	points_x_t = [(t_i[i], x_knots[i]) for i in range(len(t_i))]
	points_y_t = [(t_i[i], y_knots[i]) for i in range(len(t_i))]

	spline_x_reference = CubicSpline(t_i, x_knots).c
	spline_y_reference = CubicSpline(t_i, y_knots).c

	spline_x = get_spline_natural_fifth_degree(t_i, x_knots)
	spline_y = get_spline_natural_fifth_degree(t_i, y_knots)


	# spline_y = CubicSpline(t, y)
	spline_x_reference = list(spline_x_reference)
	spline_y_reference = list(spline_y_reference)
	spline_x_reference.reverse()
	spline_y_reference.reverse()

	print("Here is my spline_x: "+str(spline_x))
	print("Here is spline_x_reference: "+str(spline_x_reference))
	# render_result(spline_x, spline_y, points, t_i)
	render_result(spline_x, spline_y, points, t_i)
	exit(0)
