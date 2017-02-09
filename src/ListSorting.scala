import scala.io.StdIn

/* 

Sort a list and print the difference between the maximum variation among the elements. Highest variation is the absolute difference
between the maximum/largest and smallest/minimum element of the list.

Print variation for each test case. Each test case consists of two lines.
First line contains an integer value N, denoting the number of elements in the list.
Next line contains N space separated integers, of the list.

Output has 't' lines, each line prints the maximum variation.

*/

object HelloWorld {
    def main(args: Array[String]) {
        
        val t = StdIn.readInt()
        for(i <- 1 to t){
            val n = StdIn.readInt()
            val nums = StdIn.readLine()
            
            val arr = nums.split(" ").map(_.toInt).sorted
            println(arr.last - arr.head)
        }

    }
}