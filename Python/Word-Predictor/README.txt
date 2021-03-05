# ############################################################################
# Programmer: Josh Pickel
# Class: CptS 215, Fall 2019
# Programming Assignment #3
# 10/6/19
#
# Description: This program makes Unordered and Ordered LinkedLists, with
#              Various methods. It also will calculate the runtime of different
#              sorting algorithms on different sized and types of LinkedLists,
#              and graph the results.   
# ############################################################################

Classes/Methods:

class Node:
    ''' This class Holds all the data for nodes, and houses the methods
    used for nodes'''

def __init__(self,key,value):      # Constructor for node class, with attributes

def __str__(self):
        ''' This method aloows one to visualize Maps '''

def get_key(self):           # get_data method returns the data attribute for node
        '''This method returns the Node's data
        Returns: node's data'''

def get_value(self):
        '''This method returns the value for the node '''


def get_next(self):           # get_next returns the next node
        '''This method returns the next node
        Returns: next node'''

def get_previous(self):        # get_previous returns previous node
        '''This method returns the nodes previous.
        Returns: the  previous node'''

def set_value(self,new_val):   # set_data assigns data to the node
        '''This method assigns the nodes data attribute.
        Parameter new_data: The data for the node'''

def set_next(self,new_next):   # set_next sets the nodes next attribute
        '''This method sets the node's next pointer.
        Parameter new_next: The node the pointer is to be changed to'''

def set_prev(self,new_prev):   # set_prev sets the nodes previous attribute
        '''This methos sets the node's previous pointer.
        Parameter new_prev: The node the pointer is to be changed to'''

Doubly Linked List Class:

class DoublyLinkedList:
    '''This clas is a class for LinkedList, houses necessary data and methods
    for the linked list.'''

def __init__ (self):  # Constructor for doubly linked class


def __str__(self):
            '''
            This method allows to visualize the Linked List
            '''

def add_item(self,item):          # adds nodes to the LinkedList, at the
        '''This method adds an node to the front of the CircularDoublyLinkedList. This method
        assumes the item is not already in the list
        Parameter item: the item to be added to the LinkedList'''

 def append(self,item):            # appends data to back of list
        '''This method will add an node to the back of the CircularDoublyLinkedList.This 
        method assumes the item is not already in the LinkedList
        Parameter item: the item to be added to the LinkedList'''

def insert(self, index, item):
        '''
        Adds a new item to the CircularDoublyLinkedList at position imdex. It needs the item and returns nothing. 
        Assume the item is not already in list.
        Parameter item: item to be added to linked list
        Parameter index: the position desired for the item to be added.

def is_Empty(self):               # Check to see if LinkedList is empty

def pop(self, index = None):
        '''This method will return and remove the item at the given index. 
        Parameter index: the index in which you wish to pop. If no index passed, 
        method will pop the last item in the list.
        Returns: The item at the index being popped'''

def search(self, item):
        '''This method searches for an item in the CircularDoublyLinkedList, and
        returns the index.
        Parameter item: item to search for
        Returns: index position of item, -1 if not in list'''

def remove(self,item):
        '''This method removes an item from the doubly linked list and reassigns
        pointers as necessary.
        Parameter item: the item to remove
        '''

def List_size(self):
        '''This method returns the size of the doubly linked list. '''

def make_copy(self):
        '''This function makes a copy of of a CircularDoublyLinkedList, keeping the type the same '''

def min_value(self,temp_head):
        '''This method returns the minimum value stored in the doubly linked list.
        Parameter temp_head: the starting node
        Returns min_val: the minimum value stored'''

def is_ordered(self):
        '''This is a function to determine is an CircularDoublyLinkedList is 
        properly sorted.'''

def delete_copy(self):
        '''This method deletes a copy. '''

def stats(self):
        '''This method puts all of the stats used for plotting and data frames
        into one list.'''

Ordered Doubly Linked List:

def __init__(self):
        '''
        Creates a new ordered list that is empty. It needs no parameters and returns an empty list.
        '''

def add(self, item):
        '''
        Adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing. Assume the item is not already in the list.
        '''

def add_r(self,item):
        '''
        Adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing. Assume the item is not already in the list.
        '''

Word Predictor:

# ############################################################################
# Programmer: Josh Pickel
# Class: CptS 215, Fall 2019
# Programming Assignment #4
# 10/25/19
#
# Description: This program read in text files, parses the words to get their
#              Regular expression, and uses a Unigram probability model to 
#              predict a word given a prefix.
#
#
# NOTE: The HashTable and Map classes were adapted formGina Sprint's L8-2 
#       Lecture Notes. I also used https://stackoverflow.com/questions/3939361
#       /remove-specific-characters-from-a-string-in-python as a guide for
#       my regex stripping code. 
#  
#       COLLABORATION: Justin Pickel and I collaborated on the following:
# LinkedList to hadle collisions (discussed using LinkedLists)
# Node creation and attributes 
# Discussed what build function does - mapping objects to entries
# Parsing algorithm used in train()
# Size of HashTable
# Using unique hashfunction(provided by Gina)
# ###########################################################################

Hashtable Class:

class HashTable:
    '''
    This is a hashtable class. It uses a has function to determine what "bucket"
    the item should go in. Once the bucket is determined, a linked list is created 
    for the bucket. This is to handle collisions. NOTE: This class was adapted from
    Gina Sprint's Lecture L8-2 Notes.
    '''

def __init__(self, size=571):
        '''
        Constructor for the HashTable class. It creates size number of slots.
        '''

def put(self,item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise. This put method implements
        chaining via linked list if there are collisions.
        Parameter item: the Node which holds relevant data to put into hash table.
        Returns: The slot in which the Node was placed
        '''

def get(self,key):
        '''
        returns slot position if item in hashtable, if position exists,
        return it's node, -1 otherwise
        '''

def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, -1 otherwise
        '''

def hashfunction(self, item):
        '''
        This method is the hashfunction for the HashTable. It calculates what
        'bucket' the item should go in
        Parameter item: the item to be hashed
        Returns: the 'bucket' the item should go in 
        '''

def rehash(self, oldhash):
        '''
        Plus 1 rehash for linear probing. Did not use linear probing.
        '''

Map Class:

class Map(HashTable):
    '''
    This is an abstract version of a Dictionary. It maps key-value pairs. It is a child
    Class of the HashTable class. NOTE: This class was adapted formGina Sprint's 
    L8-2 Lecture notes.
    '''

def __init__(self, size=571):
        '''
        Constructor for the Map class. creates value attributes for size number of pairs
        '''

def __str__(self):
        '''
        Method to print the Map
        '''

def __len__(self):
        '''
        Return the number of key-value pairs stored in the map.
        '''

def __getitem__(self, key):
        '''
        This method will allow to get the value stored for any given key by
        using the [] characters.
        Parameter key: the item which you would like the value for
        Returns: The value associated with that item
        '''

def __setitem__(self, key, data):
        '''
        This method allows to set the value for any key using the [] characters.
        Parameters key,data: The key,data pair in which to store in the Map
        '''

def __delitem__(self, key):
        '''
        This function aloows to delete an item with the 'del' operator
        Parameter Key: the key in eich to delete
        '''

def __contains__(self, key):
        '''
        This funtion allows to do a membership check with the 'in' call
        Parameter key: The key in which to ask if Map contains
        Returns: Boolean value 
        '''

def put(self, key, value = 1):
        '''
        Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
        This method uses a linked lists to add items to the hashtable.
        Parameter key: The key in which is to be added to the Map
        Parameter value: the value in which to be sotred for the key
        '''

def get(self, key):
        '''
        This method returns the word associated with the given key.
        Parameter key: The word whose value to return
        Returns: The value associated to the word 
        '''

def remove(self, key):
        '''
        Removes key-value pair.
        Parameter key: The key which key value pair is to be removed
        Returns slot location if item in hashtable(LinkedList it is in), -1 otherwise
        '''

 def hashfunction(self, item):
        '''
        This method is the hashfunction for the HashTable. It calculates what
        'bucket' the item should go in
        Parameter item: the item to be hashed
        Returns: the 'bucket' the item should go in 
        '''
DictEntry Class:

def __init__(self,word,prob):
        '''Constructor for the DictEntry class.'''

def __str__(self):
        ''' This method is used to visualize the LinkedList(s)'''

def get_word(self):
        '''This method returns the word associated to the DictEntry '''

def get_prob(self):
        '''This method returns the probability of the word stored in the DictEntry '''

def match_pattern(self,pattern):
        ''' I did not need this function to correctly predict words given a prefix'''

WordPredictor Class:

class WordPredictor:
    '''This class creates Map objects for all words encountered, and a Map object
    for each word's prefixes, and the probable word given the prefix. It also
    is where the unigram probability is determined, as well as where the 
    training happens. '''


def __init__(self):
        '''The constructor for the WordPredictor class '''

def get_word_count(self,word):
        '''This method returns a specific word's count
        Parameter word: Thhe word in wich to count number of occurances
        Returns the number of times the word came up'''

def get_training_count(self):
        '''This method return the total number of words seen '''

def train(self,filename):
        '''This method parses all words seen, removing any characters that are not
        acceptable. It then will add the words to the Word_to_count Map object.
        Parameter gilename: The file in which to train on'''

def train_word(self,word):
        '''This method traind based on only one word given
        Parameter word: The word to add to the training set'''

def build(self):
        '''This method breaks each word in the Word_to_count Map object down into 
        all possible prefixes, and determines if the current word stored for the prefix 
        should be changed.'''

def get_best(self,prefix):
        '''This method returns the most probable word associated to the given prefix
        Parameter prefix: the prefix in which to predict the most probable word
        Returns: The word that is most probable given the prefix.'''
"""
Originally Created on Thu Mar 30 16:43:15 2017
Updated on Thur Oct 24 2017
@original_author: gsprint
updates_by: srinibadri
"""
import random
import string
import timeit


def random_load_test(wp):
    '''
    '''
    print("random load test: ")
    VALID = string.ascii_lowercase
    TEST_NUM = 10000
    hits = 0
    for i in range(TEST_NUM):
        prefix = ""
        for j in range(0, random.randint(1, 6), 1):
            prefix += VALID[random.randrange(0, len(VALID))]
        de = wp.get_best(prefix)
        if (de != None) and (de.get_word() != "null"):
            hits += 1

    print("Hit = %.2f%%" %(hits / TEST_NUM * 100))

def main():
    '''
    '''
    # train a model on the first bit of Moby Dick
    wp = WordPredictor()
    print("bad1 = %s" %wp.get_best("the"))
    wp.train("moby_start.txt")
    print("training words = %d" %(wp.get_training_count()))

    # try and crash things on bad input
    print("bad2 = %s" %wp.get_best("the"))
    wp.train("thisfiledoesnotexist.txt")
    print("training words = %d\n" %(wp.get_training_count()))

    words = ["the", "me", "zebra", "ishmael", "savage"]
    for word in words:
        print("count, %s = %d" %(word, wp.get_word_count(word)))
    wp.train("moby_end.txt")
    print()
    # check the counts again after training on the end of the book
    for word in words:
        print("count, %s = %d" %(word, wp.get_word_count(word)))
    print()

    # Get the object ready to start looking things up
    wp.build()

    # do some prefix loopups
    test = ["a", "ab", "b", "be", "t", "th", "archang"]
    for prefix in test:
        if (wp.get_best(prefix)):
            print("%s -> %s\t\t\t%.6f" %(prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("%s -> %s\t\t\t%s" %(prefix, "None", "None"))
    print("training words = %d\n" %(wp.get_training_count()))

    # add two individual words to the training data
    wp.train_word("beefeater")
    wp.train_word("BEEFEATER!")
    wp.train_word("Pneumonoultramicroscopicsilicovolcanoconiosis")

    # The change should have no effect for prefix lookup until we build()
    test_2 = ['b', 'pn']
    for prefix in test_2:
        if (wp.get_best(prefix)):
            print("before, %s -> %s\t\t%.6f" %(prefix, wp.get_best(prefix).get_word(),  wp.get_best(prefix).get_prob()))
        else:
            print("before, %s -> %s\t\t%s" %(prefix, "None",  "None"))
    wp.build()
    for prefix in test_2:
        if (wp.get_best(prefix)):
            print("after, %s -> %s\t\t%.6f" %(prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("after, %s -> %s\t\t%s" %(prefix, "None", "None"))
    print("training words = %d\n" %(wp.get_training_count()))

    # test out training on a big file, timing the training as well
    start = timeit.default_timer()
    wp.train("mobydick.txt")
    wp.build()
    for prefix in test:
        if (wp.get_best(prefix)):
            print("%s -> %s\t\t\t%.6f" %(prefix, wp.get_best(prefix).get_word(), wp.get_best(prefix).get_prob()))
        else:
            print("%s -> %s\t\t\t%s" %(prefix, "None", "None"))
    print("training words = %d\n" %(wp.get_training_count()))
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" %(elapsed))

    # test lookup using random prefixes between 1-6 characters
    start = timeit.default_timer()
    random_load_test(wp)
    stop = timeit.default_timer()
    elapsed = (stop - start)
    print("elapsed (s): %.6f" %(elapsed))

main()