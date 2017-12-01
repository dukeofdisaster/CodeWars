// -------------------------------------------------------------------
// This challenge required us to create a function that
// determines whether or not a given integer is even or even_or_odd
// as we could guess, this will involve modulo, since
// for any number x, if x % 2 = 0, then x is even.
//
// In this challenge, % is the novice solution. In C, we make
// use of the bitwise operation & to check if the number is odd
// consider the example below for the binary represenation of 6 and 1
//
// 110   Performing & on this operation only caries over the bits from
// 001   the top that are the same. thus our result is 000.
// ---
// 000   Recall that in C, True/False can be represented as 1/0
//
// Thus, comparing the number passed to 1, produces our desired effect.
// The novice solution would be as such
//
// const char * even_or_odd(int number){
//      unsigned int n = number;
//      if (n % 2 == 1)
//          return "Odd";
//      return "Even"
// --------------------------------------------------------------------
#include <stdio.h>

const char* even_or_odd(int n);
const char* even_or_odd(int n){
  return (n & 1) ? ("Odd"):("Even")
}


int main(void){
  char x = even_or_odd(5);
  printf("%s", x);
}
