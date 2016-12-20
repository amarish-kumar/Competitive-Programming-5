/*

@Title: Prefix Compression

@Problem Statement: 

You are in charge of data transfer between two Data Centers. Each set of data is represented by a pair of strings. 
Over a period of time you have observed a trend: most of the times both strings share some prefix. 
You want to utilize this observation to design a data compression algorithm which will be used to reduce amount of data to be transferred.

You are given two strings, and , representing the data, you need to find the longest common prefix () of the two strings. 

[....]

@URL: https://www.hackerrank.com/contests/lambda-calculi-oct14/challenges/prefix-compression
*/

/*
Basically we need to find the longest common prefix among given two strings.
*/

object Main extends App {
	
	var words = List[String]() 
	for(ln <- io.Source.stdin.getLines) words = ln :: words
	
	val prefix = words(0).zip(words(1)).takeWhile(t => t._1 == t._2).map(_._1).mkString

	val prefixLength = prefix.length
	val xd = words(1).substring(prefixLength)
	val yd = words(0).substring(prefixLength)

	println(prefixLength + " " + prefix)
	println(xd.length + " " + xd)
	println(yd.length + " " + yd)

}