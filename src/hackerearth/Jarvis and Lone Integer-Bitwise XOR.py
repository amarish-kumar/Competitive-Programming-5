'''

@Title:	Jarvis and Lone Integer

@Problem Statement: 

Today Tony Stark is upset with Jarvis, as it blew the whole plan of him defeating the Flash in parallel universe by showing him two images of Flash. 
Tony couldn't identify the real one and ended up getting hit hard. Jarvis is upset too and he wants to prove that it was not his mistake. 
Help Jarvis to prove himself faithful and true AI.

To prove, that Jarvis is not at fault, he is given N non-negative integers and he has to identify a lone integer among them. 
A lone integer is defined as an integer in the given array of integers that is left alone after pairing each of the other integers. 
Two integers can be paired if they have same value in decimal number system and have different indices in the array. 

[....]

@URL: https://www.hackerearth.com/practice/basic-programming/bit-manipulation/basics-of-bit-manipulation/practice-problems/algorithm/unit-existence/

@Courtesy: hackerearth

'''


t=int(input())
while t:
	t -= 1
	n = input()
	arr = map(int, raw_input().split())
	n = 0
    
    for i in arr:
    	n = n^i
    
    print n if n else -1