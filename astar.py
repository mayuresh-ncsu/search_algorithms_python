#ASTAR

import Roadmap
from HelperFunctions import heurisitc
from HelperFunctions import backtrack

def astar(src : str, dst : str, roadmap : Roadmap):
	"Performs path search from src to dst using A* search algorithm"	
	from queue import PriorityQueue
	
	#Search queue is priority queue where priority of each node is sum of cost to reach node g(n) and heuristic h(n)
	search_queue = PriorityQueue()
	search_queue.put((0,src))
	
	#Dictionary to keep track of parent nodes 
	parents = {}
	
	#Dictionary to keep track of path cost for each expanded node
	path_cost = {}
	path_cost[src] = 0
	expanded = [] 
	
	while(not search_queue.empty()):
		node = search_queue.get()[1]
		
		#Goal Test
		if node == dst:				
			#Print Results 
			print("Path from {0} to {1}: {2}\nPath Cost: {3} miles".format(src,dst,backtrack(dst,parents),path_cost[dst]))
			print("Number of Nodes Expanded: {0}\nExpanded Nodes: {1}".format(len(expanded),expanded))
			return True
		
		#Expansion of node
		neighbors = roadmap.get_neighbors(node)
		expanded.append(node)
		#DEBUG: print("{} , {} ".format(expanded,current[0]))
		for new_node in neighbors:
			#Calculate path cost of neighbor
			new_path_cost = path_cost[node] + roadmap.get_distance(node,new_node)
			
			#Condition to check : (i)new node is not already expanded and has cost assigned to it or (ii)new cost is less than previous cost 
			if(new_node not in path_cost or new_path_cost<path_cost[new_node]):
				#Assign path cost to new node (g(n))
				path_cost[new_node] = new_path_cost
				#Assign priority = g(n) + h(n) to new node which is to be inserted in queue
				priority = path_cost[new_node] + heurisitc(new_node,dst,roadmap)
				#Insert new node and along with its priority in Search queue
				search_queue.put((priority,new_node))
				#Remember where new node came from for backtracking solution		
				parents[new_node] = node	
		
	return False	
