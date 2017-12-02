# In this challenge we had to define a function that given a range from
# a to b+1, returns an array containing all numbers if the some of
# the powers of their digits is equal to the number. For eample
# for the number 12, the first (leftmost) digit is 1 and 1^1 =1, 2 is
# the second digit, and 2^2 = 4, 1+4 = 5, so 12 would not be in the list.
# in fact, the only number less than 100 that has this property is 89
# because 8^1 =  8 and 9^2 = 81, 8+81 = 89.
#
# Recall that in python, to raise a number n to an exponent e, the format
# is n**e.
#
# Novice solution is below
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    arr = []
    for x in range(a, b+1):
        length = len(str(x))
        sum = 0
        pow = 1
        index = 0
        while length > 0:
            sum += int(str(x)[index])**pow
            pow += 1
            index += 1
            length -= 1
        if x == sum:
            arr.append(x)
    return arr

# The expert solution below makes use of a helper function and two
# built-in python functions for completing this kind of task, namely
# the enumerate() and filter() functions.

# Below is an explanation of the two:
#
# enumerate():
# Return an enumerate object. sequence must be a sequence, an iterator,
# or some other object which supports iteration. The next() method of the
# iterator returned by enumerate() returns a tuple containing a count
# (from start which defaults to 0) and the values obtained from iterating
# over sequence:
#
# filter(function, iterable):
# Construct a list from those elements of iterable for which function
# returns true. iterable may be either a sequence, a container which
# supports iteration, or an iterator. If iterable is a string or a tuple,
# the result also has that type; otherwise it is always a list. If function
# is None, the identity function is assumed, that is, all elements of
# iterable that are false are removed.
#
# example of enumerate()
# string = "12345"
# for x in enumerate(string):
#     print(x)
#
# (0, '1')
# (1, '2')
# (2, '3')
# (3, '4')
# (4, '5')
def filter_func(a):
    # as seen above, enumerate makes the object passed to it iterable
    # and paired with an index, thus when i,d in enumerate(str(a)) is
    # referenceed, i, d simpley refer to each pair of objects, starting
    # at index 0, which is why we have to convert d to an int and
    # use (i+1) as the power
    return sum(int(d) ** (i+1) for i, d in enumerate(str(a))) == a

def sum_dig_pow1(a, b):
    # filter calls fiter_func on all of the objects in the given range
    # and returns an array of those items for which the filter_func
    # property returns true
    return filter(filter_func, range(a, b+1))
