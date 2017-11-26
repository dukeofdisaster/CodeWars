# The challenge is to define a function that takes the sum of the two
# smallest numbers in an array of integers and returns said sum. 
# We are not allowed to modify the original array

def sumTwoSmallest(numbers):
    copiedArray = numbers
    lowest = min(copiedArray)
    copiedArray.remove(lowest)
    nextLowest = min(copiedArray)
    return lowest+nextLowest

# Again, we commit the sin of reinventing the wheel. A novice
# does something like the above, but clever ol' python has some
# built in functions that would have helped us, coupled with slicing

def sumTwoSmallest(numbers):
    # the sorted function takes in the array and the slicing at the end tells us we want
    # the portion of the array up to but not including index 2, so 0,1 which in a sorted
    # array will always be the two lowest numbers
    return sum(sorted(numbers)[:2])
