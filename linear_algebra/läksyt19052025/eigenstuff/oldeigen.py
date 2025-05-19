
import numpy as np

def rayleigh(x, A):
    x = np.asarray(x)
    numerator = np.vdot(x, A @ x)  # vdot does conjugate transpose of x automatically
    denominator = np.vdot(x, x)

    if denominator == 0:
        raise ValueError("Input vector x must be nonzero.")
    
    return numerator / denominator

def iter(x0, A, max_i): # Iterate Ax_i / ||Ax_i||_2 for i times.
    x = x0 # Set initial guess
    for _ in range(max_i + 1):
        x = (A @ x) / np.linalg.norm(A @ x)
    return rayleigh(x, A)

def s():
    A = np.array([[2,1,0],[1,2,1],[0,1,2]])
    # Now we have the test vector here...
    x0 = np.array([1,0,0]).T

    res = iter(x0, A, 10)

    print(res)

    return

if __name__=="__main__":
    s()
    exit()
