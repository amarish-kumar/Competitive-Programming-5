'''

@Title: Skyler & Marie's Shoplifting

@Problem Statement:

As we all know, Skyler & Marie are the most annoying creatures to ever exist in Albuquerque. They went shopping together one day. 
But, Marie is a shoplifter & steals items from stores. 

[...]

She has a two-sided long ribbon in which there is a binary string K. On the other side, there is a decimal prime number M. 
In order to shoplift, she needs to find out if M divides the decimal equivalent of K.

[...]

@URI: https://www.hackerearth.com/problem/algorithm/prime-divisibility/description/

@Courtesy: hackerearth

'''

## Prime divisibility, Modular exponentiation based problem. Approach is do the summation of all the residues.


t=int(input())
while t:
    t-=1
    s = raw_input()
    s = s[::-1]
    l = len(s)
    pr = int(input())
    m = 0
    for i in xrange(l):
        if s[i] == '1':
            m = m + pow(2,i,pr)
    print 'NO' if m%pr else 'YES'