import numpy as np
import matplotlib.pyplot as plt

def rk4(f, y0, t_range, dt):
    """
    Solves the ODE dy/dt = f(y, t) using the Runge-Kutta 4 method.

    Parameters:
    f      - Function f(y, t) defining the ODE.
    y0     - Initial condition (float or array).
    t_range - Tuple (t_start, t_end).
    dt     - Time step.

    Returns:
    t_vals - Array of time values.
    y_vals - Array of solution values.
    """
    t_start, t_end = t_range
    t_vals = np.arange(t_start, t_end, dt)
    y_vals = np.zeros(len(t_vals))
    
    y = y0
    for i, t in enumerate(t_vals):
        y_vals[i] = y
        k1 = dt * f(y, t)
        k2 = dt * f(y + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * f(y + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * f(y + k3, t + dt)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6  # RK4 update

    return t_vals, y_vals

# Example: Solve f' = f + 2
def ode_func(y, t):
    return y + 2  # Example ODE

# Solve from t = 0 to 5 with step size dt = 0.1
t_vals, y_vals = rk4(ode_func, y0=1, t_range=(0, 5), dt=0.1)

# Plot the solution
plt.plot(t_vals, y_vals, label="Numerical Solution")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.title("Solution to df/dt = f + 2")
plt.legend()
plt.show()