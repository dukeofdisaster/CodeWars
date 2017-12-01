# For this challenge we had to take two integers
# then return their sum in string format as a binary
#
# As always, we want to reuse built-in functions where
# possible. Python has a bin() function so this challenge
# is very easy. bin() returns a string but prepends it with
# a format specifier 0b, which is standard. For hex it 
# would be 0x. That's no problem, as we can simply use
# slicing to only return the parts we care about
#
# Recall that slicing retunrs a range from a string or 
# an array, with [inclusive:exclusive], so if we only
# want everything after the first two values of 0-indexed
# array/string we use [2:] and we leave the second value
# blank because we want all of it.
#
# our resulting function is a simple two liner

def decimalSumToBinary(a, b):
		return bin(a+b)[2:]
 
