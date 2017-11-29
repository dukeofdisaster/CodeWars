from math import sqrt

# We'll recall that anytime we're working with number methods we
# should utilize Python's large math library. In this case, the only one that
# comes to mind is the sqrt() function

def findNextSquare(sq):
    # First we check the square root of the given number against mod 1
    # since this will either return 0, if it's an integer and otherwise
    # return a decimal.
    if((sqrt(sq) % 1) == 0):
        return ((sqrt(sq)+1)*(sqrt(sq)+1))
    # Here we keep the code clean by avoiding an unnecessary else statemnt
    return -1

print(findNextSquare(4))
