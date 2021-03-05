# ############################################################################
# Author: Josh Pickel
# Date: 11/23/19
# Assignment: Programming Assignment 6
# Course: CPTS 215, Fall 2019
# Description: This program reads files containing actor I.D's and names, movie 
# I.D's and names, and movie I.D's to actor I.D's and maps each actor I.D. to 
# thier name, each movie I.D. to thier name, and then maps each actor to what 
# movie they appeared in. Then the program builds a graph connecting all actors 
# together via the movie they appeared in. That graph is then ran though a BFS 
# algorithm, building a shortest path graph to Kevin Bacon.
# ###########################################################################

Edge Class:

def __init__(self, movie, frm, to):
        ''' Constructor for the edge classCreate a link between vertices, connected by the movie
        self.movie: The connection between the vertives
        self.to: The actor the fist vertex is connected to via self.movie
        self.frm: The actor the second vertex is connected to via self.movie'''  

Vertex Class:

class Vertex:
    '''
    Holds necessary data for each vertex, and keeps track of edges between vertices
    '''

def __init__(self, key):
        '''
        COnstructor for the Vertex class.
        self.edge: the edge the vertex is associated to (only holds one for 
        edge reference after bfs completes)
        self.ID is the actor's name
        self.conencted to: dictionary that maps the vertex and its connection 
        between other vertices to their edge object
        '''        

def add_neighbor(self, neighbor,edge):
        '''
        Map the vertex to the edge it is associated to
        
        '''

def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''

def get_connections(self):
        '''
        Returns the dictionary of connections between the vertex and the other
        vertices it is connected to via an edge object
        '''

def get_ID(self):
        '''
        Returns the vertx I.D. (actor name)
        '''

Graph Class:

class Graph:
    '''
    Contains a dictionary that maps vertex names (actors) to vertex objects. 
    '''

def __init__(self):
        '''
        Constructor for the Graph class
        self.vert_list: dictionay of each actor mapping to their vertex object
        self.num_vertices: number of vertices in the graph
        
        '''

def __str__(self):
        '''
        Printing method to see the connection of vertices
        '''

def add_vertex(self, key):
        '''
        Method that add a vertex to the graph
        Parameter key: the key or name of vertex to be created
        Returns: the newly created vertex
        
        '''

def get_vertex(self, n):
        '''
        Method to return the vertex of an given actor name
        Parameter n: the name of the actor in which to get their vertex object
        Returns: the vertex object of n, if it exists, None otherwise
        '''

def __contains__(self, n):
        '''
        in operator, this method allows to ask if ' n in graph'
        '''

def add_edge(self, f, t, movie):
        '''
        This method connected vertices via an edge object. (from to, via movie)
        Parameter f: the starting actor (from)
        Parameter t: the ending actor (to)
        Parameter movie: the movie they are connected by
        '''

def get_vertices(self):
        '''
        returns the names of all of the vertices in the graph
        '''
def __iter__(self):
        '''
        for functionality
        '''

Functions:

def bfs(g, start):
    '''
    This funcction creates and return a BFS graph. 
    Parameter g: the original graph object
    Parameter start: The root actor(vertex) in which to build the BFS tree around (Kevin Bacon)
    '''

def actor_name(file):
    ''' This function maps actor I.D's to actor names
    Parameter file: file to process
    Returns: dictionary of actor I.D. to actor name'''

def movie_names(file):
    ''' This function mapes movie I.D.'s to the movie name
    Parameter file: the file to process
    Returns: dictionary of movie I.D. to movie name '''

def movie_actors(file,actor_dict,movie_name_dict):
    '''This function maps movies to the actors that appeared in the movie
    Parameter file: the gile to process
    Parameter actor_dict: dictionary of actor I.D's to actor names
    Parameter movie_name_dictL dictionary of movie I.D's to movie names
    Returns: dictionary of movies and actors that appeared in that movie'''

def make_vertices(actor_dict):
    '''This function returns the list of actor names '''

def make_edges(movie_actor_dict):
    '''This function creats a tuple representation of all the edges needed to 
    create the original graph
    Parameter movie_actor_dict: the dictionary representing movies to actors
    appearing in that movie
    Returns: all the edges that need to be created'''

def pair_maker(L,movie):
    '''This function makes all the possible edges from the multiple actors in each movie
    Parameter L: list of actor names
    Parameter movie: the movie they appeared in '''

def find_path(actor1,T):
    '''This function searches the BFS grpah to find the path from an actor
    to Kevin Bacon, and prints the results along the way
    Parameter actor1: the actor to find a path to Kevin Bacon 
    Parameter T: the bfs tree to search''' 

def insight(actors,t):
    '''This function makes a dictionary of all actor's bacon numbers
    Parameter actors: dictionary of actor I.D's to names
    Parameter t: the befs grpah to search
    Returns Tuple fo interesting statistics about the BFS grpah'''

def graph_builder(edges):
    '''This function build a graph.
    Parameter edges: the edges to build the graph from
    Returns g: a grpah object'''
