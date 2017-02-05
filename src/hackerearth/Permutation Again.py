'''

@Title: Permutation Again

@Problem Statement:

Given an integer N. Find out the PermutationSum where PermutationSum for integer N is defined as: 
the maximum sum of difference of adjacent elements in all arrangement of numbers from 1 to N.

NOTE: Difference between two elements A and B will be considered as abs(A-B) or |A-B| which always be a positive number.
[...]

@URI: https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/practice-problems/algorithm/permutation-again/

@Courtesy: hackerearth

'''

'''
N = 3

5 1 4 2 3

sum = 4 + 3 + 2 + 1 = 10

5*4/2

N*(N-1)/2 ??

But, the correct combination is:

3 1 5 2 4

sum = 2 + 4 + 3 + 2 = 11

(N*N)/2 - 1

'''

t = int(input())
while t:
    t -= 1
    n = int(input())
    if n == 1:
        print 1
    else:
        print ((n*n)/2)-1