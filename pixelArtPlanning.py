# Scenario: you're planning a pixel art mural to paint on your wall
# 					and have decided you need a function called is_devisible
#						to determine whether or not a wall of a given size can fit 
#						a given number of pixels into it.
#
# is_divisible(length, number) : boolean



def is_divisiable(wall_Length, pixel_size):
		return (wall length % pixel_size == 0)

# This solution requires the modulus operator
# remember that for any X % Y, iff X % Y == 0, 
# X is said to be divisible by Y. 
