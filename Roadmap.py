#Class Roadmap representing Cities and Roads in the given map

class Roadmap:
	"This is class definition of graph representing roads and cities on the map."
	" This representation uses adjacency list structure for faster access to neighbors of any node"

	def __init__(self):
		"Dictionaries to maintain Adjacency Graph of each city and its coordinates"
		self._citymap = {}
		self._coords = {}
		
	def add_city(self,city_name:str,latitude,longitude):
		"Adds city to the graph with its coordinates"
		self._citymap[city_name] = {} 
		self._coords[city_name] = (latitude,longitude)
	
	def add_road(self,city1,city2,distance):
		"Adds road to the graph with two cities and travel distance between them"
		self._citymap[city1][city2] = int(distance)
		self._citymap[city2][city1] = int(distance)
	
	def get_neighbors(self,city):
		"Returns alphabetically ordered list of neighbors"
		return sorted(list(self._citymap[city].keys()))

	def get_distance(self,city1,city2):
		"Returns distance between two cities on the map"
		return self._citymap[city1][city2]

	def get_coordinates(self,city):
		"Returns coordinates of the city in the form of tuple"
		return self._coords[city]
		
	def get_cities(self):
		"For DEBUG: Returns list all the cities and prints their coordinates in the map"
		return self._coords.keys()
		#DEBUG: print(" City {} at {} and {}").format(city,self._coords[city][0],self._coords[city][1])			
		
	def print_map(self):
		"For DEBUG: Prints entire road map in city-neighbors format"
		print("\n{0}".format("MAP".center(80,'=')))
		for city in self._citymap.keys():
			print(" City : {0}\nNeighbors : {1}".format(city,self.get_neighbors(city)))
		print("\n{0}".format("END".center(80,'=')))
	
