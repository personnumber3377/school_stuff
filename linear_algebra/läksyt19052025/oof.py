
import numpy as np # Import numpy numerical math library
import random
import copy

def inner_product(x): # The inner product given in the exercise.
    return 1/3*(x[0]**2)+x[0]*x[1]+(x[1]**2)

def gen_pseudorandom(): # This gives a pseudorandom thing
    '''
    if random.random() <= 0.3:
        return np.random.uniform(-10, 10)
    else:
        return 1/(3**5)*np.random.randint(-100, 111)
    '''

    return np.random.uniform(-1, 1)



'''

def modify_matrix(matrix, average_error, perturbation_scale=0.000000001, num_elements=None): # Thanks ChatGPT!!!
    """
    Randomly adds or subtracts small values from elements in the matrix.

    Parameters:
    - matrix (np.ndarray): The input matrix to modify.
    - perturbation_scale (float): The maximum magnitude of change per element.
    - num_elements (int or None): Number of elements to modify. If None, modify all.

    Returns:
    - np.ndarray: A new matrix with modified elements.
    """

    if average_error >= 10.0: # Max cap
        average_error = 10.0

    modified = matrix.copy()
    rows, cols = modified.shape

    if num_elements is None:
        num_elements = rows * cols  # Modify all

    indices = np.random.choice(rows * cols, size=num_elements, replace=False)
    
    for idx in indices:
        i, j = divmod(idx, cols)
        change = np.random.uniform(-perturbation_scale, perturbation_scale) * average_error # Take big steps when error is large and small steps when error is small
        modified[i, j] += change

    return modified

'''


def modify_matrix(matrix, average_error, perturbation_scale=1.0, num_elements=None):
    """
    Randomly modifies elements of a symmetric matrix while preserving symmetry.

    Parameters:
    - matrix (np.ndarray): The symmetric matrix to modify.
    - average_error (float): Used to scale step size.
    - perturbation_scale (float): Maximum magnitude of change per element.
    - num_elements (int or None): Number of elements to modify. If None, modify all (a, b, d).

    Returns:
    - np.ndarray: New symmetric matrix.
    """
    if average_error >= 10.0:
        average_error = 10.0

    modified = copy.deepcopy(matrix) # matrix.copy()
    
    # Select which of the 3 independent elements to modify
    indices = ['a', 'b', 'd']
    if num_elements is not None:
        indices = random.sample(indices, k=num_elements)

    for key in indices:
        delta = np.random.uniform(-perturbation_scale, perturbation_scale) * average_error
        if key == 'a':
            modified[0, 0] += delta
        elif key == 'd':
            modified[1, 1] += delta
        elif key == 'b':
            modified[0, 1] += delta
            modified[1, 0] += delta  # Mirror to preserve symmetry

    return modified




def gen_rand_symmetric_2x2_int_matrix():
    # Generates a random symmetric integer 2x2 matrix

    # Generate random integers for the matrix

    '''
    a = np.random.uniform(-10, 10) # np.random.randint(-10, 11)  # Diagonal element A[0,0]
    b = np.random.uniform(-10, 10) # np.random.randint(-10, 11)  # Off-diagonal element A[0,1] and A[1,0]
    d = np.random.uniform(-10, 10) # np.random.randint(-10, 11)  # Diagonal element A[1,1]
    '''

    # a = gen_pseudorandom()
    # b = gen_pseudorandom()
    # d = gen_pseudorandom()

    a = 0.0
    b = 0.0
    d = 0.0

    # Construct the symmetric matrix
    A = np.array([[a, b],
                  [b, d]])
    return A # Return it

CHECK_COUNT = 10000

# This is the set of vectors we are checking against. We can not generate this on each iteration, because otherwise we create a "moving target" for the optimizer to optimize.

# test_vects = [np.random.uniform(-1, 1, size=2) for _ in range(CHECK_COUNT)]

test_vects = [np.random.uniform(-10, 10, size=2) for _ in range(CHECK_COUNT)]

def s():
    # Try to solve.
    
    A = gen_rand_symmetric_2x2_int_matrix() # Generate initial matrix

    best_error = 10000000000000 # Very big number to start with
    av_error = 10
    while True: # Do until we find a suitable matrix (which we assume exists)
        modified = modify_matrix(A, av_error) # Modify a bit

        # print("Now checking: "+str(modified))
        # Now check if the condition is for all vectors
        error = 0.0 # Initialize error here...
        for x in test_vects:
            # x = np.random.uniform(-1, 1, size=2)
            prod_result = inner_product(x) # Right Hand Side
            # Now check if it matches the thing...
            other_result = x.T @ modified @ x # Left Hand Side
            # print("prod_result: "+str(prod_result))
            # print("other_result: "+str(other_result))
            error += abs(prod_result - other_result)
            if prod_result != other_result: # Differs?
                break # Then break here
        else:
            # We did NOT break, therefore we found the thing
            print("Suitable matrix: "+str(modified))
            break
        # Did break, therefore was not valid matrix. Update best error and try again...
        av_error = error / CHECK_COUNT
        print("Average error: "+str(av_error))
        # if av_error <= 1e-4:
        #     print(modified)
        print(modified)
        if av_error <= best_error: # Best until now???
            best_error = av_error
            A = modified # Assign the modified one to the new one and use this matrix in further tries...

    return



if __name__=="__main__":
    s()
    exit(0)


