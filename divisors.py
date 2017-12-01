# divisors.py
#
# for this challenge we had to find the divisors
# of a given integer otherwise return a message saying that otherwise
# return a message saying that the number was prime.
#
# We recall that modulo (%) is frequently used in such
# operations so that will be part of our solution.
#

def divisors(integer):
    # since we know 1 will be excluded we can
    # use 2 as a starting point
    copy = 2

    # we'll need an array to store our results
    divisors = []

    # I initially wanted to start with a decrementing loop
    # but went with an incrementing loop because appending
    # the array with a decrementing loop resulted in
    # the divisors listed from left to right, greatest to least
    # which failed the tests
    while(copy < integer):
        if ((integer % copy) == 0):
            divisors.append(copy)
        copy += 1
    if len(divisors) > 0:
        return divisors
    else:
        return str(integer)+" is prime"

# Our original solution was 10 lines, but the expert solution only
# requires 4 lines. Recall that we should be wise to use python's
# clever logic operators (for in if), which can allow us to be loose
# with our logic statements yet highly effective

def divisorsExpert(num):
    # Here we make use of the range function which, when supplied 2
    # arguments will return an array from (x, y) inclusive/exclusive
    # so the array l is equal to variable a in range 2, IF num % a == 0
    l = [a for a in range(2, num) if num % a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
