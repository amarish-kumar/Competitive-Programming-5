t = int(input())
while t:
    t -= 1
    n = int(input())
    if n>1:
        sq = int((n**.5) + 1)
        divisor_sum = 1
        for i in xrange(2,sq):
            if ((n%i) == 0):
                divisor_sum += i
                if (n/i) != i:
                    divisor_sum += (n/i)
        print divisor_sum
    else:
        print 0