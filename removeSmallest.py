def remove_smallest(numbers):

    # First we check if numbers is empty so we can return an empty list
    # otherwise, if we try to access numbers[0] before this it would throw
    # an index out of bounds error so we verify that numbers "exists" first
    if not numbers:
        return []

    # Having verified that numbers exists, we set the lowest as the first index
    lowest = numbers[0]

    # then we for each number i in the array numbers we compare it against
    # our lowest, if it's less than lowest, we have a new lowest. Note that
    # this verificatin step also fulfills the requirement that if we have 
    # multiple "lowest" values, the one with the lower index gets returned
    # because we start at the lowest index as the lowest number and only
    # change that number when we find a number lower, hence the lower index
    # numbers are always favored by default
    for i in numbers:
        if i < lowest:
            lowest = i
    numbers.remove(lowest)
    return numbers
    #raise NotImplementedError("TODO: remove_smallest")

###
# Best Solution
#
# While the above works well and pasts the tests, it isn't the best solution
# because we commit the programming sin of "reinventing the wheel" or 
# inefficiency through algorithmic ignorance. Python is very robust
# and has such functions as min() for finding minimum numbers in arrays. 
#
# The best solution is a such:
# 
# def removeSmallest(numbers):
#     if numbers:
#          numbers.remove(min(numbers))
#     return numbers 
