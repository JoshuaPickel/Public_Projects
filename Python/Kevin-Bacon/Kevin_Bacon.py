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


from collections import deque
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

class Edge:
    
    def __init__(self, movie, frm, to):
        ''' Constructor for the edge classCreate a link between vertices, connected by the movie
        self.movie: The connection between the vertives
        self.to: The actor the fist vertex is connected to via self.movie
        self.frm: The actor the second vertex is connected to via self.movie'''        
        
        self.movie = movie
        self.to = to
        self.frm = frm
        
    
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
        self.edge = None
        self.ID = key
        self.edges = None
        self.connected_to = {}

    def add_neighbor(self, neighbor,edge):
        '''
        Map the vertex to the edge it is associated to
        
        '''
        self.edges = edge
        self.connected_to[neighbor] = edge
    def __str__(self):
        '''
        returns all of the vertices in the adjacency list, as represented by the connectedTo instance variable
        '''
        return str(self.ID) + ' connected to: ' + str([x.ID for x in self.connected_to])

    def get_connections(self):
        '''
        Returns the dictionary of connections between the vertex and the other
        vertices it is connected to via an edge object
        '''
        return self.connected_to

    def get_ID(self):
        '''
        Returns the vertx I.D. (actor name)
        '''
        return self.ID

    
    
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
        self.vert_list = {}
        self.num_vertices = 0
    def __str__(self):
        '''
        Printing method to see the connection of vertices
        '''
        count = 0
        edges = ""
        for vert in self.vert_list.values():
            for vert2 in vert.get_connections():
                edges += "(%s, %s)\n" %(vert.get_ID(), vert2.get_ID())
                
        return

    def add_vertex(self, key):
        '''
        Method that add a vertex to the graph
        Parameter key: the key or name of vertex to be created
        Returns: the newly created vertex
        
        '''
        self.num_vertices = self.num_vertices + 1  # Add to the number of vertices in the graph
        new_vertex = Vertex(key)                   # Create new vertex object with key
        self.vert_list[key] = new_vertex           # Add the vertex to the self.vert_list dictionary
        return new_vertex                          # Return the new vertex

    def get_vertex(self, n):
        '''
        Method to return the vertex of an given actor name
        Parameter n: the name of the actor in which to get their vertex object
        Returns: the vertex object of n, if it exists, None otherwise
        '''
         
        if n in self.vert_list:        # Check if actor is in self.vert_list dictionary
            return self.vert_list[n]   # Return the vertex
        else:                          # Not in self.vert_list, so return none
            return None

    def __contains__(self, n):
        '''
        in operator, this method allows to ask if ' n in graph'
        '''
        return n in self.vert_list     # Return boolean

    def add_edge(self, f, t, movie):
        '''
        This method connected vertices via an edge object. (from to, via movie)
        Parameter f: the starting actor (from)
        Parameter t: the ending actor (to)
        Parameter movie: the movie they are connected by
        '''
        if f not in self.vert_list:        # If no vertex for f, make it
            nv = self.add_vertex(f)
        if t not in self.vert_list:        # If no vertex for t, make it
            nv = self.add_vertex(t)
        edge = Edge(movie,f,t)             # Make edge object 
        self.vert_list[f].add_neighbor(self.vert_list[t],edge)  # call add_neighbor to connect them
        

    def get_vertices(self):
        '''
        returns the names of all of the vertices in the graph
        '''
        return self.vert_list.keys()

    def __iter__(self):
        '''
        for functionality
        '''
        return iter(self.vert_list.values())
      

    
    
    
def bfs(g, start):
    '''
    This funcction creates and return a BFS graph. 
    Parameter g: the original graph object
    Parameter start: The root actor(vertex) in which to build the BFS tree around (Kevin Bacon)
    '''
    frontier_queue = deque()                 # Make a queue
    frontier_queue.appendleft(start)         # Put the root vertex in the queue
    discovered_set = set([start])            # Make a set to keep track of which vertices has been visited
    T = Graph()                              # Make a new grpah object
    T.add_vertex(start.ID)                   # Make a vertex of the root vetrex in the new graph
    while len(frontier_queue) > 0:           # While there are still vertices to look at
        curr_v = frontier_queue.pop()            # Pop the queue to process the next vertex
        for adj_v in curr_v.get_connections():   # Loop though their connection dictionary
            if adj_v not in discovered_set:      # If we haven't already looked at the connection
                frontier_queue.appendleft(adj_v) # Add this vertex to be processed
                discovered_set.add(adj_v)        # add it tot discovered set
                T.add_edge(adj_v.ID,curr_v.ID,adj_v.connected_to[curr_v].movie)    # Make edges in new grpah connecting root to the other vertices
    return T                                                                       # Return the BFS graph


def actor_name(file):
    ''' This function maps actor I.D's to actor names
    Parameter file: file to process
    Returns: dictionary of actor I.D. to actor name'''
    actor_dict = {}                             # Make new dictionary  
    file = open(file, "r", encoding="latin-1")  # Open the file, encoding for encoded characters                          
    for line in file.readlines():               # For each line in the file
        line = line.strip()                     # Remove special characters
        line = line.split('|')                  # Split at |
        actor_id = line[0]                      # First item in split list is the actor id
        actor_name = line[1]                    # Second item in split list is the actor name  
        actor_dict[actor_id] = actor_name       # Map the actor I.D. to their name
    return actor_dict


def movie_names(file):
    ''' This function mapes movie I.D.'s to the movie name
    Parameter file: the file to process
    Returns: dictionary of movie I.D. to movie name '''
    movie_name_dict = {}                           # Make new dictionary
    file = open(file,"r",encoding="latin-1")       # Open the file, encoding for encoded characters
    for line in file.readlines():                  # For each line in the file
        line = line.strip()                        # Remove special characters
        line = line.split('|')                     # Split at |
        movie_id = line[0]                         # First item in split list is movie I.D.
        if movie_id == '﻿1':
            movie_id = '1'
        movie_name = line[1]                       # Second item in split list is movie name
        movie_name_dict[movie_id] = movie_name     # Map movie I.D. to movie name
    return movie_name_dict                         

def movie_actors(file,actor_dict,movie_name_dict):
    '''This function maps movies to the actors that appeared in the movie
    Parameter file: the gile to process
    Parameter actor_dict: dictionary of actor I.D's to actor names
    Parameter movie_name_dictL dictionary of movie I.D's to movie names
    Returns: dictionary of movies and actors that appeared in that movie'''
    movie_actor_dict = {}                      # Make new dictionary
    file = open(file,"r",encoding="utf-8")     # Open the file, encoding for encoded characters
    for lines in file.readlines():             # For each line in the file
        lines = lines.strip()                  # Strip to remove encoded characters
        lines = lines.split('|')               # Split at |
        movie_id = lines[0]                    # First item in split list is the movie I.D.
        actor_id = lines[1]                    # Second item is actor I.D.
        movie_id = movie_name_dict[movie_id]   # Get movie name from movie_name_dict
        if movie_id in movie_actor_dict:       # If already an actor for a movie in the dictionary
            movie_actor_dict[movie_id].append(actor_dict[actor_id])   # Append them to the list
        else:
            movie_actor_dict[movie_id] = [actor_dict[actor_id]]       # Otherwise make an entry
    return movie_actor_dict                                           # Return the dictionary of movies to actors that appeard in the movie

       
def make_vertices(actor_dict):
    '''This function returns the list of actor names '''
    vertices = list(actor_dict.values())
    return vertices

def make_edges(movie_actor_dict):
    '''This function creats a tuple representation of all the edges needed to 
    create the original graph
    Parameter movie_actor_dict: the dictionary representing movies to actors
    appearing in that movie
    Returns: all the edges that need to be created'''
    edges = []                                       # Make an enpty array
    movies_list = list(movie_actor_dict.keys())      # Grab all movie names
    for movies in movies_list:                       # Loop through each movie
        actor_list = list(movie_actor_dict[movies])  # Grab list of actors for the movie
        pairs = pair_maker(actor_list,movies)        # Call on helper function to create the combination of edges
    edges.extend(pairs)                              # Extend result to edges array
    return edges
        
empty_list = []                   # Empty starting list for pair maker function
def pair_maker(L,movie):
    '''This function makes all the possible edges from the multiple actors in each movie
    Parameter L: list of actor names
    Parameter movie: the movie they appeared in '''
    if len(L) == 0:               # Base case for recursion
        return empty_list         
    for i in range(1,len(L)):     # Loop through all actors after thr first actor
        pair = (L[0],L[i],movie)  # Make a pair between first actor and others
        empty_list.append(pair)   # Add pairs to the empty list
    L.pop(0)                      # Remove first actor, as their pairs are made 
    pair_maker(L,movie)           # Recursive call to make remaining pairs
    return empty_list


def find_path(actor1,T):
    '''This function searches the BFS grpah to find the path from an actor
    to Kevin Bacon, and prints the results along the way
    Parameter actor1: the actor to find a path to Kevin Bacon 
    Parameter T: the bfs tree to search''' 
    count = 0         # Counter variabel to count steps
    label = {}        # label Dictionary for networx
    edges = []        # Edge list for networkx
    flag = True       # Start with a flag of True
    if actor1 not in T:   # Actor1 has no path to Kevin Bacon
        print("This actor Does not have a path to Kevin Bacon")
        return
    if actor1 == "Kevin Bacon":  # Kevin Bacon has Baocn Number of 0
        G = nx.Graph()           # Draw graph with one Kevin Bacon Node
        G.add_node('Kevin Bacon')
        plt.figure(figsize = (11,9))                     # Make figure, scale it
        plt.title("Kevin Bacon's Bacon number is 0")     # Title for the grpah visulization        
        nx.draw(G,pos = nx.circular_layout(G),labels = {'Kevin Bacon':'Kevin Bacon'},node_size = 6000)  
        plt.show()
        flag = False
        return
    else:                         # Actor1  has a path
        edge = T.get_vertex(actor1).edges  # Get actor1's edge
        while flag:                        # While flag has not switched 
            if edge.frm == 'Kevin Bacon':   # We have found Kevin Bacon
                flag = False               # switch flag
            else: 
                first_actor = edge.frm     # Get the first actor
                second_actor = edge.to     # Get second actor
                movie = edge.movie         # Get the movie connecting them
                label[(first_actor,second_actor)] = movie      # Create entry in label dictionary for neworkx
                edges.append(list((first_actor,second_actor)))  # Create entry in edge list for networkx
                edge = T.get_vertex(edge.to).edges              # Get the next vertex to get the next connection
                print("%s Appeared in %s, with %s" %(first_actor,movie,second_actor)) # Printing results
                if edge == None:
                    flag = False
                count+=1
        G=nx.DiGraph()                                   # Create a directe graph
        G.add_edges_from(edges)                          # Add all of the edges to the graph
        pos = nx.circular_layout(G)                      # Circular layout for networx visulization
        plt.figure(figsize = (11,9))                     # Make figure, scale it
        plt.title(actor1+ " 's" + " Bacon Number is: " + "{}".format(count),loc = 'center')  # Title for the grpah visulization
        nx.draw(G,pos = pos, edge_color='green',width=5,linewidths=0,\
        node_size=6000,alpha=1,\
        labels={node:node for node in G.nodes()},style = 'dotted')                 # Draw the grpah
        nx.draw_networkx_edge_labels(G,pos,edge_labels=label,font_color='black')   # Draw edge labels on the grpah
        plt.show()

 
 
def insight(actors,t):
    '''This function makes a dictionary of all actor's bacon numbers
    Parameter actors: dictionary of actor I.D's to names
    Parameter t: the befs grpah to search
    Returns Tuple fo interesting statistics about the BFS grpah'''
    actors = list(actors.values())    # Get all of the actor names
    temp = (0,actors[0])              # temp tuple for data storage
    bacon_dict = {}                   # Make dictionary to hold data
    for i in actors:                  # Loop through all actors
        flag = True                   # Flag variable set to True
        if i in t:                        # If actor is in the graph
            count = 0                    # make count variable
            edge = t.get_vertex(i).edges  # Get the edges of the actor
            while edge != None:           # While there is still an edge
                if edge.frm == 'Kevin Bacon': # We are at Kevin Bacon, Break
                    break
                else:                        # Otherwise increase count, get the next edge
                    count+=1                
                    edge = t.get_vertex(edge.to).edges
            bacon_dict[i] = count                       # Make entry in dictionary for actor name and the Bacon Number
    biggest_bacon_actor = max(bacon_dict ,key = bacon_dict.get)   # Find first occurance(actor) of largest bacon number
    biggest_bacon_number = bacon_dict[biggest_bacon_actor]        # Find the Bacon number associated to actor wiht largest Baocn number
    Small_Bacon = sum(value == 1 for value in bacon_dict.values()) # Find how many acotrs have a Bacon number of 1
    stats = (biggest_bacon_actor,biggest_bacon_number,Small_Bacon,bacon_dict) # Make tuple of above stats, and the bacon_number dictionary
    
    return stats


def graph_builder(edges):
    '''This function build a graph.
    Parameter edges: the edges to build the graph from
    Returns g: a grpah object'''
    g = Graph()                              # Make an grpah object
    for i in edges:                          # Add all edges to grpah
        g.add_edge(i[0],i[1],i[2])
        g.add_edge(i[1],i[0],i[2])       
    return g
    

def main():
    '''Main function of program. Takes user input of actor name, handles boudaries,
    and searches the BFS for the actor's Bacon Number
    '''
    # Create all dictionaries to map movies to the actors that were in that movie
    actors = actor_name('actors.txt')
    movies = movie_names('movies.txt')
    actor_movie_pairs = movie_actors('movie-actors.txt',actors,movies)
    
    
    edges = make_edges(actor_movie_pairs)    # Create all edges for the graph
    g = graph_builder(edges)
       
    bfs_graph = bfs(g,g.get_vertex('Kevin Bacon'))  # Make BFS graph form original graph
    Stats = insight(actors,bfs_graph)               # Get the stats tuple for BFS graph

    
    # Print statements for user, printing interestind stats first
    print("Here are some interesting statistics about the Kevin Bacon Graph: ")
    print("An actor with the highest Bacon number is %s with a Bacon number of: %i" %(Stats[0],Stats[1]))
    print("There are %i actors who have a Bacon number of 1!" %(Stats[2]))
    print("\n")
    
    # Print how to wuit game, and how to enter actor names
    print("When you would like to quit, please enter 'Q' or 'q' in to prompt box")
    print("You can type an actor's name in upper or lowercase, or a combination of the two.")
    print("Ex: 'Tom cruise', 'Tom Cruise' , 'TOm CruIse' \n ")
    while True:                                                                  # Loop for user input
        actor_search = input("Please name an actor to find their Bacon number: ") # Get user input
        print("\n")
        if actor_search.lower() == "q":                                          # Break if user wishes to wuit game
            print("You have chosen to end the game. Goodbye.")
            break
        else:                                                                    
            new_dict = dict((k.lower(), v) for k, v in g.vert_list.items())      # Create a new dictionary of original graph with keys in lowercase
            actor_search = actor_search.lower()                                  # Convert user input to all lowercase(to handle input variance)
            if actor_search in new_dict:                                         # See if user input is in new_dict
                actor_search = new_dict[actor_search].ID                         # Get the proper representation of user input, by referencing actor's vertex I.D.(name)
                Bacon = Stats[3]                                                 # Get the actor's Bacon number through stats vairable(dictionary holding all actor's Bacon number)
                number = Bacon[actor_search]
                print("%s's Bacon number is: %i" %(actor_search,number))         # Print statement for user
                find_path(actor_search,bfs_graph)                                # Find the path of the actor(path printed in find_path function)
                print("\n")
            else:                                                                # If the user input is not found, then it was in invalid input(If actor has no path, this will\
                print("INVALID INPUT!!! Please try again \n")                    # be printed in the find_path function
main()