# Requirements: Instead of a Fibonacci sequence, we'll make a TRI-bonacci sequence
#
# Your function will be given a signature array of 3 numbers and a positive integer n
# it must return an array of size n, where the n-th number is the sum of the previous 3
# 
# For n < 3, we have our base cases, so if n == 1, we return the first item in the signature
# For n == 2, we return the first two items in the signature
# and for n == 3, we simply return the signature
# for n == 0, we return an empty array, [] 

def tribonacci(signature, n):
    if n == 0:
        return []
    if n == 1:
        return [signature[0]]
    if n == 2:
        signature.remove(signature[2])
        return signature
    sigcopy = signature
    indexCount = 0
    while n > 3:
        sigcopy.append((sigcopy[indexCount]+sigcopy[indexCount+1]+sigcopy[indexCount+2]))
        indexCount += 1 
        print ("indexCount: ",indexCount)
        n = n-1
        print(sigcopy)
    return sigcopy

## Best Solution ##
#
# A better solution to this problem takes advantage of python's slicing syntax
# which is very effective at accessing specific parts of an array of numbers
#
# def tribonacci(signature, n):
#     result = signature[:n]
#     for i in range(n - 3):
#         res.append(sum(res[-3:]))
#     return res
