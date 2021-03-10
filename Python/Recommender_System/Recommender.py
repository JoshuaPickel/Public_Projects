# ############################################################################
# Author: Josh Pickel
# Date: 10/19/20
# Assignment: Programming Assignment 2
# Course: CPTS 315, Fall 2020
# Description: This program is an item-item collaborative filtering recommender 
# system. The program is designed to recommend movies to a user based on their
# ratings for other movies. The program uses cosine similarity to find the 
# similarity of users.
# ###########################################################################



import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity



def readRatingFile(file):
    '''This function reads in a file, converts it into a pandas Data Frame
    with the index being movieId, columns being userId and the values being 
    ratings. It then subtracts each rows mean from itself.
    Parameters: 
    file: the file in which to process the data
    Returns:
    movies: a pandas data frame consisting of each movie, it's rating per user 
    moviesCentered: a pandas data frame consisting of each movie and it's rating
    per user after subtracting the movie mean.'''
    print("\nCleaning %s and converting to centered and non-centered data frames....." %(file))  
    # Read in the file as a csv
    df = pd.read_csv(file) 
    # Pivot that data frame to get all user ratings per movie
    movies = df.pivot(index = 'movieId',columns = 'userId', values = 'rating') 
    # Subtract row mean from it's own row
    means = movies.mean(axis = 1)
    # Make a new data frame which is the centered data frame
    moviesCentered = movies.sub(means, axis = 0)
    # Fill the Na values for the centered data frame
    moviesCentered = moviesCentered.fillna(0)
    print("Files cleaned and data frames made.")
    return movies, moviesCentered

def readMovies(file,idCol,titleCol):
    '''This function makes a dictionairy holding the key:value pairs for 
    movieID and title. 
    Parameters:
    file: the file containing movieID and movie title
    idCol: String name of movie ID column in the csv file
    titleCol: String name of the movie title in the csv file
    Returns:
    movieTitle: dictionary holding movie:title pairs.'''
    # Read in the csv file
    df = pd.read_csv(file)
    # Get only movieID and title
    df = df[[idCol,titleCol]]
    # Convert data frame to dictionary
    movieTitle = df.set_index(idCol)[titleCol].to_dict()
    # Return the dictionary
    return movieTitle

def similarity(df):
    '''This function calculates the pearson coefficient correlation for all rows
    in the data frame, using the Scikit-learn library.'
    Parameters:
    df: the data frame in which to compute the pearson correlation coefficient for
    Returns:
    sims: Data Frame holding pearson correlation coefficient scores.
    '''
    print("\nCreating cosine similarity matrix for data.....")
    # Get list of movie Id's
    names = sorted(df.index.unique())
    # Convert proived Data Frame into numpy array
    nump = df.to_numpy()
    # Compute pearson correlation coefficients
    scores = cosine_similarity(nump)
    # Convert results into data Frame
    sims = pd.DataFrame(scores,index = names, columns = names)
    print("Similarity matrix made.")
    return sims

def estimate(neighbors, df, sims):
    '''This function predicts movie ratings for each movie the user does not
    have a rating for. It gets the neighbor set for each movie, grabs the data
    for the neighbor set for each user, and calculates the predicted value
    for missing movie ratings per user.
    Parameters:
    neighbors: the number of neighbors to be used for the nieghbor set
    df: data frame containing user-movie rating data
    sims: data frame containing similarity scores across all movies
    Returns:
    prediction: data frame containing predicted movie ratings for each user'''
    print("\nMaking predictions for unrated movies by user.....")
    # Create empty dictionary to store prediction values
    predict_dict = {}
    # Loop through each movie Id
    for movie in list(df.index):
        # Get the neighbor set for the movie, excluding the movie itself
        simsData = sims[movie].sort_values(ascending= False).drop(movie).head(neighbors)
        # Create a data frame containing users who need predicted rating for movie,
        # with the data of the nieghbor set excluding users who have missing values
        # for all neigbor set movies (those will be considered 0)
        frame = df[df.loc[movie].index[df.loc[movie].isna() == True]].loc[simsData.index]
        # Calulate the predicted value for users that are missing a rating for the movie
        ratings = frame.multiply(simsData, axis = 0).sum(axis = 0)/simsData.sum()
        # Convert rating series to dictionary
        ratings = ratings.to_dict()
        # Store user predictions for the movie
        predict_dict[movie] = ratings
    # Convert movie-user prediction dictionary to data frame, transpose it
    prediction = pd.DataFrame(predict_dict).T.round(4)
    print("Predictions made")
    return prediction

def writeResults(outFile, results, movieDict):
    '''This function writes the top 5 movie prediction values for each user
    to a file. It goes through the prediction data frame users and gets the 
    top 5 movie Id's based on prediction scores, then writes each user's top 5
    prediction scores to the file.
    Parameters:
    outFile: the file name to write results to
    results: data frame containing prediction results
    movieDict: dictionary holding movieId:title pairs'''
    print("\nReturning top 5 predictions per user, writing results to %s ....." %(outFile))
    # Create a new file to write results to
    file = open(outFile, 'w')
    # Loop through users in the prediction data frame
    for users in sorted(results.columns):
        # Get the top 5 movie Id's for the user based on prediction value
        userData = results[users].dropna().to_dict()
        # Sort an break ties
        userData = {k:v for k,v in sorted(userData.items(), key = lambda item: (item[1],item[0]), reverse = False) }
        # Sort again so order is descending based on movieId w.r.t prediction score
        userData = {k:v for k,v in sorted(userData.items(), key = lambda item: item[1], reverse = True) }
        # Convert Id's to titles
        strings = [movieDict[x] + ',' for x in userData.keys()][0:5]
        # Create string for 'userId' + top 5 prediction movieId's
        toWrite = str(users)+ ' ' + ' '.join(strings)[0:-1]
        # Write the 'userId-movieId1-movieId2....movieId5' string to file w/ newline after each user
        file.write( toWrite + '\n')
    # Close the file
    file.close()
    print("The results have been written to %s" %(outFile))
    return
        

def main():
    # Get input from user for file to make movie recommendations for
    inputFile = input('Please enter the file name you wish to make movie recommendations for: ')
    # Get input from user for movieID/movie Title
    titleInput = input("Please enter the file name containing the movieID and Movie titles: ")
    # Get user input for name of movieID column
    idCol = input("Please enter the name of the movieID column in the file containing movieID and title: ")
    # Get user input for the name of title column
    titleCol = input("Please enter the name of the title column in the file containing movieID and title: ")
    # Get input from user for file to write results to
    outputFile = input('Please enter the name of the file you wish for the output to be written to: ')
    # Get input from user for the cardinality of neighbor set
    neighborCardinality = int(input('Please enter the desired neighbor set cardinalty value: '))
    # Clean the file, make appropriate data frames using user input
    movieData,centeredData = readRatingFile(inputFile)
    # Make Dictionary for movieID:title 
    movieTitle = readMovies(titleInput, idCol, titleCol)
    # Create similarity data frame using result from above call
    sims = pd.DataFrame(cosine_similarity(centeredData), index =  centeredData.index.tolist(), columns = centeredData.index.tolist())
    # Make result data frame using user input/results from above call
    results = estimate(neighborCardinality, movieData, sims)
    # Write the results using user input/results from above call
    writeResults(outputFile,results, movieTitle)
main()