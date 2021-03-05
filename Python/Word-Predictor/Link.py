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
import random
import timeit
import sys
import time
#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
iMaxStackSize = 999999999
sys.setrecursionlimit(iMaxStackSize)


class Node:
    ''' This class Holds all the data for nodes, and houses the methods
    used for nodes'''

    def __init__(self,key,value):      # Constructor for node class, with attributes
        self.key = key                 # Key for the node
        self.value = value             # value for node
        self.next = None               # default for next and previous is None
        self.previous = None

        
    def __str__(self):
        ''' This method aloows one to visualize Maps '''
        return "{"+str(self.key) + ":" + str(self.value) +"}"

       

    def get_key(self):           # get_data method returns the data attribute for node
        '''This method returns the Node's data
        Returns: node's data'''
        return self.key
    
    def get_value(self):
        return self.value

   

    def get_next(self):           # get_next returns the next node
        '''This method returns the next node
        Returns: next node'''
        return self.next

   

    def get_previous(self):        # get_previous returns previous node
        '''This method returns the nodes previous.
        Returns: the  previous node'''
        return self.previous

   

    def set_value(self,new_val):   # set_data assigns data to the node
        '''This method assigns the nodes data attribute.
        Parameter new_data: The data for the node'''
        self.value = new_val

       

    def set_next(self,new_next):   # set_next sets the nodes next attribute
        '''This method sets the node's next pointer.
        Parameter new_next: The node the pointer is to be changed to'''
        self.next = new_next

   

    def set_prev(self,new_prev):   # set_prev sets the nodes previous attribute
        '''This methos sets the node's previous pointer.
        Parameter new_prev: The node the pointer is to be changed to'''
        self.previous = new_prev



class DoublyLinkedList:
    '''This clas is a class for LinkedList, houses necessary data and methods
    for the linked list.'''
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def __str__(self):
            '''
            This method allows to visualize the Linked List
            '''
            list_str = ""
            curr = self.head
            while curr is not None:
                list_str += str(curr)
                list_str += "->"
                curr = curr.get_next()
            list_str += "None"
            return list_str        

        

    def add_item(self,item):          # adds nodes to the LinkedList, at the
        '''This method adds an node to the front of the CircularDoublyLinkedList. This method
        assumes the item is not already in the list
        Parameter item: the item to be added to the LinkedList'''
        if self.is_Empty():           # If the Linked List is empty, add first node
            item.set_next(None)       # assign the nodes next
            item.set_prev(None)       # Set previous
            self.tail = item          # assign the tail
            self.head = item          # assign the head
            self.size += 1            # add to size attribute
        else:
            item.set_next(self.head)  # if not empty, add node and change pointers
            item.set_prev(None)
            #self.head.set_prev(temp)
            #self.tail.set_next(temp)
            self.head = item
            self.size += 1
        return
            
            
    def append(self,item):            # appends data to back of list
        '''This method will add an node to the back of the CircularDoublyLinkedList.This 
        method assumes the item is not already in the LinkedList
        Parameter item: the item to be added to the LinkedList'''
        if self.is_Empty():           # if empty linkedlist, add first node
            self.add_item(item)  

        else: 
            item.set_prev(self.tail)  # If not empty, add node and change pointers
            item.set_next(None)       # Set next
            self.tail.set_next(item)  # set tail's next
            self.tail = item          # Set tail
            self.size += 1            # Add to size attribute
            
    def insert(self, index, item):
        '''
        Adds a new item to the CircularDoublyLinkedList at position imdex. It needs the item and returns nothing. 
        Assume the item is not already in list.
        Parameter item: item to be added to linked list
        Parameter index: the position desired for the item to be added.
        '''
        if index == 0:                 # If index is 0, add to front of list
            self.add_item(item)
            
        elif index == self.size:      # If index is size, append it, adding to back
            self.append(item)

        else:                          # not adding at front or back. stop one before location
            curr = self.head
            i = 0
            while i < index - 1:
                curr = curr.get_next()
                i += 1
                if curr.get_next() is self.head:
                    break
            temp = Node(item)                # Change pointers to accomodate the change
            temp.set_next(curr.get_next())
            temp.set_prev(curr)
            curr.next.set_prev(temp)
            curr.set_next(temp)
            self.size += 1                  # Add to size attribute
            
            
            
       

    def is_Empty(self):               # Check to see if LinkedList is empty
        return self.head == None
    
    def pop(self, index = None):
        '''This method will return and remove the item at the given index. 
        Parameter index: the index in which you wish to pop. If no index passed, 
        method will pop the last item in the list.
        Returns: The item at the index being popped'''
        curr = self.head
        
        if index > self.size -1 or self.is_Empty():       # Check if index is valid
            raise Exception("The index passed was out of range, or the Linked List is empty")
        
        if index is None:                # Define index / argument
            index = self.size - 1
            
        if index == 0:                   # Case for index 0            
            if self.size == 1:           # If size is 1, handle case
                self.head = None 
                self.tail = None
                self.size -= 1 
            else:                                 # size was not 0
                self.head = self.head.get_next()  # Reassign head
                self.head.set_prev(None)          # Reassign head's prvious pointer
                self.tail.set_next(None)          # Reassign tail's next pointer
                self.size -= 1
        else:                                     # Else popping something in middle
            for i in range(index):                # Move curr up to index point
                curr = curr.next    
            curr.previous.set_next(curr.next)     # Reassign curr's previous next pointer
            curr.next.set_prev(curr.previous)     # Reassign currs next previous pointer
            self.size -= 1
            
        return curr.data
    
    
    def search(self, item):
        '''This method searches for an item in the CircularDoublyLinkedList, and
        returns the index.
        Parameter item: item to sesrch for
        Returns: index position of item, -1 if not in list'''
        curr = self.head                                # Start ar head
        loc = 0
        while curr.key != None and curr.key != item:  # While looking for something, and its not the item, move up
            if loc > self.size -1:
                return -1                               # Return -1 if not in LinkedList
            curr = curr.next
            loc += 1                                    # Index moved up
        return loc
    
    def remove(self,item):
        loc = self.search(item)
        curr = self.head
        if loc == -1:
            raise Exception("Item is not in the LinkedList")
        if loc == 0:
            self.head = self.head.get_next()  # Reassign head
            self.size -= 1
        else:
            for i in range(loc):                # Move curr up to index point
                curr = curr.next 
            self.size -= 1    
            curr.previous.set_next(curr.next)     # Reassign curr's previous next pointer
            if curr.next != None:
                curr.next.set_prev(curr.previous)
            #curr.previous.set_next(curr.next)     # Reassign curr's previous next pointer
            self.size -= 1
    
    def List_size(self):
        return self.size
    
    
    def make_copy(self):
        '''This function makes a copy of of a CircularDoublyLinkedList, keeping the type the same '''
        temp = self.head
        if type(self) == CircularDoublyLinkedList:           # Check type
            copy_list = CircularDoublyLinkedList()           # Make new LinkedList object of type
        else:
            copy_list = OrderedCircularDoublyLinkedList()    # Make OrderedLinkedList Object
        for i in range(self.size):             # For each node in LinkedList
            copy_list.append(temp.data)        # Add the data
            temp = temp.get_next()                     # Move up
        return copy_list
                    
                
    def min_value(self,temp_head):
        min_val = temp_head.data
        curr = temp_head.get_next()
        self.loop_assign += 1
        self.d_assign += 1
        while curr != self.head:
            self.comparisons += 1
            if curr.data < min_val:
                min_val = curr.data
                self.d_comparisons += 1
                self.d_assign += 1
            curr = curr.get_next()
            self.loop_assign += 1
        return min_val
                
    
        
    def is_ordered(self):
        '''This is a function to determine is an CircularDoublyLinkedList is 
        properly sorted.'''
        prev = self.head               # Start one pointer at head
        curr = self.head.get_next()    # Start another pointer one above head
        Flag = True
        for i in range(self.size-1):    # Loop through entire list
            if prev.data > curr.data:   # If something is out of order, return Fasle
                Flag = False
            else:
                prev = prev.get_next()  # Else, keep moving up
                curr = curr.get_next()
        return Flag
    
    def delete_copy(self):
        self.head = None
        self.tail = None
        
    def stats(self):
        '''This method puts all of the stats used for plotting and data frames
        into one list.'''
        self.tot_op = self.comparisons+self.d_comparisons+self.d_assign+self.loop_assign+self.other_op
        Stats = [self.time,self.d_comparisons, self.comparisons,self.d_assign,self.loop_assign,self.other_op,self.tot_op]
        return Stats
            
            
        
            

class OrderedDoublyLinkedList(DoublyLinkedList):
    def __init__(self):
        '''
        Creates a new ordered list that is empty. It needs no parameters and returns an empty list.
        '''
        self.head = None
        super().__init__()
        
        
    def add(self, item):
        '''
        Adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing. Assume the item is not already in the list.
        '''
        temp = Node(item)
        if self.is_Empty():           # If the Linked List is empty, add first node
            self.add_item(item)
            return
        #print(my)
        current = self.head
        previous = None
                
        stop = False
        while not stop:                   # Find where the item needs to go 
            if current.get_data() > item:
                stop = True
            else:
                previous = current
                current = current.get_next()

            if current == self.head:
                break
            
        if previous == None:              # If previous never reassigned, add the item
            self.add_item(item)
        
        else:                              # If it was reassigned, put it where 
            temp.set_prev(previous)        # It goes, reassign pointers around it
            temp.set_next(current)
            previous.set_next(temp)
            current.set_prev(temp)
            self.tail = self.head.get_previous()
            self.size += 1

            
    def add_r(self,item):
        '''
        Adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing. Assume the item is not already in the list.
        '''
        temp = Node(item)
        if self.is_Empty():           # If the Linked List is empty, add first node
            self.add_item(item)
            return
        current = self.head
        previous = None
        stop = False
        while not stop:                     # Find where the item needs to go 
            if current.get_data() < item:
                stop = True
            else:
                previous = current
                current = current.get_next()

            if current == self.head:
                break
            
        if previous == None:                # If previous never reassigned, add the item  
            self.add_item(item)         
        
        else:                               # If it was reassigned, put it where 
            temp.set_prev(previous)         # It goes, reassign pointers around it     
            temp.set_next(current)
            previous.set_next(temp)
            current.set_prev(temp)
            self.tail = self.head.get_previous()
            self.size += 1

