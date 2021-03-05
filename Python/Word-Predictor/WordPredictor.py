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
from Link import DoublyLinkedList    # Import from linked list (And Node class) from previous assignment(modified to be DoublyLinked)
from Link import Node                          
import re
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
        self.size = size
        self.slots = [None] * self.size
        
    def put(self,item):
        '''
        Place an item in the hash table.
        Return slot number if successful, -1 otherwise. This put method implements
        chaining via linked list if there are collisions.
        Parameter item: the Node which holds relevant data to put into hash table.
        Returns: The slot in which the Node was placed
        '''
        hashvalue = self.hashfunction(item.key)                            # determine which bucket to put item in
        slot_placed = -1
        if self.slots[hashvalue] == None or self.slots[hashvalue] == item:  # If slot is empty, or has something in it
            self.slots[hashvalue] = DoublyLinkedList()                      # Create a linked list for the slot
            self.slots[hashvalue].append(item)                              # Use linked list append method (adds to back)
            slot_placed = hashvalue                                         # Declare which slot 
        else:
            self.slots[hashvalue].append(item)                              # Didn't need to create linked list, was already one. append item
            slot_placed = hashvalue
            
        return slot_placed
        
    def get(self,key):
        '''
        returns slot position if item in hashtable, if position exists,
        return it's node, -1 otherwise
        '''
        startslot = self.hashfunction(key)                       # find item's hash table bucket
        position = startslot
        if self.slots[position] == None or self.slots[position].is_Empty():   # If that item's buucket is empty, or Linked List is empty it is not in the hash table
            return -1
        else:
            curr = self.slots[position].head                      # Otherwise go though the linked list
            while curr.key != key and curr.get_next() != None:    # keep moving through linked list nodes until found
                curr = curr.get_next()
            if curr.key == key:
                return curr
            else:
                return -1
    
    def remove(self, item):
        '''
        Removes item.
        Returns slot position if item in hashtable, -1 otherwise
        '''
        slot = self.slots[self.hashfunction(item)]     # Get the key's LinkedList, if exists
        if slot != None:                               # Make sure there is linked list for given item
            slot.remove(item)                          # Remove the node(from linked list class)
        return slot

    def hashfunction(self, item):
        '''
        This method is the hashfunction for the HashTable. It calculates what
        'bucket' the item should go in
        Parameter item: the item to be hashed
        Returns: the 'bucket' the item should go in 
        '''
        return item.__hash__() % self.size
    

    def rehash(self, oldhash):
        '''
        Plus 1 rehash for linear probing. Did not use linear probing.
        '''
        return (oldhash + 1) % self.size


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
        super().__init__(size)
        self.values = [None] * self.size # holds values
        
    def __str__(self):
        '''
        Method to print the Map
        '''
        count = 0
        s = ""
        for slot in self.slots:
            if slot != None:
                node = slot.head
                if node == None:
                    s += "["+str(count)+"]"+"  Empty\n"
                else:
                    s += "["+str(self.hashfunction(node.get_key()))+"]"+ "--"
                    s += str(slot)+"\n"
                count += 1
        return s

    def __len__(self):
        '''
        Return the number of key-value pairs stored in the map.
        '''
        count = 0
        for values in self.values:          #  For each key-value pair    
            if values != None:
                count += values.List_size()  # count how long the linked list is
        return count
                
    
    def __getitem__(self, key):
        '''
        This method will allow to get the value stored for any given key by
        using the [] characters.
        Parameter key: the item which you would like the value for
        Returns: The value associated with that item
        '''
        return self.get(key)

    def __setitem__(self, key, data):
        '''
        This method allows to set the value for any key using the [] characters.
        Parameters key,data: The key,data pair in which to store in the Map
        '''
        self.put(key,data)
        
    def __delitem__(self, key):
        '''
        This function aloows to delete an item with the 'del' operator
        Parameter Key: the key in eich to delete
        '''
        self.remove(key)
        
    def __contains__(self, key):
        '''
        This funtion allows to do a membership check with the 'in' call
        Parameter key: The key in which to ask if Map contains
        Returns: Boolean value 
        '''
        return self.get(key) != None

            
    def put(self, key, value = 1):
        '''
        Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
        This method uses a linked lists to add items to the hashtable.
        Parameter key: The key in which is to be added to the Map
        Parameter value: the value in which to be sotred for the key
        '''
        item = Node(key,value)                            # Create a node holding the key and value pair   
        temp = super().get(key)                           # Determine if item has already been added
        if type(value) == DictEntry and temp != -1:
            temp.value = value                            # If item is a DictEntry, and already exists, change it's value
        elif temp != -1 and type(value) == int:
            temp.value += value                           # If item is not a DictEntry and already exists, change it's value accordingly
        else:
            slot = super().put(item)                      # Otherwise, add the new item 
            if slot != -1:
                self.values[slot] = self.slots[slot]      
        return
        
    def get(self, key):
        '''
        This method returns the word associated with the given key.
        Parameter key: The word whose value to return
        Returns: The value associated to the word 
        '''
        slot = super().get(key)                      # Get the slots type
        if type(slot) == Node:                       # If Node
            if type(slot.value) == int and type(slot.value) != -1: # If Node and Int
                return slot.value                    # Return int value
            elif type(slot.value)== DictEntry:       # Not int
                return slot.value              # Return word
        return None
    
    def remove(self, key):
        '''
        Removes key-value pair.
        Parameter key: The key which key value pair is to be removed
        Returns slot location if item in hashtable(LinkedList it is in), -1 otherwise
        '''
        slot = self.slots[self.hashfunction(key)]     # Get the key's LinkedList, if exists
        if slot != None:                              # Make sure there is linked list for given item
            slot.remove(key)                          # Remove the node(from linked list class)
        return slot

    def hashfunction(self, item):
        '''
        This method is the hashfunction for the HashTable. It calculates what
        'bucket' the item should go in
        Parameter item: the item to be hashed
        Returns: the 'bucket' the item should go in 
        '''
        return item.__hash__() % self.size
    
    
class DictEntry:
    '''This class stores an entry that keeps track of a word, and it's probability '''
    def __init__(self,word,prob):
        '''Constructor for the DictEntry class.'''
        self.word = word
        self.prob = prob
        
    def __str__(self):
        ''' This method is used to visualize the LinkedList(s)'''
        s = "" 
        s += str(self.get_word())
        s+= ":" 
        s+= str(self.get_prob())
        return s
    
        
    def get_word(self):
        '''This method returns the word associated to the DictEntry '''
        if self.word != None:     # If there is a word
            return self.word      # Return the word
    
    def get_prob(self):
        '''This method returns the probability of the word stored in the DictEntry '''
        if type(self) != DictEntry:  # If being asked for prob of non DictEntry
            return 0                 # Return 0
        else:
            return self.prob         # Return the probability
    
    def match_pattern(self,pattern):
        ''' I did not need this function to correctly predict words given a prefix'''
        pass
    
class WordPredictor:
    '''This class creates Map objects for all words encountered, and a Map object
    for each word's prefixes, and the probable word given the prefix. It also
    is where the unigram probability is determined, as well as where the 
    training happens. '''
    
    def __init__(self):
        '''The constructor for the WordPredictor class '''
        self.Prefix_to_entry = Map()               # Create Map object for Prefix_to_entry
        self.Word_to_count = Map()                 # Create Map object for Word_to_count 
        self.total = 0
 
    def get_word_count(self,word):
        '''This method returns a specific word's count
        Parameter word: Thhe word in wich to count number of occurances
        Returns the number of times the word came up'''
        if word in self.Word_to_count:            # See if word has been seen
            return self.Word_to_count[word]       # If so, return it's count
        else:
            return 0
    
    def get_training_count(self):
        '''This method return the total number of words seen '''
        return self.total

    def train(self,filename):
        '''This method parses all words seen, removing any characters that are not
        acceptable. It then will add the words to the Word_to_count Map object.
        Parameter gilename: The file in which to train on'''
        clean_words =[]                         # Array to hold parsed words
        try:                                    # Make sure the file is in the CWD, throw exception otherwise
            open(filename)
        except:
            print("Could no topen training file: %s" %(filename))
            return
        in_file = open(filename)                
        Words = in_file.read()                  # Read the file
        Words = Words.split()                   # Split the words
        for i in Words:                         # Go through words
            i = i.lower()                       # Make each word lowercase
            i = re.sub("[^a-zA-Z']+", "", i)    # Use regex to remove unecessary words (adapted from https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python)
            i = i.strip()                       # Strip                                       
            clean_words.append(i)               # Add the stripped version to clean word array
        for i in clean_words:                   # Go through the words in clean words array and put them in the Word_to_count Map object
            self.Word_to_count.put(i) 
            self.total += 1                     # Increase total word count for each word in clean_words array
           
 
    def train_word(self,word):
        '''This method traind based on only one word given
        Parameter word: The word to add to the training set'''
        clean_word = []                             # Array to hold stripped word
        word = word.lower()                         # Convert to lowercase
        word = re.sub("[^a-zA-Z']+", "", word)      # Use Regex (adapted from https://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python)
        word = word.strip()                         # Strip the word
        clean_word.append(word)                     # Add stripped version to the clean word array
        self.Word_to_count.put(word)                # Put word into Word_to_count Map
        self.total += 1                             # Add to our total words seen
        
 
    def build(self):
        '''This method breaks each word in the Word_to_count Map object down into 
        all possible prefixes, and determines if the current word stored for the prefix 
        should be changed.'''
        for values in self.Word_to_count.values:                       # Go through all words in the Word_to_vount Map object
            if values != None:
                curr = values.head
                while(curr != None):                                   # While not on empty Linked List
                    string = curr.key                                  # String is current word
                    count = curr.value
                    key = DictEntry(string,curr.value/self.total)      # Make a DictEntry for current word
                    for i in range(1,len(string)+1):                   # Go through all possible prefixes
                        strings = string[0:i]
                        if self.Prefix_to_entry[strings] == None:      # If Prefix_to_entry Map object does not have this prefix
                            self.Prefix_to_entry[strings] = key        # Add ot with DictEntry for the word
                        else:                                          # Prefix is already in Prefix_to_entry Map object
                            temp = DictEntry(string,curr.value/self.total)   # Make a temporary DictEntry for current word
                            if self.Prefix_to_entry[strings].get_prob() < temp.prob:   # if stored word unigram probability < curent word probability
                                self.Prefix_to_entry[strings] = temp                   #  Reassign stored word to current word (new word is now more probable)
                    curr = curr.get_next()                                   # Keep moving through linked list
                    
                    
    def get_best(self,prefix):
        '''This method returns the most probable word associated to the given prefix
        Parameter prefix: the prefix in which to predict the most probable word
        Returns: The word that is most probable given the prefix.'''
        if prefix in self.Prefix_to_entry:
            return self.Prefix_to_entry[prefix]

       

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