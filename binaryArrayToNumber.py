# binaryArrayToNumber.py
#
# For this challenge we had define a function that would take
# in an array of 0's and 1's, or a binary array, and then
# based on that array, return an integer that was a 
# decimal representation of the binary array.

def binaryArrayToNumber(arr):
		size = len(arr) - 1
		power = 0
		number = 0
		while (size >= 0):
				if (arr[size] == 1):
						number += 2**power
				power += 1
				size -= 1
		return number

# Should return 5
print(binaryArrayToNumber([1,0,1]))

# An even simpler solution utilizes several built in python functions.
# Specifically, int(), join(), and map()
# int() converts a string of digit characters to an integer, however
#	when given two arguments, it converts the string to a decimal
# representation based on the base supplied, so if we did something
# like int('101', 2) the int function would return 5. 
#
# join() is a standard command for adding things to strings
#
# map() is a function that applies a seperate function to each object
# in an iterable. Say if we wanted to convert an array of integers
# to string objects, we could call map(str, arrayName). that's how
#
# The solution below is the most efficient, requiring only two lines of code
#

def binaryArrayToDecimal(arr):
		# This can seem confusing but if we start at the inner most function
		# and work our way out it makes more sense. So we first apply the
		# str function to each object in the array via map(). The map function
		# is then being passed to the join() function, which appends the 
		# the converted data to an empty string. The resulting string is then
		# passed as an argument along with the integer literal 2, saying we
		# want to conver the string to a decimal using the base 2
		return int("".join(map(str, arr)), 2)
