
# #################################################################################
# Programmer: Josh Pickel
# Class: CptS 215-01, Fall 2019
# Programming Assignment #1
# 9/7/19
#
# Description: This program takes in two files containing tweets and will sort each
#              of the files based on time, then merge both files based on time.Then 
#              it will return a file containing all of the merged tweets, with the 
#              most recent tweet appearing first.
# ##################################################################################



from Scanner import Scanner
import sys


def read_record(filename):
    '''This function will create an empty dictionary,create a scanner object
    of the file passed in, and will create a record fo each tweet. the record
    will contain the tweeter's name, the tweet, the year, month day and the time of the tweet.
    Parameter filename: the file to create a record of
    Returns: A list representation of the record.''' 
    recordList= []                                                      # Create empty list                                                                                              
    fileScan = Scanner(filename)                                        # Create scanner object from the file passed in
    for line in open(filename).readlines():                             # Loop through all the lines of the file
        record = create_record(fileScan)                                # Create a record through the create_record function
        recordList.append(record)                                       # Append result to empty list
    sortedList = sort_List(recordList)                                  # Call sort function to get list in order by date
    for i in range(len(sortedList)):                                    # Loop through the sorted list and convert int value to string values(for merge_and_sort_tweets)                                       
        for e in range(len(sortedList[i])):                    
            if type(sortedList[i][e]) != str:
                sortedList[i][e] = str(sortedList[i][e])
    return sortedList                                                   # Return the sorted list with int values converted to string
        
                                       
def sort_List(record):
    '''This function takes a list and sortes the list based on time(most recent first) 
    Parameter record: the list you wish to sort
    Returns: The list passed in sorted by time (most recent first)'''
    for i in range(-5,-1):                                              # Implemented from MIT press 3rd edition "introductions to algorithms" pg. 18
        for e in range(1,len(record)):
            key = record[e][-i]                                         # Set a key to look at time value
            j = e-1
            while j >= 0 and record[j][-i] < key:                       # While list needs sorting, sort it 
                temp = record[j+1]
                record[j+1] = record[j]
                record[j] = temp
                j -= 1
            record[j+1][-i] = key                                       # Once while loop breaks, reassign the key to check the rest fo the list
    return record                                                       # Return the sorted list
                
                
        
def create_record(ScanObj):
    '''This function will take on an scanner object, and create fields of 'name'
    (without '@' symbol) ,'tweet', 'year', 'month', 'day; and 'time' for the twitter 
    files passed in. 
    Parameter ScanObj: Scanner object of twitter file.
    Returns: a List of the file line broken into fields.'''
    createDict = {}                                                                      # Create an empty dictionary                                                  
    ScanObj.readchar()                                                                   # Remove the '@' symbol
    createDict[1] = {'name' : ScanObj.readtoken(), 'tweet' : ScanObj.readstring(),       # Add values for 'name', 'tweet', 'year', 'month', 'day' and 'time' keys
                     'year' : int(ScanObj.readtoken()), 'month': int(ScanObj.readtoken()),
                     'day' : int(ScanObj.readtoken()), 'time' : ScanObj.readtoken()}
    outputList = list(createDict[1].values())                                            # Convert dictionary into list
    return outputList                                                                    # Return list of tweet

def is_more_recent(record1, record2):
    ''' This function will take on two records of tweets ,and determine which of 
    them was most recent.
    Parameters record1, record2: a record of tweets
    Returns: Boolean value for record 1 happening before record 2''' 
    time1 = " ".join(record1[0][2:])
    time2 = " ".join(record2[0][2:])
    flag = True                                                                   # Start with boolean flag of True
    if time1 < time2:                                                             # Compare records' time 
        flag = False
    return flag                                                                   # Return result

def merge_and_sort_tweets(list1, list2):
    '''This function takes two records of tweets and will sort them, putting the most recent one first.
    Parameters record1, record2: the records containing the tweets
    Returns: A sorted list of tweets'''
    sorted_list = []                                                         # Create empty list
    record1 = [i for i in list1]
    record2 = [i for i in list2]
    while len(record1) + len(record2) > 0:
        record1len = len(record1)
        record2len = len(record2)        
        if record2len == 0 and record1len !=0:                               # If record2 has no records, append record1's first value
            sorted_list.append(" ".join(record1[0]))                         # Append to the list
            del(record1[0])
        elif record1len == 0 and record2len != 0:                            # If record1 has no records, append record2's first value
            sorted_list.append(" ".join(record2[0]))                         # Append to the list
            del(record2[0])                 
        else: 
            if is_more_recent(record1 ,record2):
                sorted_list.append(" ".join(record1[0]))                     # If first record is more recent, append it
                del(record1[0])                                              # Delete appended record from it's list
            else:
                sorted_list.append(" ".join(record2[0]))                     # If second record more recent, append it
                del(record2[0])                                              # Delete appended record form it's list 
    return sorted_list                                                       # return the list of ordered tweets


def write_records(merged_list):
    '''This function will take a sorted list of tweets and write them
    to a file, each tweet getting their own line.
    Parameter merged_list: The sorted list to write to a file
    Returns: nothing'''
    outfile = open(sys.argv[3], "w")                                      # Create a new file for sorted tweets to write to
    for i in merged_list:                                                 # Loop through each tweet in the sorted tweet list
        outfile.write(i +"\n")                                            # Write each tweet to the file
    outfile.close()                                                       # Close the file
    
def fivetweets(merged_list):
    '''This function takes a sorted list of tweets and will display only
    the first five tweets.
    Parameter merged_list: The merged list to get first five tweets
    Returns: Nothing, will print the tweets'''
    ScanObj = Scanner("")                                                  # Create scanner object
    for i in range(1,6):                                                   
        ScanObj.fromstring(merged_list[-i])                                # Scan the merged_list starting at the first entered tweet
        name = ScanObj.readtoken()                                         # Declare variable name as the first token
        tweet = ScanObj.readstring()                                       # Declare variable tweet as the first string
        print(name + " " +tweet)                                           # Print the name, a space, and the tweet that follows
        
        
def mosttweets(record1,record2):
    '''This function takes two records of tweets, and determines which one
    contained the most number of tweets.
    Parameters record1, record2: The tweet records to get the number of tweets from
    Returns: Nothing, result will be printed'''
    name1 = sys.argv[1]                                                         # Declare variable name1 as the first file input to the command promt
    name2 = sys.argv[2]                                                         # Declare variable name1 as the second file input to the command promt
    if len(record1) < len(record2):
        tweets = len(record2)                                                   # If record1 is shorter than record2, then the second file contained the most tweets
        print("%s file had the most tweets, with %i tweets" %(name2, tweets))
    elif len(record1) > len(record2):
        tweets = len(record1)
        print("%s file had the most tweets, with %i tweets" %(name1, tweets))   # If record1 is longer than record 2, then the first file contained the most tweets
    else:
        tweets = len(record1)                                                   # Otherwise, there was a tie
        print("%s and %s both contained %i tweets" %(name1,name2, tweets))
    




def main():
    print("Reading files...")
    tweetrecord1 = read_record(sys.argv[1])
    tweetrecord2 = read_record(sys.argv[2])
    mosttweets(tweetrecord1,tweetrecord2)
    print("Merging files...")
    merged_set = merge_and_sort_tweets(tweetrecord1,tweetrecord2)
    write_records(merged_set)
    print("Writing files...")
    print("Files written, displaying 5 earliest tweeters and tweets")
    fivetweets(merged_set)
    
main()
