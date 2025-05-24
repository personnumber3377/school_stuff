
from sympy import *





def partb():
    V = Matrix([[1,1],[2,1],[1,2],[0,1]])
    W = Matrix([[2,1],[1,1],[1,1],[0,1]])

    # Concatenate to form a full-rank basis for R^4
    M = V.row_join(W)

    # Inverse of M
    M_inv = M.inv()

    # Take first 2 rows of M_inv to extract V-components
    P = V @ M_inv[:2, :]

    print("P: "+str(P))
    print("As latex: "+latex(P))

    return P


def s():
	# Do the stuff here maybe????
	P = partb()
	V = Matrix([[1,1],[2,1],[1,2],[0,1]])
	W = Matrix([[2,1],[1,1],[1,1],[0,1]])
	I = Matrix([[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]])

	Q = V @ (V.transpose() @ V).inv() @ V.transpose()
	print("Q: "+str(Q))
	print("As latex: "+str(latex(Q)))

	print("Checking...")

	assert Q @ Q == Q # Should be true...
	x = Q.transpose() @ (I - Q)
	assert x == zeros(4,4) # Should be the zero matrix...

	assert P @ V == V
	# print(P @ W)
	assert P @ W == zeros(4,2)


	return

if __name__=="__main__":
	s()
	exit(0)
