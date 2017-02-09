'''

@Title: Neo Integration

@Problem Statement:

Bitoholic is an inhabitant of the planet Neo in a galaxy far far away. Their civilization is studies an advanced form of mathematics. 
However, rules of calculus are a bit different there. On his planet, integration and differentiation techniques are called alpha and beta operations
 respectively and are defined as:

alpha: after applying this operation on an polynomial, the degree is incremented by some integral value R and this operation can only be allowed 
if the degree of the polynomial does not exceed an upper limit U. 
[...]

You need to perform a total of N such operations on the polynomial, although the alpha and beta operations can be performed in any order such that 
the degree of the polynomial is maximized after N such operations.
[...]

@URI: https://www.hackerearth.com/problem/algorithm/integration-1/

@Courtesy: hackerearth

'''


t = input()
t += 1
for i in range(1,t):
    N, P, U, R , S = map(int, raw_input().split())
    while N > 0:
    	if (P+R)>U and (P-S)<0:
    		break
    	else:
    		if (P+R)<=U:
    			P += R
    			N -= 1
    		elif (P-S)>=0:
    			P -= S
    			N -= 1
    print "Case #%d: %d" %(i,P)