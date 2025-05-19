from scipy.optimize import minimize
import numpy as np

def inner_product(x): # The inner product given in the exercise.
    return 1/3*(x[0]**2)+x[0]*x[1]+(x[1]**2)


CHECK_COUNT = 1000

A = np.array([
    [1.0, 1.0],
    [1.0, 1.0]
])

x_samples = np.random.uniform(-10, 10, size=(CHECK_COUNT, 2))


def error_sym(params):
    a, b, d = params
    A = np.array([[a, b], [b, d]])
    return np.mean([
        abs(inner_product(x) - x.T @ A @ x)
        for x in x_samples # np.random.uniform(-10, 10, size=(CHECK_COUNT, 2))
    ])

res = minimize(error_sym, x0=[0, 0, 0])  # Start from zero or another good guess
a, b, d = res.x
A_optimized = np.array([[a, b], [b, d]])
print(A_optimized)



'''
error = lambda A_flat: np.mean([
    abs(inner_product(x) - x.T @ A.reshape(2, 2) @ x)
    for x in np.random.uniform(-10, 10, size=(CHECK_COUNT, 2))
])
'''



'''
res = minimize(error, A.flatten())
A_optimized = res.x.reshape(2, 2)
print(A_optimized)
'''




