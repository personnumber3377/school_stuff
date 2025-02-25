#!/bin/python3

# These next two libraries are purely for displaying the result...
import matplotlib.pyplot as plt
import numpy as np

def get_spline_natural_fifth_degree(points: list) -> list: # This function returns the coefficients of the spline as a list. The points are of the format [[x0,y0],[x1,y1]...[xn,yn]] where each value is a float value.
	# This is taken straight from wikipedia: https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
	x_vals = [p[0] for p in points]
	y_vals = [p[1] for p in points]
	# 1. Create new array a of size n + 1 and for i = 0, …, n set a_i = y_i
	n = len(points)-1
	a = [y_vals[i] for i in range(len(y_vals))]#  + [0.0] # Initialize the thing.
	assert len(a) == n + 1
	# a[-1] = 0.0 # Because the index 
	# 2. Create new arrays b and d, each of size n.
	assert len(a) == n + 1
	b = [0.0 for _ in range(n)]
	d = [0.0 for _ in range(n)]
	# 3. Create new array h of size n and for i = 0, …, n – 1 set h_i = x_(i+1) - x_i
	h = [x_vals[i+1] - x_vals[i] for i in range(n)]
	print("Our H: "+str(h))
	# 4. Create new array α of size n and for i = 1, …, n – 1 set alpha_1 = (3/h_i)*(a_(i+1) - a_i) - (3/h_(i-1))*(a_i-a_(i-1))
	alpha = [(3.0/h[i])*(a[i+1]-a[i])-(3.0/h[i-1])*(a[i]-a[i-1]) for i in range(1,n)] # Actually n-1, but because python ranges are dumb, we need to do this.
	#alpha.append(0.0)
	alpha = [0.0] + alpha
	assert len(alpha) == n
	# 5. Create new arrays c, l, μ, z, each of size n + 1.
	c = [0.0 for _ in range(n+1)]
	assert len(c) == len(points)
	l = [0.0 for _ in range(n+1)]
	mu = [0.0 for _ in range(n+1)]
	z = [0.0 for _ in range(n+1)]
	# 6. Set l_0 = 1 , mu_0 = z_0 = 0
	l[0] = 1.0
	mu[0] = 0.0
	z[0] = 0.0
	# 7. For i = 1 .. n-1 set the following: l_i = 2*(x_(i+1)-x_(i-1))-(h_(i-1))*(mu_(i-1))	mu_i = h_i/l_i   z_i = (alpha_i-h_(i-1)*z_(i-1))/l_i
	for i in range(1, n):
		l[i] = 2*(x_vals[i+1]-x_vals[i-1])-(h[i-1])*(mu[i-1]) # Stuff.
		mu[i] = h[i]/l[i]
		z[i] = (alpha[i]-h[i-1]*z[i-1])/l[i]
	assert l[0] == 1.0
	# 8. Set l_n = 1; z_n = c_n = 0
	l[n] = 1.0
	assert c[n] == 0.0 # Should be zero...
	z[n] = 0.0
	# 9. For j = n – 1, n – 2, …, 0, set the following: c_j = z_j - mu_j*c_(j+1)   b_j = (a_(j+1)-a_j)/h_j - (h_j*(c_(j+1)+2*c_j))/3	and   d_j = (c_(j+1)-c_j)/(3*h_j)
	for j in range(n - 1, -1, -1):
		print("j == "+str(j))
		c[j] = z[j] - mu[j]*c[j+1] # Just do the bullshit here...
	for j in range(n - 1, -1, -1):
		b[j] = (a[j+1]-a[j])/h[j] + (h[j]*(2*c[j+1]+c[j]))/3.0
	for j in range(n - 1, -1, -1):
		d[j] = (c[j+1]-c[j])/(3.0*h[j])
	print("Our c: "+str(c))
	print("Our d: "+str(d))
	print("Our b: "+str(b))
	print("Our a: "+str(a))
	a.pop(0)
	c.pop(0)
	'''

	b = (a[1:] - a[:-1]) / h + (2 * c[1:] + c[:-1]) / 3 * h
	# b[j] = (a[j+1]-a[j])/h[j] - (h[j]*(c[j+1]+2*c[j]))/3.0
	'''
	# Create new set "Splines" and call it "output_set". Populate it with n splines S.
	splines = [[] for _ in range(5)]
	for i in range(n):
		#splines.append([a[i], b[i], c[i], d[i], x_vals[i]])
		splines[0].append(a[i])
		splines[1].append(b[i])
		splines[2].append(c[i])
		splines[3].append(d[i])
		splines[4].append(x_vals[i])

	return splines # Return the output....


def tri_diag_solve(A, B, C, F):
	n = B.size
	assert A.ndim == B.ndim == C.ndim == F.ndim == 1 and (
		A.size == B.size == C.size == F.size == n
	) #, (A.shape, B.shape, C.shape, F.shape)
	Bs, Fs = np.zeros_like(B), np.zeros_like(F)
	Bs[0], Fs[0] = B[0], F[0]
	for i in range(1, n):
		Bs[i] = B[i] - A[i] / Bs[i - 1] * C[i - 1]
		Fs[i] = F[i] - A[i] / Bs[i - 1] * Fs[i - 1]
	x = np.zeros_like(B)
	x[-1] = Fs[-1] / Bs[-1]
	for i in range(n - 2, -1, -1):
		x[i] = (Fs[i] - C[i] * x[i + 1]) / Bs[i]
	return x
	

def calc_spline_params(x, y):
	a = y
	h = np.diff(x)
	print("Actual H: "+str(h))
	c = np.concatenate((np.zeros((1,), dtype = y.dtype),
		np.append(tri_diag_solve(h[:-1], (h[:-1] + h[1:]) * 2, h[1:],
		((a[2:] - a[1:-1]) / h[1:] - (a[1:-1] - a[:-2]) / h[:-1]) * 3), 0)))
	print("Actual c: "+str(c))
	d = np.diff(c) / (3 * h)
	print("Actual d: "+str(d))
	print("Actual a: "+str(a))
	b = (a[1:] - a[:-1]) / h + (2 * c[1:] + c[:-1]) / 3 * h
	# b[j] = (a[j+1]-a[j])/h[j] - (h[j]*(c[j+1]+2*c[j]))/3.0
	print("Actual b: "+str(b))

	return a[1:], b, c[1:], d

def test_spline() -> None: # This function here tests our implementation of splines...
	# These values are taken straight from my homework assignment...
	x_vals=[-0.83,0.14,-1.09,1.09,-0.54,2.03,3.0]
	y_vals=[-2.03,-2.06,0.71,1.49,2.06,2.43,3.0]

	assert len(x_vals) == len(y_vals)
	assert all([isinstance(x, float) for x in x_vals])
	assert all([isinstance(x, float) for x in y_vals])
	points = [[x_vals[i], y_vals[i]] for i in range(len(x_vals))] # Just do the thing...
	spline_vals = get_spline_natural_fifth_degree(points)
	print("Output: ")
	print(spline_vals)
	return spline_vals

def evaluate_spline(x, x_i, a, b, c, d):
	return a + b * (x - x_i) + c * (x - x_i)**2 + d * (x - x_i)**3

def genfines(x_knots) -> list:
	# np.linspace(x_knots[0], x_knots[-1], 1000)
	output = []
	for i in range(len(x_knots)-1):
		# Just go through the things...
		x0 = x_knots[i]
		x1 = x_knots[i+1]
		output.append(np.linspace(x0, x1, num=1000, endpoint=True, retstep=False, dtype=None, axis=0))
	return output

def correct_interval(x, intervals):
	#assert all([intervals[i+1]>=intervals[i] for i in range(len(intervals)-1)]) # Should be sorted.
	#assert x >= intervals[0] and x <= intervals[-1] # Should be within the shit.
	
	# Now loop over each element and check the thing.
	for i in range(len(intervals)-1):
		# Now calculate the shit here...
		if x >= intervals[i] and x <= intervals[i+1]:
			return i, intervals[i] # Return the index thing... 
	assert False

def calculate_spline(x, x_stuff, splines):
	# This function checks the correct interval and then evaluates the thing...

	i, x0 = correct_interval(x, x_stuff) # This is the index into the bullshit.
	# a, b, c, d, _ = splines[0][i], splines[1][i], splines[2][i], splines[3][i], splines[4][i]
	a, b, c, d, _ = splines[0][i], splines[1][i], splines[2][i], splines[3][i], splines[4][i]
	# Now evaluate.

	return evaluate_spline(x, x0, a, b, c, d)

def render_result(splines: list, points: list) -> None:
	x_knots = [p[0] for p in points] # Something like this????
	y_knots = [p[1] for p in points]

	# Evaluate the spline on each interval
	start = -1.5
	end = 1.5
	count = 1000

	t_values = [start+(end-start)/count*i for i in range(count)]

	#t_values = np.array(t_values)
	y_things = []
	x_things = []
	x_stuff = x_knots
	for t_val in t_values:
		# calculate_spline   calculate_spline(x, x_stuff, splines):
		x_things.append(calculate_spline(t_val, x_stuff, splines))

	y_stuff = y_knots
	for t_val in t_values:
		# calculate_spline   calculate_spline(x, x_stuff, splines):
		y_things.append(calculate_spline(t_val, y_stuff, splines))


	plt.plot(x_things, y_things, label='Cubic Spline Curve')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.legend()
	plt.title('Spline Graph Using Manually Calculated Coefficients')
	plt.grid(True)
	plt.show()
	return


if __name__=="__main__":
	x_vals=[-0.83,0.14,-1.09,1.09,-0.54,2.03,3.0]
	y_vals=[-2.03,-2.06,0.71,1.49,2.06,2.43,3.0]

	assert len(x_vals) == len(y_vals)
	assert all([isinstance(x, float) for x in x_vals])
	assert all([isinstance(x, float) for x in y_vals])
	points = [[x_vals[i], y_vals[i]] for i in range(len(x_vals))] # Just do the thing...
	splines = test_spline()
	actual = calc_spline_params(np.array(x_vals), np.array(y_vals))
	print("Our splines: "+str(splines))
	print("Actual splines: "+str(actual))
	render_result(splines, points)
	exit(0)
