import numpy as np
import matplotlib.pyplot as plt

def compute_t_knots(points):
    """ Computes t values based on cumulative distance along the curve. """
    t_knots = [0]
    for i in range(1, len(points)):
        dist = np.sqrt((points[i][0] - points[i - 1][0])**2 + (points[i][1] - points[i - 1][1])**2)
        t_knots.append(t_knots[-1] + dist)  # Accumulate distances
    return t_knots

def compute_spline_coeffs(t_knots, values):
    """ Computes natural cubic spline coefficients for given t-values and values (x or y). """
    n = len(t_knots) - 1  # Number of spline segments
    h = [t_knots[i + 1] - t_knots[i] for i in range(n)]  # Step sizes

    alpha = [0] * (n + 1)
    for i in range(1, n):
        alpha[i] = (3 / h[i]) * (values[i + 1] - values[i]) - (3 / h[i - 1]) * (values[i] - values[i - 1])

    l = [1] + [0] * n
    mu = [0] * (n + 1)
    z = [0] * (n + 1)

    for i in range(1, n):
        l[i] = 2 * (t_knots[i + 1] - t_knots[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    a = values[:-1]
    b = [0] * n
    c = [0] * (n + 1)
    d = [0] * n

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (values[j + 1] - values[j]) / h[j] - h[j] * (c[j + 1] + 2 * c[j]) / 3
        d[j] = (c[j + 1] - c[j]) / (3 * h[j])

    return (a, b, c, d, h)

def evaluate_spline(t, t_knots, a, b, c, d):
    """ Evaluates the cubic spline at a given t-value. """
    for i in range(len(t_knots) - 1):
        if t_knots[i] <= t <= t_knots[i + 1]:
            dt = t - t_knots[i]
            return a[i] + b[i] * dt + c[i] * dt**2 + d[i] * dt**3
    raise ValueError("t is out of bounds!")

def render_result(points):
    """ Plots the manually computed cubic parametric spline. """
    t_knots = compute_t_knots(points)

    x_knots = [p[0] for p in points]
    y_knots = [p[1] for p in points]

    # Compute spline coefficients for x and y separately
    spline_x = compute_spline_coeffs(t_knots, x_knots)
    spline_y = compute_spline_coeffs(t_knots, y_knots)

    t_values = np.linspace(t_knots[0], t_knots[-1], 1000)

    x_things = [evaluate_spline(t, t_knots, *spline_x) for t in t_values]
    y_things = [evaluate_spline(t, t_knots, *spline_y) for t in t_values]

    # Plot the parametric spline
    plt.plot(x_things, y_things, label="Cubic Spline Curve")
    plt.scatter(x_knots, y_knots, color="red", label="Control Points")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Corrected Parametric Spline with Proper t-values")
    plt.grid(True)
    plt.show()



