
import numpy as np # Import numpy numerical math library
import random
import copy

def inner_product(x): # The inner product given in the exercise.
    return 1/3*(x[0]**2)+x[0]*x[1]+(x[1]**2)

def gen_pseudorandom(): # This gives a pseudorandom thing
    return np.random.uniform(0, 1)
    # return np.random.uniform(-1, 1)

MAX_ERROR_THING = 5.0

def modify_matrix(matrix, average_error, perturbation_scale=0.1, num_elements=None):
    if average_error >= MAX_ERROR_THING:
        average_error = MAX_ERROR_THING

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
    # a = 0.0
    # b = 0.0
    # d = 0.0

    a = gen_pseudorandom()
    b = gen_pseudorandom()
    d = gen_pseudorandom()

    # Construct the symmetric matrix
    A = np.array([[a, b],
                  [b, d]])
    return A # Return it

CHECK_COUNT = 10000

MAX_VEC_ELEM = 3

test_vects = [np.random.uniform(-MAX_VEC_ELEM, MAX_VEC_ELEM, size=2) for _ in range(CHECK_COUNT)]

def s():
    # Try to solve.
    
    A = gen_rand_symmetric_2x2_int_matrix() # Generate initial matrix

    best_error = 10000000000000 # Very big number to start with
    av_error = 10
    while True: # Do until we find a suitable matrix (which we assume exists)
        modified = modify_matrix(A, av_error) # Modify a bit
        # Now check if the condition is for all vectors
        error = 0.0 # Initialize error here...
        for x in test_vects:
            # x = np.random.uniform(-1, 1, size=2)
            prod_result = inner_product(x) # Right Hand Side
            # Now check if it matches the thing...
            other_result = x.T @ modified @ x # Left Hand Side
            error += abs(prod_result - other_result)
            # if prod_result != other_result: # Differs?
            #     break # Then break here
        '''
        else:
            # We did NOT break, therefore we found the thing
            print("Suitable matrix: "+str(modified))
            break
        '''
        # Did break, therefore was not valid matrix. Update best error and try again...
        av_error = error / CHECK_COUNT
        print("Average error: "+str(av_error))
        print(modified)
        if av_error <= best_error: # Best until now???
            best_error = av_error
            A = modified # Assign the modified one to the new one and use this matrix in further tries...
        if av_error <= 1e-7:
            print(modified)
            exit(0)
    return



if __name__=="__main__":
    s()
    exit(0)


