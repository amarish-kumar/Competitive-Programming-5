'''

@Title: Exploring ruins

@Problem Statement:

Little robot CJ-17 is exploring ancient ruins. He found a piece of paper with a word written on it. 
Fortunately, people who used to live at this location several thousand years ago used only two letters 
of modern English alphabet: 'a' and 'b'. It's also known, that no ancient word contains two letters 'a' in a row. 
CJ-17 has already recognized some of the word letters, the others are still unknown.

CJ-17 wants to look up all valid words that could be written on this paper in an ancient dictionary. 
He needs your help. Find him the word, which is the first in alphabetical order and could be written on the paper.
[...]

@URI: https://www.hackerearth.com/practice/algorithms/greedy/basics-of-greedy-algorithms/practice-problems/algorithm/exploring-ruins/

@Courtesy: hackerearth

'''

## Building the string one character by character and comparing it with one previous and the immediate next character. Greedy approach.


s=raw_input()
l=len(s)
if l > 1:
    l -= 1
    curr = s[0]
    if s[0] == '?':
        curr = 'a' if s[1] != 'a' else 'b'
    
    new_s = curr
    for i in xrange(1,l):
        if s[i] == '?':
            curr = 'a' if (curr != 'a' and s[i+1] != 'a') else 'b'
        else:
            curr = s[i]
        new_s += curr
    
    if s[-1] == '?':
        curr = 'a' if curr != 'a' else 'b'
    else:
        curr = s[-1]
    new_s += curr
    
    print new_s
else:
    new_s = 'a' if s[0] != 'b' else 'b'
    print new_s