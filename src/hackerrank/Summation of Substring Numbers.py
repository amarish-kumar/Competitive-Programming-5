#!/bin/python

'''

@Title: Sam and sub-strings

@Problem Statement:

Samantha and Sam are playing a game. They have 'N' balls in front of them, each ball numbered from 0 to 9, except the first ball 
which is numbered from 1 to 9. Samantha calculates all the sub-strings of the number thus formed, one by one. 

If the sub-string is S, Sam has to throw 'S' candies into an initially empty box. 
At the end of the game, Sam has to find out the total number of candies in the box, T. 
As T can be large, Samantha asks Sam to tell T % (10^9+7) instead.
[...]

@URI: https://www.hackerrank.com/challenges/sam-and-substrings

@Courtesy: hackerrank

'''

## Find a common pattern. For that, break down the final sum recursively. For eg.: if N = 123, then substrings are 1,2,3,12,23,123.
## These substrings can be converted into: 1, 2, 3, 10(1*10)+2, 20(2*10)+3, 100(1*100)+20(2*10)+3. Then group/rearrage these numbers by digits and position wise.
## After grouping: 1 1*10 1*100, 2 2 2*10 2*10, 3 3 3. This means: [1]*1*(1+10+100), [2]*2(1+10), [3]*3*(1) where [1,2,3] are their index values.
## Note: The constraints for N. It's too big!

s = raw_input().strip()
l = len(s)

MOD = 10**9 + 7
total = 0

c = 1
for i in xrange(l-1, -1, -1):
	total += (int(s[i])*(i+1)*c)%MOD
	total %= MOD
	c = c*10 + 1
	c %= MOD
	

print total%MOD