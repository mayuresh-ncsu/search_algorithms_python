#searchUSA

import sys

def SearchUSA(search_type,src_city,dst_city,filename='roads.txt'):
	"This function searches for a path from source city to destination city using given search algorithm"
	
	import bfs, dfs, astar, Roadmap
	from HelperFunctions import ReadFileToMap
	
	#Initializing empty map which uses adjacency list data structure to store map information
	my_map = Roadmap.Roadmap()
	
	#Loading map from the text file
	ReadFileToMap(filename,my_map)

	success = False
	
	print("\nApplying '{0}' Algorithm to search path from {1} to {2}\n".format(search_type.upper(),src_city.upper(),dst_city.upper()))
	
	if(search_type == 'bfs'):
#		print("\n{}".format("BFS SEARCH".center(80,'$')))
		success = bfs.bfs(src_city,dst_city,my_map)
	elif(search_type == 'dfs'):
#		print("\n{}".format("DFS SEARCH".center(80,'$')))
		success = dfs.dfs(src_city,dst_city,my_map)
	elif(search_type == 'astar'):
#		print("\n{}".format("ASTAR SEARCH".center(80,'$')))
		success = astar.astar(src_city,dst_city,my_map)		
	else:
		print("\nInvalid Search Type: Please Try Again.\n")
		
	if(success):
		pass
		# print("{}\n".format("SUCESS".center(400,'*')))
	else:
		print("{}\n".format("FAILURE".center(400,'*')))

if(len(sys.argv)==4):
	search_algorithm = sys.argv[1].lower()
	starting_city = sys.argv[2]
	destination_city = sys.argv[3]
	
	SearchUSA(search_algorithm,starting_city,destination_city)

else:
	print("\nInvalid Input: Please Try Again.\n")

# searchUSA('bfs','minneapolis','provo')
# searchUSA('astar','minneapolis','cleveland')
# searchUSA('bfs','raleigh','miami')
# searchUSA('dfs','raleigh','miami')
# searchUSA('astar','raleigh','miami')