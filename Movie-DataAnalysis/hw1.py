
# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

import collections
import math
from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    name = str(f)
    file = open(name,'r')
    for line in file:
        msg = line
        msg = msg.split("|")
        #print(msg)
        dict[msg[0]].append(msg[1])
        
    return dict
        

    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    name = str(f)
    file = open(name,'r')
    for line in file:
        msg = line
        msg = msg.split("|")
        dict[msg[2].rstrip()] = msg[0]
    return dict

# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    for key in d:
        dict[d[key]].append(key)

    #print(dict)
    return dict



    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    for key in d:
        sum = 0
        counter = 0
        for item in d[key]:
            sum+=float(item)
            counter+=1
        avg = sum/counter
        dict[key] = avg
        
    return dict


    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
   # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    dict = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    if len(dict) > n:
        while len(dict) != n:
            dict.pop()
    return dict


    
# 3.2
def filter_movies(d, thres_rating=3):
 # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    for items in d:
        if d[items] >= thres_rating:
            dict[items] = d[items]
    return dict


    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
 # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    #creates empty list
    dict = defaultdict(list)
    #scans values of genre_to_movies[key/genre]
    #creates dict[key] item and populates it with values at genre
    for items in genre_to_movies[genre]:
        dict[items] = movie_to_average_rating[items]
    #sorts resulting list by popular movies
    dict = get_popular_movies(dict, n)
    return dict
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
 # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    sum = 0
    counter = 0
    for items in genre_to_movies[genre]:
        # print(items)
        # print(movie_to_average_rating[items])
        sum += movie_to_average_rating[items]
        counter+=1
    avg = sum/counter
    return avg


    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
# parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    # print(genre_to_movies)
    # print("\n")
    # print(movie_to_average_rating)
    for items in genre_to_movies:
        ans = get_genre_rating(items, genre_to_movies, movie_to_average_rating)
        # print(items)
        # print(ans)
        dict[items] = ans
        
    dict = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    if len(dict) > n:
        while len(dict) != n:
            dict.pop()
    return dict



# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
# parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to movies and ratings
    # WRITE YOUR CODE BELOW
    dict = defaultdict(list)
    name = str(f)
    file = open(name,'r')
    for line in file:
        msg = line.split("|")
        a = msg[0]
        b = msg[1]
        c = msg[2].rstrip()
        dict[c].append(a)
        dict[c].append(b)

    return dict

    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
  # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    userid = str(user_id)
    work = defaultdict(list)
    currword = ""
    for items in user_to_movies[userid]:
        try:
            float(items)
            work[currword] = float(items)
        except:
            currword = items
    
    dict1 = defaultdict(list)
    dict2 = defaultdict(list)


    for items in work:
        a = items                     #movie
        b = movie_to_genre[items]     #genre
        c = work[items]               #rating
        # print(a)
        # print(b)
        # print(c)
        if b in dict1:
            temp = dict1[b]
            ans = temp + c
            dict1[b] = ans
            dict2[b] += 1
        else:
            dict1[b] = c
            dict2[b] = 1 
    # print(dict1)
    # print("\n")
    # print(dict2)
    for items in dict1:
        temp1 = dict1[items]
        temp2 = dict2[items]
        avg = temp1/temp2
        dict1[items] = avg

   
    max = 0.0
    for items in dict1:
        work = dict1[items]
        if work > max:
            max = work
        
    string = ""
    counter = 0
    for items in dict1:
        if dict1[items] == max:
            if counter > 0:
                string += "."
            string += items
            counter+=1

    return(string)

        
        
        
        
        

        
        
    


    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
# parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    userid = str(user_id)
    repo = defaultdict(list)

    # print(user_to_movies)
    # print("\n")
    # print(movie_to_genre)
    # print("\n")
    # print(movie_to_average_rating)
    topgenre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    #print("Topgenre = "+topgenre)
    target = "."
    if target in topgenre:
        string = topgenre.split(".")
        counter = 0
        while counter != len(string):
            for items in movie_to_genre:
                if movie_to_genre[items] == string[counter]:
                    repo[movie_to_genre[items]].append(items)
            counter+=1

    else:
        for items in movie_to_genre:
            if movie_to_genre[items] == topgenre:
                repo[movie_to_genre[items]].append(items)
    
    # print(user_to_movies[userid])
    # print("\n")
    # print(repo)
    for items in repo:
        #print(items)
        for keys in repo[items]:
            
            #print(keys)



# -------- main function for your testing -----
if __name__ == "__main__":

    #test for 3.3
    # genredict = read_movie_genre("movie.txt")
    # ratingsdict = read_ratings_data("rating.txt")
    # dict1 = create_genre_dict(genredict)
    # dict2 = calculate_average_rating(ratingsdict)
    # dict3 = get_popular_in_genre("Comedy", dict1, dict2)
    # print(dict3)
    #test for 3.3

    #test for 3.4
    # genredict = read_movie_genre("movie.txt")
    # ratingsdict = read_ratings_data("rating.txt")
    # dict1 = create_genre_dict(genredict)
    # dict2 = calculate_average_rating(ratingsdict)
    # ans = get_genre_rating("Comedy", dict1, dict2)
    # print(ans)
    #test for 3.4

    #test for 3.5
    # genredict = read_movie_genre("movie.txt")
    # ratingsdict = read_ratings_data("rating.txt")
    # dict1 = create_genre_dict(genredict)
    # dict2 = calculate_average_rating(ratingsdict)
    # ans = genre_popularity(dict1, dict2, 5)
    # print(ans)
    #test for 3.5

    #test for 4.1
    # dict1 = read_user_ratings("rating.txt")
    # print(dict1)
    #test for 4.1

    #test for 4.2
    # userTOmovies = read_user_ratings("rating.txt")
    # movieTOgenre = read_movie_genre("movie.txt")
    # dict1 = get_user_genre(25, userTOmovies, movieTOgenre)
    #test for 4.2

    #test for 4.3
    dict1 = read_user_ratings("rating.txt")
    dict2 = read_movie_genre("movie.txt")
    temp = read_ratings_data("rating.txt")
    dict3 = calculate_average_rating(temp)
    recommend_movies(1,dict1,dict2,dict3)

    #test for 4.3

    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions

    
# program will start at the following main() function call
# when you execute hw1.py


    

