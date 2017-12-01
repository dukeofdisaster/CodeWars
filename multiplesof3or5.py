# for this challenge we had to define a function
# that takes an integer as an argument and returns
# the sum of any numbers less than it that are multiples
# of 3 or of 5.
#
# The natural novice tendency is to use a counter variable
# and increment it like below:
#
def solution1(num):
    count = 0
    for i in range(num):
        if ((i % 3 == 0) or (i % 5) == 0):
            count += 1
    return count

# the expert solution reduces this to a one-liner that makes
# use of python's built in sum() function as well as range()
# and the liberal array logic

def solution2(num):
    # so we use the funky logic to create an array from the numbers
    # in range 0-num if any of those numbers are divisible by 3 or 5
    reutrn sum([i for i in range(num) if i % 3 == 0 or i % 5 == 0])
