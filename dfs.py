#DFS

import Roadmap

#Global variables to be accessed during multiple calls of recursive_dfs
dfs_path = []
dfs_expanded = []
dfs_path_cost = 0

def recursive_dfs(node,dst,roadmap):
	"Performs recursive depth first search from 'node' to 'dst'"
	global dfs_path,dfs_expanded,dfs_path_cost			

	#Goal Test before expansion
	if node == dst: 	
		return True
		
	#Expand current node from map
	neighbors = roadmap.get_neighbors(node)				
	dfs_expanded.append(node)
	#DEBUG : print(dfs_expanded)
	#Process neighbors in alphabetical order
	for new_node in neighbors:					
		#Check for repeated nodes and skip
		if new_node not in dfs_expanded:	
			#Recursive call to the function which returns 'success'
			if(recursive_dfs(new_node,dst,roadmap)):	
				#DFS path is formed by appending each node which had returned success
				if(dfs_path):
					dfs_path_cost += roadmap.get_distance(new_node,dfs_path[-1])	 
				dfs_path.append(new_node)				
				return True
	return False
	
def dfs(src : str, dst : str, roadmap : Roadmap):
	"This function performs depth first search on given map to find path from 'src' to 'dst'"
	
	global dfs_path,dfs_expanded,dfs_path_cost
	#Initializing Global variables
	dfs_path = []	
	dfs_expanded = []
	dfs_path_cost = 0

	if src == dst:		
		#Checking for Special Case
		success = True
	else:				
		#Calling recursive function 
		success = recursive_dfs(src,dst,roadmap)
		
	if success:
		#Append source information to returned path and total cost
		dfs_path_cost += roadmap.get_distance(src,dfs_path[-1])
		dfs_path.append(src)
		dfs_path.reverse()
		print("Path from {0} to {1}: {2}\nPath Cost: {3}".format(src,dst,dfs_path,len(dfs_path)-1))
		
	print("Number of Nodes Expanded {0}\nExpanded Nodes: {1}".format(len(dfs_expanded),dfs_expanded))						
	return success
