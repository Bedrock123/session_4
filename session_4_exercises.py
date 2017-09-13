"""
Zachary Bedrosian
Session 4 Exercises
9.14.2017
"""

"""
Define a function quadratic(a, b, c) to solve a quadratic equation:
"""

import cmath

# Define Function
def quadratic(a,b,c):
    """
    This function takes in three parameters and uses them to find x in the 
    quadratic equation.
    """
    d = (b**2) - (4*a*c)
    # find two solutions
    solution_one = (-b-cmath.sqrt(d))/(2*a)
    solution_two = (-b+cmath.sqrt(d))/(2*a)

    print(solution_one)
    print(solution_two)

# Run Function
quadratic(6,3,2)

