import sympy as sp
from scipy.integrate import quad

def compute_path_length_parametric(x_expr, y_expr, t_range):
    """
    Computes the path length of a curve defined parametrically by x(t) and y(t).

    Parameters:
        x_expr (str): Parametric expression for x(t) as a string.
        y_expr (str): Parametric expression for y(t) as a string.
        t_range (tuple): The range of the parameter t as (t_start, t_end).

    Returns:
        float: The computed path length of the curve.
    """
    # Define the parameter t as a symbolic variable
    t = sp.symbols('t')

    # Parse the parametric expressions for x(t) and y(t)
    x_t = sp.sympify(x_expr)
    y_t = sp.sympify(y_expr)

    # Compute the derivatives dx/dt and dy/dt
    dx_dt = sp.diff(x_t, t)
    dy_dt = sp.diff(y_t, t)

    # Define the arc length integrand sqrt((dx/dt)^2 + (dy/dt)^2)
    arc_length_integrand = sp.sqrt(dx_dt**2 + dy_dt**2)

    # Convert the integrand to a numerical function for integration
    integrand_func = sp.lambdify(t, arc_length_integrand, modules='numpy')

    # Perform numerical integration using scipy's quad
    t_start, t_end = t_range
    path_length, _ = quad(integrand_func, t_start, t_end)

    return path_length


def compute_path_length_polar(r_expr, theta_range):
    """
    Computes the path length of a curve defined in polar coordinates r(theta).

    Parameters:
        r_expr (str): Polar expression for r(theta) as a string.
        theta_range (tuple): The range of the parameter theta as (theta_start, theta_end).

    Returns:
        float: The computed path length of the polar curve.
    """
    # Define the parameter theta as a symbolic variable
    theta = sp.symbols('theta')

    # Parse the polar expression for r(theta)
    r_theta = sp.sympify(r_expr)

    # Compute the derivative dr/dtheta
    dr_dtheta = sp.diff(r_theta, theta)

    # Define the arc length integrand sqrt(r^2 + (dr/dtheta)^2)
    arc_length_integrand = sp.sqrt(r_theta**2 + dr_dtheta**2)

    # Convert the integrand to a numerical function for integration
    integrand_func = sp.lambdify(theta, arc_length_integrand, modules='numpy')

    # Perform numerical integration using scipy's quad
    theta_start, theta_end = theta_range
    path_length, _ = quad(integrand_func, theta_start, theta_end)

    return path_length




def compute_tangent_vector_polar(r_expr, theta_value):
    """
    Computes the tangent vector of a curve defined in polar coordinates r(theta).

    Parameters:
        r_expr (str): Polar expression for r(theta) as a string.
        theta_value (float): The specific value of theta at which to compute the tangent vector.

    Returns:
        tuple: The tangent vector (dx/dtheta, dy/dtheta) at the given theta.
    """
    # Define the parameter theta as a symbolic variable
    theta = sp.symbols('theta')

    # Parse the polar expression for r(theta)
    r_theta = sp.sympify(r_expr)

    # Compute the derivative dr/dtheta
    dr_dtheta = sp.diff(r_theta, theta)

    # Compute dx/dtheta and dy/dtheta
    # dx_dtheta = sp.cos(theta) * r_theta - sp.sin(theta) * dr_dtheta
    dx_dtheta = -sp.sin(theta) * r_theta + sp.cos(theta) * dr_dtheta
    dy_dtheta = sp.sin(theta) * r_theta + sp.cos(theta) * dr_dtheta

    # Evaluate the tangent vector components at the specific theta value
    dx_dtheta_val = dx_dtheta.evalf(subs={theta: theta_value})
    dy_dtheta_val = dy_dtheta.evalf(subs={theta: theta_value})

    return (dx_dtheta_val, dy_dtheta_val)

#import math
from math import sqrt

def our_answer():
    return (-sqrt(2)/2*(1+sqrt(2)), -(sqrt(2)/2)**2+(1+sqrt(2)/2)*(sqrt(2)/2))



# Example usage
if __name__ == "__main__":
    # Input the parametric equations and range for t
    #x_expr = "cos(t)"
    #y_expr = "sin(t)"
    
    #x_expr = str(input("Please give the x parameter as a function of t: "))
    #y_expr = str(input("Please give the x parameter as a function of t: "))

    r_expr = str(input("Please give the r parameter: "))
    theta_range = (0, 2 * sp.pi)  # Full circle

    # Compute and print the path length
    length = compute_path_length_polar(r_expr, theta_range)
    # Now compute the tangent vector thing...
    theta_value = sp.pi/4
    tangent_vector = compute_tangent_vector_polar(r_expr, theta_value)
    print(f"Path length of the curve: {length:.5f}")
    print("Tangent vector: "+str(tangent_vector))
    print("Our answer: "+str(our_answer()))

