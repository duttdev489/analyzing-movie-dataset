# --------------
from csv import reader


def explore_data(dataset, start, end, rows_and_columns=False):
    """Explore the elements of a list.
    
    Print the elements of a list starting from the index 'start'(included) upto the index 'end'         (excluded).
    
    Keyword arguments:
    dataset -- list of which we want to see the elements
    start -- index of the first element we want to see, this is included
    end -- index of the stopping element, this is excluded 
    rows_and_columns -- this parameter is optional while calling the function. It takes binary          values, either True or False. If true, print the dimension of the list, else dont.
    """
    print(dataset[start:end])
    #if rows_and_columns == True:

    
        
     


def duplicate_and_unique_movies(dataset, index_):
    """Check the duplicate and unique entries.
    
    We have nested list. This function checks if the rows in the list is unique or duplicated based     on the element at index 'index_'.
    It prints the Number of duplicate entries, along with some examples of duplicated entry.
    
    Keyword arguments:
    dataset -- two dimensional list which we want to explore
    index_ -- column index at which the element in each row would be checked for duplicacy 
    
    """
    print('index is' , index_)
    dict_col = { 'budget' :0 , 'genres' :1, 'id' :2, 'original_language':3, 'overview':4, 'popularity':5, 'production_countries':6, 'release_date':7, 'revenue':8, 'runtime':9, 'status':10, 'vote_average':11, 'vote_count':12, 'title_movies':13, 'Director' :14 
    }
    search_index=-1
    search_value =''
    row =-1
    dict_count ={}
    
    if index_ in dict_col.keys():
        search_index =dict_col[index_]
        print(search_index)
    else:
        print('provide valid index')
    for i  in range(0, len(dataset)):
        search_value=dataset[i] [search_index]
        #print(search_value)
        if search_value not in dict_count.keys():
            dict_count[search_value] =1
        else:
            dict_count[search_value] +=1

    duplicate_movies = 0
    print ('First 5 movies duplicated')
    for i,v in dict_count.items():
        if v>1 and duplicate_movies <=5 :
            print (i,':',v)
            
            duplicate_movies+=1




        



         
        



    


def movies_lang(dataset, index_, lang_):
    """Extract the movies of a particular language.
    
    Of all the movies available in all languages, this function extracts all the movies in a            particular laguage.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.

    Keyword arguments:
    dataset -- list containing the details of the movie
    index_ -- index which is to be compared for langauges
    lang_ -- desired language for which we want to filter out the movies
    
    Returns:
    movies_ -- list with details of the movies in selected language
    
    """
    movies_ =[]
    for i  in range(0,len(dataset)):
        if ( dataset[i][index_]=='en'):
            movies_.append(dataset[i])
    explore_data(movies_, 0, 5)


    return movies_
    



def rate_bucket(dataset, rate_low, rate_high):
    """Extract the movies within the specified ratings.
    
    This function extracts all the movies that has rating between rate_low and high_rate.
    Once you ahve extracted the movies, call the explore_data() to print first few rows.
    
    Keyword arguments:
    dataset -- list containing the details of the movie
    rate_low -- lower range of rating
    rate_high -- higher range of rating
    
    Returns:
    rated_movies -- list of the details of the movies with required ratings
    """
    rating = []
    for i in (range (0, len(movies))):
        rating.append(movies[i][11])
    #print( movies[0][11])
    print(max(rating) , min(rating))
    if(rate_high ==0 or rate_high ==None):
        rate_high =max(rating)

    rated_movies =[]
    index_ = 11
    #print(type (rate_low))
    #print(type (rate_high))


    for i  in range(0,len(dataset)):
        value = float(dataset[i][index_] )
        movie =(dataset[i][13] )

        if (value >= rate_low and value <= rate_high ):
            #rated_movies.append(dataset[i])
            rated_movies.append([movie,value])

    explore_data(rated_movies, 0, 5)



    
    return rated_movies




# Read the data file and store it as a list 'movies'
opened_file = open(path, encoding="utf8")
read_file = reader(opened_file)
movies = list(read_file)

#print(len(movies))
#print(type(movies[0] [11]))

# The first row is header. Extract and store it in 'movies_header'.
movies_header=movies[0]

print(movies_header)
# Subset the movies dataset such that the header is removed from the list and store it back in movies

movies = movies [1: ]




# Delete wrong data
del_mov =movies[4553:4554]
# Explore the row #4553. You will see that as apart from the id, description, status and title, no other information is available.
# Hence drop this row.
#print(del_mov)
del movies[4553]
#print(movies[4553])
#print(len(movies))

# Using explore_data() with appropriate parameters, view the details of the first 5 movies.
explore_data(movies, 0, 5)



# Our dataset might have more than one entry for a movie. Call duplicate_and_unique_movies() with index of the name to check the same.
duplicate_and_unique_movies(movies,'title_movies') 



# We saw that there are 3 movies for which the there are multiple entries. 
# Create a dictionary, 'reviews_max' that will have the name of the movie as key, and the maximum number of reviews as values.
reviews_max ={}
for i in range(0 ,len(movies)):
    value= movies[i][13]
    vote = movies[i][12]
    #print('value', value)
    #print('vote', vote)
    if value in reviews_max.keys():
        reviews_max[value] += vote
    else:
        reviews_max [value]= vote


        




# Create a list 'movies_clean', which will filter out the duplicate movies and contain the rows with maximum number of reviews for duplicate movies, as stored in 'review_max'. 
movies_clean=[]
for key,value in reviews_max.items():
    movies_clean.append([key,value])





# Calling movies_lang(), extract all the english movies and store it in movies_en.
movies_en=movies_lang(movies,3,'en')



# Call the rate_bucket function to see the movies with rating higher than 8.
high_rated_movies=rate_bucket(movies_en,8,10)


