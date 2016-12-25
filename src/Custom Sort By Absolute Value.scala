/*

@Title: Sort me this way !

@Problem Statement: 

Given an array A consisting of integers of size N, you need to sort this array in non-decreasing order 
on the basis of the absolute value of the integers in the array.

Print the sorted array to output then. 

[....]

@URL: https://www.hackerearth.com/practice/algorithms/sorting/quick-sort/practice-problems/algorithm/fredo-and-absolute-sorting-24

@Courtesy: hackerearth
*/


// Simply need to write a custom sortBy function(lambda) which considers the absolute(abs) value of each integer it receives.
// Stable Sorting: Below used sorting is stable, meaning, it maintains the relative ordering among the numbers among numbers having equal absolute values.


object Main extends App {
	
	def printSameLine(x: Int) = {
		print(x + " ")
	}

	var lines = List[String]()
    for(ln <- scala.io.Source.stdin.getLines) lines = ln :: lines
        
//	val ans = lines.head.split(" ").map(_.toInt).sortBy(_.abs)
// 	ans.foreach(println)
//	ans.foreach(printSameLine)

	lines.head.split(" ").map(_.toInt).sortBy(_.abs).foreach(printSameLine)
}