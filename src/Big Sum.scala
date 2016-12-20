/*

@Title: A Very Big Sum

@Problem Statement: 

You are given an array of integers of size N. 
You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large. 

[....]

@URL: https://www.hackerrank.com/challenges/a-very-big-sum

@Courtesy: hackerrank
*/


// Calculating the Sum in functional style


object Main extends App {
	
	var lines = List[String]()
	for(ln <- io.Source.stdin.getLines) lines = ln :: lines
	
	println(lines.head.split(" ").foldLeft(0L){_.toLong + _.toLong})
	println(lines.head.split(" ").map(_.toLong).sum)		
	println(lines.head.split(" ").par.map(_.toLong).sum)	// Parallel Collection
	
}