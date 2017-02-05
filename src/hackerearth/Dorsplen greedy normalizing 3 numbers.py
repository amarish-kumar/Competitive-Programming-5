'''

@Title: Exploring ruins

@Problem Statement:

Edward is playing a simplified version of game called "Dorsplen". This game is played with gems of three different colors: red, green and blue. 
Initially player has no gem and there are infinitely many gems of each color on the table.

On each turn a player can either acquire gems or buy an artifact. Artifact can be bought using gems. 
On acquiring gems player can get three gems of distinct colors or two gems of the same color from the table.

Edward is planning to buy an artifact, it costs r red gems, g green gems and b blue gems. 
Compute, what is the minimum number of turns Edward has to make to earn at least r red gems, g green gems and b blue gems, 
so that he will be able to buy the artifact.
[...]

@URI: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/dorsplen/

@Courtesy: hackerearth

'''

## Greedy approach. Finding the minimum among the three possible ways of acquiring all the 3 types of gems.


def meth2(n):
    if(n%2):
        return (n+1)/2
    else:
        return n/2

        
nums = sorted(map(int, raw_input().split()))
h,m,l = nums[-1], nums[1], nums[0]

t1 = h
t2 = m + meth2(h-m)
t3 = l + (meth2(h-l)+meth2(m-l))

count = min(t1,t2,t3)

print count

#1 2 4
#3