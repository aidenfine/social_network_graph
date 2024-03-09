class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertex):
        """ returns a list of all the edges of a vertex"""
        return self._graph_dict[vertex]
        
    def all_vertices(self):
        """ returns the vertices of a graph as a set """
        return set(self._graph_dict.keys())

    def all_edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in 
            self._graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. 
            Otherwise nothing has to be done. 
        """
        if vertex not in self._graph_dict:
            self._graph_dict[vertex] = set()

    def add_edge(self, *people):
        """Add friendships between people."""
        for person1 in people:
            self.add_vertex(person1) 
            for person2 in people:
                if person1 != person2:
                    self.add_vertex(person2) 
                    self._graph_dict[person1].add(person2)
                    self._graph_dict[person2].add(person1)


    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbor in self._graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges
    
    def find_path(self, start_vertex, end_vertex, path=None):
        """ find path from start to end
        """
        if path == None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None
    
    def recommend_friend(self, person):
        """ recommend friends for this person"""
        return person

    
    def find_distance(self, start_vertex, end_vertex, path=None, distance=0):
        """ Find distance from start to end """
        if path is None:
            path = []
        graph = self._graph_dict
        path = path + [start_vertex]

        if start_vertex == end_vertex:
            return distance

        if start_vertex not in graph:
            return -1

        for vertex in graph[start_vertex]:
            if vertex not in path:
                new_distance = self.find_distance(vertex, end_vertex, path, distance + 1)
                if new_distance != -1:
                    return new_distance

        return -1

    
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self._graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, 
                                                     end_vertex, 
                                                     path)
                for p in extended_paths: 
                    paths.append(p)
        return paths
    
    def __iter__(self):
        self._iter_obj = iter(self._graph_dict)
        return self._iter_obj
    
    def __next__(self):
        """ allows us to iterate over the vertices """
        return next(self._iter_obj)

    def __str__(self):
        res = "vertices: "
        for k in self._graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res
