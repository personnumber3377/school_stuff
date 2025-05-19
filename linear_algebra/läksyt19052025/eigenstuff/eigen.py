
import numpy as np
import math
import matplotlib.pyplot as plt

def rayleigh(x, A):
    x = np.asarray(x)
    numerator = np.vdot(x, A @ x)  # vdot does conjugate transpose of x automatically
    denominator = np.vdot(x, x)

    if denominator == 0:
        raise ValueError("Input vector x must be nonzero.")
    
    return numerator / denominator

def iter(x0, A, max_i): # Iterate Ax_i / ||Ax_i||_2 for i times.
    x = x0 # Set initial guess
    errors = []
    correct_result = 2 + math.sqrt(2) # This is the actual result calculated symbolically
    for _ in range(max_i):
        x = (A @ x) / np.linalg.norm(A @ x)
        # Calculate the error thing
        errors.append(correct_result - rayleigh(x, A))
    return rayleigh(x, A), errors

def s():
    A = np.array([[2,1,0],[1,2,1],[0,1,2]])
    # Now we have the test vector here...
    x0 = np.array([1,0,0]).T

    res, errs = iter(x0, A, 10)
    print(errs)
    print(res)
    idxs = [x+1 for x in list(range(0,10))] # Because math is 1 indexed, we need to do this kinda stuff
    # Create the plot
    plt.plot(idxs, errs, marker='o', linestyle='-', color='b')  # blue line with dots
    plt.xlabel('i values')
    plt.ylabel('error')
    plt.title('Plot of Two Lists')
    plt.grid(True)
    plt.show()

    return

if __name__=="__main__":
    s()
    exit()
