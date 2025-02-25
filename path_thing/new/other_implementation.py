
from sympy import *

'''

def find_with_constraints(f, variables, constraints):
    # Define Lagrange multipliers
    constr_variables = [Symbol("l" + str(i)) for i in range(len(constraints))]
    assert not set(f.free_symbols) & set(constr_variables)  # Ensure no variable conflicts

    # Construct the Lagrangian function
    constraint_stuff = sum(l * c for l, c in zip(constr_variables, constraints))
    L = f - constraint_stuff  # Corrected sign
    
    print("Lagrange function:", L)
    
    # Compute derivatives
    derivatives_variables = [diff(L, v) for v in variables]  # Partial derivatives w.r.t variables
    derivatives_lambdas = [diff(L, l) for l in constr_variables]  # Partial derivatives w.r.t lambdas
    derivatives_all = derivatives_variables + derivatives_lambdas
    all_vars = variables + constr_variables
    
    print("Derivatives:", derivatives_all)
    
    # Solve the system of equations
    sol = solve(derivatives_all, all_vars)
    
    # Ensure sol is a list of solutions
    if isinstance(sol, dict):
        sol = [sol]  # Convert dictionary to list of one solution
    elif not isinstance(sol, list):
        sol = [sol]  # Ensure sol is a list
    
    print("Solutions:", sol)
    
    # Evaluate function values at critical points
    min_thing, max_thing = None, None
    min_res, max_res = None, None
    
    for s in sol:
        result = f
        for var in variables:
            result = result.subs(var, s[var])  # Substitute variable values
        
        if min_res is None or result < min_res:
            min_res, min_thing = result, s
        
        if max_res is None or result > max_res:
            max_res, max_thing = result, s
    
    print("Max critical point:", max_thing)
    print("Min critical point:", min_thing)
    print("Max value obtained:", max_res)
    print("Min value obtained:", min_res)
    
    # Hessian matrix check for local min/max classification
    hessian = Matrix([[diff(diff(f, v1), v2) for v2 in variables] for v1 in variables])
    eigenvalues = hessian.eigenvals()
    
    print("Hessian Eigenvalues:", eigenvalues)
    if all(ev > 0 for ev in eigenvalues):
        print("Local minimum confirmed")
    elif all(ev < 0 for ev in eigenvalues):
        print("Local maximum confirmed")
    else:
        print("Saddle point detected")

    # Check function value at boundary
    print("Checking boundary values:")
    for var in variables:
        boundary_value = solve(constraints[0], var)  # Solve constraint for one variable
        if boundary_value:
            for val in boundary_value:
                boundary_f = f.subs(var, val)
                print(f"Boundary check {var} = {val}: f = {boundary_f}")

Koska vihreällä valolla on lyhyempi aallonpituus, samanvaiheisten aaltojen kohtaamiseen vaadittava kulkumatkaero pienenee. Tämä tarkoittaa, että vierekkäiset interferenssimaksimit ovat lähempänä toisiaan.
sqrt(-4*cos(x)**3-cos(x)**2+4*cos(x)+2)

x**2 + 2*y**2 + 3*z**2 - 2*x*y - 3*y*z = 3


z

'''


def find_with_constraints(f, variables, constraints):
    # Define Lagrange multipliers
    constr_variables = [Symbol(f"l{i}") for i in range(len(constraints))] 

    # Construct the Lagrangian function
    L = f + sum(l * g for l, g in zip(constr_variables, constraints))
    
    # Compute the derivatives
    derivatives = [diff(L, v) for v in variables] + [diff(L, l) for l in constr_variables]

    # Solve the system of equations
    all_vars = variables + constr_variables
    sol = solve(derivatives, all_vars, dict=True)  # Solve as dictionary for clarity

    if not sol:
        print("No solution found.")
        return

    # Find max and min values
    max_val = -oo
    min_val = oo
    max_point = None
    min_point = None

    for s in sol:
        f_val = f.subs(s)

        # Update min/max tracking
        if f_val > max_val:
            max_val = f_val
            max_point = s
        if f_val < min_val:
            min_val = f_val
            min_point = s

    # Output results
    print("Max critical point:", max_point)
    print("Min critical point:", min_point)
    print("Max value obtained:", max_val)
    print("Min value obtained:", min_val)