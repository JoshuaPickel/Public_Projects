# #################################################################################
# Programmer: Josh Pickel
# Class: CptS 215-01, Fall 2019
# Programming Assignment #1
# 9/7/19
#
# Description: This program takes in two files containing tweets and will sort each
#              of the files based on time, then merge both files based on time. Then 
#              it will return a file containing all of the merged tweets, with the 
#              most recent tweet appearing first.
# ##################################################################################


Functions:

def read_record(filename):
    '''This function will create an empty dictionary,create a scanner object
    of the file passed in, and will create a record fo each tweet. the record
    will contain the tweeter's name, the tweet, the year, month day and the time of the tweet.
    Parameter filename: the file to create a record of
    Returns: A list representation of the record.''' 

def sort_List(record):
    '''This function takes a list and sortes the list based on time(most recent first) 
    Parameter record: the list you wish to sort
    Returns: The list passed in sorted by time (most recent first)'''

def create_record(ScanObj):
    '''This function will take on an scanner object, and create fields of 'name'
    (without '@' symbol) ,'tweet', 'year', 'month', 'day; and 'time' for the twitter 
    files passed in. 
    Parameter ScanObj: Scanner object of twitter file.
    Returns: a List of the file line broken into fields.'''

def is_more_recent(record1, record2):
    ''' This function will take on two records of tweets ,and determine which of 
    them was most recent.
    Parameters record1, record2: a record of tweets
    Returns: Boolean value for record 1 happening before record 2''' 

def merge_and_sort_tweets(list1, list2):
    '''This function takes two records of tweets and will sort them, putting the most recent one first.
    Parameters record1, record2: the records containing the tweets
    Returns: A sorted list of tweets'''

def write_records(merged_list):
    '''This function will take a sorted list of tweets and write them
    to a file, each tweet getting their own line.
    Parameter merged_list: The sorted list to write to a file
    Returns: nothing'''

def fivetweets(merged_list):
    '''This function takes a sorted list of tweets and will display only
    the first five tweets.
    Parameter merged_list: The merged list to get first five tweets
    Returns: Nothing, will print the tweets'''

def mosttweets(record1,record2):
    '''This function takes two records of tweets, and determines which one
    contained the most number of tweets.
    Parameters record1, record2: The tweet records to get the number of tweets from
    Returns: Nothing, result will be printed'''

