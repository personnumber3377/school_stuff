
'''
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
	# print("Our H: "+str(h))
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
		#print("j == "+str(j))
		c[j] = z[j] - mu[j]*c[j+1] # Just do the bullshit here...
	for j in range(n - 1, -1, -1):
		b[j] = (a[j+1]-a[j])/h[j] + (h[j]*(2*c[j+1]+c[j]))/3.0
	for j in range(n - 1, -1, -1):
		d[j] = (c[j+1]-c[j])/(3.0*h[j])
	#print("Our c: "+str(c))
	#print("Our d: "+str(d))
	#print("Our b: "+str(b))
	#print("Our a: "+str(a))
	a.pop(0)
	c.pop(0)

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



import copy

def get_spline_natural_fifth_degree_one(knots: list, values: list) -> list: # This function returns the coefficients of the spline as a list. The points are of the format [[x0,y0],[x1,y1]...[xn,yn]] where each value is a float value.
	# This is taken straight from wikipedia: https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
	#x_vals = [p[0] for p in points]
	#y_vals = [p[1] for p in points]
	# 1. Create new array a of size n + 1 and for i = 0, …, n set a_i = y_i
	n = len(knots)-1
	# a = [y_vals[i] for i in range(len(y_vals))]#  + [0.0] # Initialize the thing.
	a = copy.deepcopy(values)
	assert len(a) == n + 1
	# a[-1] = 0.0 # Because the index 
	# 2. Create new arrays b and d, each of size n.
	assert len(a) == n + 1
	b = [0.0 for _ in range(n)]
	d = [0.0 for _ in range(n)]
	# 3. Create new array h of size n and for i = 0, …, n – 1 set h_i = x_(i+1) - x_i
	h = [knots[i+1] - knots[i] for i in range(n)]
	print("Our H: "+str(h))
	# 4. Create new array α of size n and for i = 1, …, n – 1 set alpha_1 = (3/h_i)*(a_(i+1) - a_i) - (3/h_(i-1))*(a_i-a_(i-1))
	alpha = [(3.0/h[i])*(a[i+1]-a[i])-(3.0/h[i-1])*(a[i]-a[i-1]) for i in range(1,n)] # Actually n-1, but because python ranges are dumb, we need to do this.
	

	# a.pop(-1)


	# alpha[i] = (3 / h[i]) * (values[i + 1] - values[i]) - (3 / h[i - 1]) * (values[i] - values[i 

	#alpha.append(0.0)
	alpha = [0.0] + alpha
	assert len(alpha) == n
	# 5. Create new arrays c, l, μ, z, each of size n + 1.
	c = [0.0 for _ in range(n+1)]
	assert len(c) == len(knots)
	l = [0.0 for _ in range(n+1)]
	mu = [0.0 for _ in range(n+1)]
	z = [0.0 for _ in range(n+1)]
	# 6. Set l_0 = 1 , mu_0 = z_0 = 0
	l[0] = 1.0
	mu[0] = 0.0
	z[0] = 0.0
	# 7. For i = 1 .. n-1 set the following: l_i = 2*(x_(i+1)-x_(i-1))-(h_(i-1))*(mu_(i-1))	mu_i = h_i/l_i   z_i = (alpha_i-h_(i-1)*z_(i-1))/l_i
	for i in range(1, n):
		l[i] = 2*(knots[i+1]-knots[i-1])-(h[i-1])*(mu[i-1]) # Stuff.    (values[j + 1] - values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
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
		b[j] = (values[j+1]-values[j])/h[j] + (h[j]*(2*c[j+1]+c[j]))/3.0   # (values[j + 1] - values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
	for j in range(n - 1, -1, -1):
		d[j] = (c[j+1]-c[j])/(3.0*h[j])
	print("Our c: "+str(c))
	print("Our d: "+str(d))
	print("Our b: "+str(b))
	print("Our a: "+str(a))
	a.pop(0)
	c.pop(0)

	# Create new set "Splines" and call it "output_set". Populate it with n splines S.
	splines = [[] for _ in range(5)]
	for i in range(n):
		#splines.append([a[i], b[i], c[i], d[i], x_vals[i]])
		splines[0].append(a[i])
		splines[1].append(b[i])
		splines[2].append(c[i])
		splines[3].append(d[i])
		splines[4].append(knots[i])

	return splines # Return the output....
'''











'''
def get_spline_natural_fifth_degree(x_vals, y_vals):
	# This is taken straight from wikipedia: https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
	#x_vals = [p[0] for p in points]
	#y_vals = [p[1] for p in points]
	x_vals = list(x_vals)
	y_vals = list(y_vals)
	# 1. Create new array a of size n + 1 and for i = 0, …, n set a_i = y_i
	n = len(x_vals)-1
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
	assert len(c) == len(x_vals)
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
	# a.pop(0)
	a.pop(-1)
	# c.pop(0)
	c.pop(-1)

	# Create new set "Splines" and call it "output_set". Populate it with n splines S.
	splines = [[] for _ in range(4)]
	for i in range(n):
		#splines.append([a[i], b[i], c[i], d[i], x_vals[i]])
		splines[0].append(a[i])
		splines[1].append(b[i])
		splines[2].append(c[i])
		splines[3].append(d[i])
		#splines[4].append(x_vals[i])

	return splines # Return the output....
'''


















'''
def get_spline_natural_fifth_degree(x_vals, y_vals):
	# This is taken straight from wikipedia: https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
	#x_vals = [p[0] for p in points]
	#y_vals = [p[1] for p in points]
	x_vals = list(x_vals)
	y_vals = list(y_vals)
	# 1. Create new array a of size n + 1 and for i = 0, …, n set a_i = y_i
	n = len(x_vals)-1
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
	assert len(c) == len(x_vals)
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
	
	a.pop(-1)
	# c.pop(0)


	print("Our c: "+str(c))
	print("Our d: "+str(d))
	print("Our b: "+str(b))
	print("Our a: "+str(a))


	# Create new set "Splines" and call it "output_set". Populate it with n splines S.
	splines = [[] for _ in range(4)]
	for i in range(n):
		#splines.append([a[i], b[i], c[i], d[i], x_vals[i]])
		splines[0].append(a[i])
		splines[1].append(b[i])
		splines[2].append(c[i])
		splines[3].append(d[i])
		#splines[4].append(x_vals[i])

	return splines # Return the output....


'''


























def get_spline_natural_fifth_degree(x_vals, y_vals):
	# This is taken straight from wikipedia: https://en.wikipedia.org/wiki/Spline_(mathematics)#Algorithm_for_computing_natural_cubic_splines
	#x_vals = [p[0] for p in points]
	#y_vals = [p[1] for p in points]
	x_vals = list(x_vals)
	y_vals = list(y_vals)
	# 1. Create new array a of size n + 1 and for i = 0, …, n set a_i = y_i
	n = len(x_vals)-1
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
	assert len(c) == len(x_vals)
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
	
	a.pop(0)
	c.pop(0)
	# c.append(0.0)

	print("Our c: "+str(c))
	print("Our d: "+str(d))
	print("Our b: "+str(b))
	print("Our a: "+str(a))

	'''

	b = (a[1:] - a[:-1]) / h + (2 * c[1:] + c[:-1]) / 3 * h
	# b[j] = (a[j+1]-a[j])/h[j] - (h[j]*(c[j+1]+2*c[j]))/3.0
	'''
	# Create new set "Splines" and call it "output_set". Populate it with n splines S.
	splines = [[] for _ in range(4)]
	for i in range(n):
		#splines.append([a[i], b[i], c[i], d[i], x_vals[i]])
		splines[0].append(a[i])
		splines[1].append(b[i])
		splines[2].append(c[i])
		splines[3].append(d[i])
		#splines[4].append(x_vals[i])

	return splines # Return the output....












