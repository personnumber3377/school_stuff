import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([-0.83, 0.14, -1.09, 1.09, -0.54, 2.03, 3])
y = np.array([-2.03, -2.06, 0.71, 1.49, 2.06, 2.43, 3])

# Sort x and y for correct spline input (optional if needed)
sorted_indices = np.argsort(x)
x = x[sorted_indices]
y = y[sorted_indices]

# Define the cubic spline
cs = CubicSpline(x, y)

# Generate 100 points between the min and max of x for a smooth curve
# x_fine = np.linspace(np.min(x), np.max(x), 500)
x_fine = np.linspace(-1.3, 4, 1000)
y_fine = cs(x_fine)

plt.figure(figsize=(8, 6))
plt.plot(x_fine, y_fine, label='Cubic Spline', color='blue')
plt.scatter(x, y, color='red', label='Given Points', zorder=5)  # Original points
plt.legend()
plt.title('Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()