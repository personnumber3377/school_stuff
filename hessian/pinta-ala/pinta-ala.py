#!/bin/sh

# This file implements the calculating of a hessian with pythons symbolic calculation library sympy.

import sympy
import numpy as np



def test_basic():
	x, y, z = sympy.Symbol("x"), sympy.Symbol("y"), sympy.Symbol("z")
	variables = [x,y,z]
	f = 2*x*z+2*z*y+x*y # This should be the function thing...
	f_new = f.subs(x, 4/(y*z))
	H = sympy.hessian(f_new, (y,z))
	print("Here is the hessian: ")
	print(H)
	return

def run_tests(): # This function runs the tests of the program.
	test_basic()
	return


if __name__=="__main__":

	# Example usage:

	run_tests()
	exit(0)

