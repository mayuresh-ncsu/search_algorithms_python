# BFS

import Roadmap

def bfs(src : str, dst : str, roadmap : Roadmap):
	"This function performs breadth first search on given map to find path from 'src' to 'dst'"
	
	from queue import Queue
	#Search queue is a FIFO Queue stores each path. This increases memory requirement but avoids backtracking
	search_queue = Queue()
	search_queue.put([src]) 
	#ALTERNATE: search_queue.put((1,[src])) 

	#Dictionary to maintain path costs to each expanded node (Optional for BFS)
	path_cost = {}
	path_cost[src] = 0	
	expanded = []
	
	if(src == dst):					
		#Checking for Special case
		print("\nDestination {} already reached! \nTraveling distance {} miles".format(dst,path_cost[dst]))
		return True
		
	while(not search_queue.empty()):
		#Node to be checked and expanded is the last element in current path
		path = search_queue.get()
		node = path[-1]
		#ALTERNATE: node = path[1][0]		
		
		#Checking whether node is already expanded
		if node not in expanded:	
			if node == dst:			
				#Goal Test
				#ALTERNATE: path.reverse()
				print("Path from {0} to {1}: {2}\nPath Cost: {3}".format(src,dst,path,len(path)-1))
				print("Number of Nodes Expanded: {0}\nExpanded Nodes: {1}".format(len(expanded),expanded)) 
				return True
			else:	
				neighbors = roadmap.get_neighbors(node)
				expanded.append(node)
				#DEBUG: print(expanded)
				for new_node in neighbors:		
					#Processing neighbors in alphabetical order
					if new_node not in expanded:		
					#Skip if newly generated node already expanded 
						current_path = list(path)		
						current_path.append(new_node)	
						#Add Newly formed path after appending new node to the search Queue
						search_queue.put(current_path)	
						#ALTERNATE: search_queue.put((len(current_path),current_path))
						
						#Storing total cost for reaching new node in dictionary	
						path_cost[new_node] = path_cost[node] + roadmap.get_distance(node,new_node)				
	return False

	