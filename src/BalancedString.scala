import scala.collection.mutable.Stack

/* 

Check whether a String is balanced or not. Allowed brackets are '{}', '()' and '[]'. A balanced string can have equal number of open and closing
brackets, and then may contain any number of Alphanumeric characters.

*/

object BalancedString {

	def main( args: Array[String]){
	
		val s = "[ABC{DEF}]"
//		val s = "[{}"
//		val s = "[{(())]"
//		val s = "[{()()()}{}]"
//		val s = "[{()()(){}]"

		val bracks = s.filter(!_.isLetterOrDigit)
		println(bracks)

		val matchingBracks = List(Tuple2('{', '}'), Tuple2('[',']'), Tuple2('(', ')'))

		val stack = Stack[Char]()
		val len = bracks.length - 1

		for(i <- 0 to len){

			if(stack.isEmpty)
				stack.push(bracks(i))
			else{
				val matchingParter = matchingBracks.filter(_._2 == bracks(i))
				val isOpening  = matchingParter.isEmpty
				if(isOpening)
					stack.push(bracks(i))
				else{
					val tos = stack.pop
					if(!(tos == matchingParter.head._1)){
						stack.push(tos)
						stack.push(bracks(i))
					}
				
				}
			}
		}

		if(stack.isEmpty){
			println("Balanced String")
		}
		else{
			println("Unbalanced String")
		}
	}
}