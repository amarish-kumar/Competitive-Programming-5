'''

@Title: Pairs

@Problem Statement:

Given integers, count the number of pairs of integers whose difference is K. 
All the numbers are unique.
[...]

@URI: https://www.hackerrank.com/challenges/pairs

@Courtesy: hackerrank

'''

## We need to find the number of pairs of integers from a set of integers, whose difference is exactly equal to a given value of K.

s = raw_input().split()

n,d = int(s[0]),int(s[1])

arr = map(int, raw_input().split())

arr = sorted(arr)
brr = []

for i in xrange(n-1):
	brr.append(arr[i]+d)

print len(set(arr)&set(brr))