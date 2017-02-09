import scala.collection.mutable.Stack
object BalancedString2 {

	def main( args: Array[String]){
	
//		val s = "[ABC{DEF}]"
//		val s = "[{}"
//		val s = "[{(())]"
//		val s = "[{()()()}{}]"
//		val s = "[{()()(){}]"
		val s = "{     AAA BHARAT }   ]"


		val matchingBracks = List(Tuple2('{', '}'), Tuple2('[',']'), Tuple2('(', ')'))

		val stack = Stack[Char]()
		val len = s.length - 1
		val allowedBrackets = List('{','[','(',')',']','}')

		for(i <- 0 to len){

			if(allowedBrackets.contains(s(i))){
				if(stack.isEmpty)
					stack.push(s(i))
				else{
					val matchingParter = matchingBracks.filter(_._2 == s(i))
					val isOpening  = matchingParter.isEmpty
					if(isOpening)
						stack.push(s(i))
					else{
						val tos = stack.pop
						if(!(tos == matchingParter.head._1)) {
							stack.push(tos)
							stack.push(s(i))
						}			
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