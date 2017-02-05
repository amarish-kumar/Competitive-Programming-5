#!/bin/python

#!/bin/python

'''

@Title: Cut the sticks

@Problem Statement:

You are given N sticks, where the length of each stick is a positive integer. 

A cut operation is performed on the sticks such that all of them are reduced by the length of the smallest stick.

The above step is repeated until no sticks are left.

Given the length of N sticks, print the number of sticks that are left before each subsequent cut operations.
[...]

@URI: https://www.hackerrank.com/challenges/cut-the-sticks/

@Courtesy: hackerrank

'''

## Group the sticks by size, and its corresponding count. So, for stick lengths: [5 4 4 2 2 8], the groupings would result in [(2, 2), (4, 2), (5, 1), (8, 1)]. 
## Then pop each item in each subsequent steps.


import operator
from collections import Counter

n=input()
arr = map(int, raw_input().strip().split())

ct = Counter(arr).items()

ct = sorted(ct, key = operator.itemgetter(0))
# print ct

while n:
    print n
    x = ct.pop(0)
    n = n - x[1]