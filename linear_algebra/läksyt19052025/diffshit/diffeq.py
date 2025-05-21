import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

def solve_and_plot(A, x0, t_values, title):
    # Compute x(t) = exp(A t) @ x0 for each t
    solutions = np.array([expm(A * t) @ x0 for t in t_values])
    print("Solutions when A == "+str(A)+" are these: "+str(solutions))
    # Plot each component of x(t)
    plt.plot(t_values, solutions[:, 0].real, label="x₁(t)")
    plt.plot(t_values, solutions[:, 1].real, label="x₂(t)")
    plt.xlabel("t")
    plt.ylabel("x(t)")
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Initial condition
x0 = np.array([1, 0])

# Time values
t_values = np.linspace(0, 5, 300)

# --- (a) A = [[3, -1], [1, 1]]
A1 = np.array([[3, -1],
               [1,  1]])
solve_and_plot(A1, x0, t_values, "Solution to x'(t) = A₁x(t) using matrix exponential")

# --- (b) A = [[1, 3], [3, 1]]
A2 = np.array([[1, 3],
               [3, 1]])
solve_and_plot(A2, x0, t_values, "Solution to x'(t) = A₂x(t) using matrix exponential")
