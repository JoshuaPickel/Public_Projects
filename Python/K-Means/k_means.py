# ############################################################################
# Author: Josh Pickel
# Date: 9/29/19
# Assignment: Programming Assignment 2
# Course: CPTS 215, Fall 2019
# Description: This program is a k-means algorithm designed to cluster breast
# cancer patients based on their genome sequences. The program will prompt
# the user for a file path and number of clusters, and perform the k-means 
# algorithm on the provided data in the file. It will then plot the results
# as a heatmap to visualize any differences between the clusters.
# ###########################################################################




import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from math import*
import random
import sys


class K_means:
    '''A class used to create a k means object, with methods to run the k-means
        algorithm.
        def __init__(self,k): k-means constructor that produces k clusters
        def random_data(self,dataSet): method that creates random clusters
        def calculate_centroid(self): method to produce centroid for each cluster
        def distances(self,cluster): calculates each smaples distance from eahc cluster
        def shift(self): reassigns cluster members to closest cluster by centroid distance
        def get_members(self): gathers each clusters members
        '''
    def __init__(self,k, dataSet):
        ''' connstructor that creates k number of clusters
        Parameter k: number of clusters to produce'''
        self.k = k               
        self.cluster_set = []                     # create an empty clutser array
        self.df1 = None       
        self.dataSet = pd.read_csv(dataSet, index_col = 0, header = None)
        for i in range(k):                        # Loop k number of times
            cluster = clusters()                  # make a cluster object
            self.cluster_set.append(cluster)      # Append cluster object to cluster_set array    
            
            
    def random_data(self):
        '''Method that assigns each sample to a random cluster '''
        dataSet1 = self.dataSet                                                 # Alias DataSet   
        for i in range(self.k):                                                 # Loop k number of times
            data_subset = dataSet1.sample()                                     # Get a sample from the data set alias
            index = list(data_subset.index)                                     # Put sample in a list
            df_subset1 = list(dataSet1.loc[index[0]])                           # Get the numerical value of the sample
            self.cluster_set[i].append_data(df_subset1)                         # append it to cluster "i" (this ensure each cluster will not be empty)
            dataSet1 = dataSet1.drop(data_subset.index)                         # remove sample from data set alias so no repeats happen    
            
        for i in range(len(dataSet1)):                                          # Now go through remaming samples
            e = random.randint(0,self.k-1)                                      # Pick a random cluster 
            self.cluster_set[e].append_data(list(dataSet1.iloc[i]))             # Put sample data into appropriate cluster 
           
        
    def calculate_centroid(self):
        '''This function calculates the centroid for each cluster
        Returns: centroid list'''
        self.centroids = []                                                    # Create empty centroid list 
        for i in self.cluster_set:                                             # Loop through each cluster
            centroid = pd.DataFrame(i.members).mean()                          # Centroid's attribute value is the average of each cluster's attributes
            i.centroid = centroid                                              # Declare centroid attribute for each cluster
            self.centroids.append(i.centroid)                                  # Append centroid to centroid list  
                                                      # Return the centroid
        
    
    def distances(self,cluster):
        ''' This function calculates each samples distance from the given cluster
        Parameter cluster: The cluster to calculate the distance from '''
        self.distance = []                                                     # Array of distances
        for i in range(len(self.cluster_set)):                                 # Loop through each cluster 
            difference =(self.centroids[i] - cluster)**2                       # Calculate the distance from centroid to cluster samples 
            Euclidean = sqrt(sum(difference))                                  # take swaure root of difference 
            self.distance.append(Euclidean)                                    # Append the difference to difference list
        return self.distance                                                   # Return the distance array 
    
    
    
    def shift(self):
        '''This function will calculate the distance of each sample to each cluster's
        centroid,and move the sample into the cluster in which it is closest to'''
        after = []                                                             # Array to compare before shift and after shit 
        Flag = True
        while(Flag == True):
            before = self.get_members()                                        # Create an object in which to campe before/after shift members
            for i in range(len(self.cluster_set)):                             # Loop through each cluster 
                for e in self.cluster_set[i].members:                          # Loop through each cluster's members 
                    distance_array = self.distances(e)                         # Create an array of distances through distance function
                    closest_index = distance_array.index(min(distance_array))  # Calculate which cluster is the closest
                    if closest_index != i:                                     # Move the sample if it needs to be moved 
                        self.cluster_set[closest_index].append_data(e)         # move the sample to the appropriate cluster   
                        self.cluster_set[i].remove_data(e)                     # remove sample from current cluster, after it has been moved 
            self.calculate_centroid()                                          # After all necessary moves, recalculate centroids based on new cluster sets
            after = self.get_members()                                         # After array now hold the current cluster members 
            if after == before:                                                # Check to see if clusters changed 
                Flag = False
            else:
                Flag = True
                
    def get_members(self):
        '''This function appends gets each clusters members
        Returns: array of members for each cluster'''
        final_membs = []
        for i in self.cluster_set:                                             # Go through cluster set
            final_membs.extend(i.members)                                      # Put all the members in an array
        return final_membs
            
        
    def plot(self):
        '''This method will plot the end K-means data after shfting is complete
        in the for of a heatmap.'''
        data_array = []                                                        # Creats an empty array to hold the data to be plotted in a heatmap
        for i in self.cluster_set:                                             # Loop through each cluster
            data_array.extend(i.members)                                       # Extend each cluster's members' to the data array   
        graph = plt.subplot()                                                  # Create a graph 
        plt.pcolor(data_array, cmap = 'seismic')                               # Plot the data array, with color 'seismic' 
        graph.axes.get_xaxis().set_visible(False)                              # Format the x axis
        graph.axes.get_yaxis().set_visible(False)                              # Format y axis
        plt.colorbar()
        length = 0
        for i in self.cluster_set:
            length += len(i.members)
            if length != len(self.dataSet):
                plt.axhline(y = length, c = 'forestgreen', lw = 3.0)                 # Put lines on the heatmap
        plt.show()
    
    def insight(self):
        '''This function determines how many nonrecurring and recurring samples
        are in each cluster after re assignment convergence
        Returns: a touple for each cluster, representing number of non recurring
        samples for index 0, and recurring in index 1'''
        insights = []                                                            # Empty array
        count = 0
        insight_frame = self.dataSet                                             # Create dataFrame for original data set
        insight_frame = insight_frame.sort_index()                               # sort the insight frame by col index (sorts by recur and non recur)
        patient_type = insight_frame.index                                       # Create list of sorted patient type
        for i in range(len(patient_type)):                                       # loop through patient list
            if 'non' in patient_type[i]:                                         # Count number of non recurring patients
                count += 1
        nons = pd.DataFrame(insight_frame.iloc[0:count])                         # Create data frame of non recurring samples  
        has = pd.DataFrame(insight_frame.iloc[count:])                           # Create data frame of recurring samples   
        for i in self.cluster_set:                                               # Loop through the clusters, and their samples 
            count_non = 0
            count_recur = 0
            for e in range(len(i.members)):   
                cluster_df = pd.DataFrame(i.members)                            # Create a dataframe of the cluster samples
                mem_list = cluster_df.iloc[e].tolist()                          # create list of the members
                num_nons = nons.eq(mem_list,axis = 1).all(1)                    # Find in nons
                num_recur = has.eq(mem_list,axis = 1).all(1)                    # Find in recurs
                count_non += sum(num_nons)                                      # Add the nons
                count_recur += sum(num_recur)                                   # Add the recurs
                counts = (count_non,count_recur)                                # Put totals in tuple
            insights.append(counts)                                             # Append tuple to insight array
        return insights                                                         # Return insight array 
        
        
class clusters(K_means):
    ''' A class that cretes clusters to be stored in K-means members cluster array
    This class is a child of the K-means class
    def __init__(self): creats an empty member array, and gives each cluster a centroid attribute
    def append_data__(self,sample): method to append data to the member array
    def remove_data(self,sample): method to remove data from the member array'''
    def __init__(self):
        ''' Constructor for the clusters class'''
        self.members = []                                                      # Create empty member array 
        self.centroid = None                                                   # Create centroid attribute
        self.distance = None 
        
    def append_data(self,sample):
        '''This method allows one to append data to the member array
        Parameter sample: the data to append to member array'''
        self.sample = sample
        self.members.append(self.sample)
        
    def remove_data(self,index):
        '''This method allows one to remove data from the member array 
        Parameter index: the index in which to remove from the member array'''
        self.index = index 
        self.members.remove(self.index)
        
        
def main():
    while True:   # Continue to grun program
        user_file = False  # Set flag to false
        while user_file == False: # Continue to get file input until valid path
            print("Please enter 'q' when promted for the file name to end the program\n")
            file = input("Please enter the name of the file to perform k-means on. ") 
            print("\n")
            if file.lower() == 'q': # Check for exit
                sys.exit()
            else:                   # check for valid file path
                try:
                    open(file, "r")
                    user_file = True
                except:              # inform user of invalid path
                    print(user_file)
                    print("Invalid file path provided, please enter a valid file path.")
                    print("\n")
               
        user_k = False  # Set flag to false
        while user_k == False: # Continue to get k from user until valid value
            k = input("Please enter the number of clusters you want the algorithm to use: ")
            print("\n")
            try:             # Run program if valid k
                k = int(k)
                user_k = True
                k = int(k)
                run = K_means(k, file)
                run.random_data()
                run.calculate_centroid()
                run.shift()
                run.plot()
                run.insight()                
            except:              # inform user of invalid k value
                print("Please enter a valid whole number for K Value")
                print("\n")
main()
