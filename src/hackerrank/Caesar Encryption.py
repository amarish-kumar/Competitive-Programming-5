#!/bin/python

'''

@Title: Encryption

@Problem Statement:

An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text.

The encoded message is obtained by displaying the characters in a column, inserting a space, 
and then displaying the next column and inserting a space, and so on. 
[...]

@URI: https://www.hackerrank.com/challenges/encryption/

@Courtesy: hackerrank

'''

## Simple encryption problem. Just follow the rules step-by-step.


from math import ceil as ceil

s = raw_input().split()
s=''.join(s)
n=len(s)
x=n**.5

if (int(x)**2) == n:
	c=int(x)
else:
	c=int(ceil(x))
	
for i in range(c):
	d=''
	j=i
	while j<n:
		d=d+s[j]
		j=j+c
	print d,