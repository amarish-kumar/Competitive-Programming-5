/*

@Title: The Best Player

@Problem Statement: 

It's Lolympics 2016 right now, and we all know who's the best player there right now: Kalyani! 
Obviously, he has a huge female fan following and he has to make sure they are all happy and rooting for him to win the gold medals.

But with fan following comes arrogance and lack of time. Thus, he has sufficient time to interact with atmost T of his fans. 
Each fan is defined by two parameters : Name and Fan Quotient. The name defines the name of the fan, while the fan quotient is 
a measure of the fan's devotion towards Kalyani. Higher the fan quotient, greater is the devotion. Kalyani now wants to meet T of his fans. 
While selecting the fans he wants to meet, he wants to make sure that a fan with a higher fan quotient should be given a chance in favour of those with lesser fan quotient. In case of ties, he sorts their name lexicographically and chooses the lexicographically lesser named fan. 

[....]

@URL: https://www.hackerearth.com/practice/algorithms/sorting/bubble-sort/practice-problems/algorithm/the-best-player-1/

@Courtesy: hackerearth
*/

// We need to sort by two parameters: first reverse sort by fan quotient(numerical value) and then sort alphabetically by the name parameter.



object Main extends App {
	
//	case class Fan(name: String, quotient: Int)
	
	var lines = List[String]()
	for(ln <- scala.io.Source.stdin.getLines) lines = ln :: lines
	
	val T = lines.last
				 .split(" ")
				 .last
				 .toInt

	lines.dropRight(1)
		 .map(_.split(" "))
		 .map(f=> (f(0),f(1).toInt))
		 .sortBy(r=> (- r._2, r._1))
		 .take(T)
		 .map(f=> f._1)
		 .foreach(println)

}