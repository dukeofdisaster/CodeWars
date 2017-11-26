// Solution to the challenge: create a function to find the average of
// an array of values without using for loops. This requires two functions
// So it's technically not a one function solution (misleading) but
// requires a helper function that performs a sum

#include <stdio.h>
int sum(const int *values, unsigned int count)
{
	// this functions as the base case of our recursive function
  if(count == 0) return 0;
	//Here we make a recursive call using values+1 as the array in question
	// which is the first element+ offset, or the next element, and we
	// also shorten the count by one because we're referencing a smaller array 
  else 
		return values[0] + sum(values+1, count-1);
}

int average(const int *values, unsigned int count){
  double avg = sum(values, count) / (double) count;
  return avg + 0.5;
}
