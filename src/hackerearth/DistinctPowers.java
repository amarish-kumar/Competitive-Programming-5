/*

@Title: Distinct Powers

@Problem Statement: 

Aayush has just arrived home after his Maths Class. Today he learnt a very special thing that every number could be represented as 
a sum of distinct powers of 2.He was amazed when he came to know about this.

Example:

6 - > 4 + 2

11 -> 8 + 2 + 1

On his way he back home he kept testing this given property. While testing he realized that this special summation is unique for every number 
but it may be a subset of many other numbers.

Example :

3 -> 2+1 Thus 2+ 1 is unique for 3 but this pattern is a subset for 7 as 7 -> 4 + 2 + 1 , 11 -> 8 + 2 + 1 etc.

Since he got baffled after coming to this conclusion he asks you for help.

Given a numbers A you need to output the smallest number such that the special summation of A is subset of the special summation for that number.

Input:

The first line contains T denoting the number of test cases.

Then T lines follow each containing 1 integer A.

Output:

Print the smallest number which satisfy the above condition.

Constraints:

1 <= T <= 10000

1<= A <= 10^9
Sample Input

2
3
9



Sample Output

7
11

@URL: https://www.hackerearth.com/rang-de-java-hiring-challenge/problems/

@Courtesy: hackerearth

*/

import java.io.BufferedReader;
import java.io.InputStreamReader;

import java.util.*;

class DistinctPowers {
    public static void main(String args[] ) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line = br.readLine();
        int N = Integer.parseInt(line);
        int i,j,p;
        boolean found;
        
        for (i = 0; i < N; i++) {
            int x = Integer.parseInt(br.readLine());
            p = 0;
            found = false;
            
            for(j=0; j<31; j++){
                p = 1<<j;
                if(((p & x) == 0) && (p<=x)) {
                    found = true;
                    break;
                }
                if(p>=x)
                    break;
            }
            if(found)
                System.out.println((p+x));
            else
                System.out.println(x + (1<<j));
        }


    }
}