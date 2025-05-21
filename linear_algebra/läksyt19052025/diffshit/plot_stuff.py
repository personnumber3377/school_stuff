import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import norm, inv

def compute_condition(delta):
    # Build A and its diagonalization manually
    # A = np.array([[1, 1],
    #               [0, 1 + 2*delta]], dtype=np.complex128)

    # Eigenvalues: 1, 1 + 2*delta
    # Eigenvectors: manually constructed to match sympy's scaled version
    # Eigenvector matrix V with first row [1, 1]
    V = np.array([[1, 1],
                  [0, 2*delta]], dtype=np.complex128)

    # Compute condition number using 2-norm
    kappa = norm(V, 2) * norm(inv(V), 2)
    return kappa

def plot_condition():
    deltas = np.logspace(np.log10(0.5e-4), np.log10(0.5), 4000)
    condition_numbers = [compute_condition(d) for d in deltas]

    plt.figure(figsize=(8, 5))
    plt.semilogy(deltas, condition_numbers)
    plt.xlabel(r'$\delta$')
    plt.ylabel(r'$\kappa_2(V)$')
    plt.title(r'Condition number of $V$ vs. $\delta$')
    plt.grid(True, which='both', linestyle='--')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_condition()