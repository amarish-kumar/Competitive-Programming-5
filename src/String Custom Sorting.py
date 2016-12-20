'''

@Title: ginortS

@Problem Statement:

You are given a string S.
S contains alphanumeric characters only.

Your task is to sort the string S in the following manner:

    All sorted lowercase letters are ahead of uppercase letters.
    All sorted uppercase letters are ahead of digits.
    All sorted odd digits are ahead of sorted even digits.

[...]

@URI: https://www.hackerrank.com/challenges/ginorts/

@Courtesy: hackerrank

'''

## Simply write a custom sort criteria and use it as a key.


from __future__ import print_function

def sort_param(x):
    y = ord(x)
#    if y > 96 and y<123:
    if 96 < y < 123:
        return y-96
    elif 64 < y <91:
        return 50 + (y-64)
    else:
    	if y%2 == 1:
        	return 100 + (y-47)
        else:
        	return 150 + (y-47)


s = raw_input()
b = sorted(s, key = sort_param )

print(*b, sep='')


# Lamba function solution:
print(*(sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')