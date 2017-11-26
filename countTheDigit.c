//
//  count_the_digits.c
//  cPractice
//
// Challenge parameters: create a function that takes two integers, n and d, and squares
// all numbers from 0 - n, then counts the number of time the digit d appears in all the numbers
//
// A novice will attempt to do this with arrays, but we should take advantage of other methods
// of manipulating numbers, specifically modulus, and integer division

#include <stdio.h>
int nbDig(int n, int d);

int main(void) {
    
    printf("%d\n", nbDig(12, 4));
    
    return 0;
}
int nbDig(int n, int d) {
    // This is a simple check, since we know that 0 is automatically
    // included in a list of squares from 0 - n, if d == 0, we shold
    // automatically increment the count by one
    int count = (d == 0) ? 1 : 0;
    
    for (int k = 1; k <= n; k++) {
        int kk = k * k;
        printf("Square: %d\n", kk);
        while (kk != 0) {
            // This logic check's the last digit aginst our given digit, d
            // and if they are same we incremen the count
            if (kk % 10 == d){
                printf("kk mod 10 : %d\n", d);
                count++;
            }
            // This is integer division, so numbers < 10 will be == 0 which
            // means that after we've checked the last digit for equality with d
            // we can get rid of it and check the next digit, since intiger division
            // by 10 will truncate the last digit
            kk /= 10;
            printf(" kk /= 10: %d\n", kk);
        }
    }
    
    return count;
}

