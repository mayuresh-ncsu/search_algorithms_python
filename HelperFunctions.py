# Helper Functions

import Roadmap
import fileinput, re

def ReadFileToMap(filename: str, my_map:Roadmap):
	"This function Reads text file and loads map information"
	num_cities,num_roads = 0,0

	f = fileinput.input(filename)
	for line in f:
		comment_line = re.search(r"^%[\S\s]+",line)
		city_line = re.search(r"^(\w+),\s+([0-9]+\.[0-9]+),\s+(-?[0-9]+\.[0-9]+)",line)
		road_line = re.search(r"^(\w+),\s+(\w+),\s+([0-9]+)",line)
		if(comment_line):
			pass
		elif(city_line):
			my_map.add_city(city_line.group(1),float(city_line.group(2)),float(city_line.group(3)))
		elif(road_line):
			my_map.add_road(road_line.group(1),road_line.group(2),road_line.group(3))

			
def heurisitc(node,dst,roadmap):
	"This function returns heuristic value for given arguments"
	
	import math
	
	(lat1,long1) = roadmap.get_coordinates(node)
	(lat2,long2) = roadmap.get_coordinates(dst)	
	h_n = math.sqrt(((69.5 * (lat1-lat2)) ** 2) + ((69.5 * math.cos((lat1+lat2)/360 * math.pi) * (long1-long2)) ** 2))
	
	return h_n

 	
def backtrack(dst,parents):			
	"This function generates Backtracking path from destination using parents dictionary (used ONLY for A*)" 
	
	successor = dst
	path = [dst]
	while(successor in parents):
		parent = parents[successor]
		path.append(parent)
		successor = parent
	path.reverse()
	return path	

	
	