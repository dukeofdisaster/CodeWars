# In this challenge we have to define a function that
# takes in an integer and returns a count of the number
# of 1's in the binary representation of this integer
#
# We can assume that we'll probably use the built-in bin()
# function to convert the number to binary, then we'll use
# some slicing since bin() returns a number in the format 0bXXX
# so we'll only want the numbers from [2:] up.

def countBits(num):
    count = 0
    for x in [i for i in bin(num) if i == '1']:
        count += 1
    return count

print(countBits(5))

# in our quest for coding glory, we forgot another built in
# python function. The ever trusty count() which will count how
# many times the given object appears in the string/array the
# method is called on. As such, we get the following one-liner

def countBits1(num):
    return bin(n).count("1")
