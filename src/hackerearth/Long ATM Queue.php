<?php     


/*
@Title: Long ATM Queue

@Problem Statement: 

Due to the demonetization move, there is a long queue of people in front of ATMs. Due to withdrawal limit per person per day, 
people come in groups to withdraw money. Groups come one by one and line up behind the already present queue. The groups have 
a strange way of arranging themselves. In a particular group, the group members arrange themselves in increasing order of their height(not necessarily strictly increasing).

Swapy observes a long queue standing in front of the ATM near his house. Being a curious kid, he wants to count the total number of groups present in the queue waiting to withdraw money. Since groups are standing behind each other, one cannot differentiate between different groups and the exact count cannot be given. Can you tell him the minimum number of groups that can be observed in the queue?

[....]

@URL: https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/long-atm-queue-3/

@Courtesy: hackerearth

*/


    $N = fgets(STDIN);
    $queue = fgets(STDIN);
    $heights = explode(" ", $queue);
     
     
    array_unshift($heights,"0");
    //print_r($heights);
     
    $group_count = 0;
     
     
    for($i= 1; $i <= $N; $i++){
    	if($heights[$i] >= $heights[$i-1])
    		continue;
    	else
    		$group_count += 1;
    }
     
    $group_count += 1;
     
    echo $group_count
     

?>