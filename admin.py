from seats import *
print("Admin Page")
def movie_list():
    number_of_movies = int(input("Enter the number of movies to add: "))
    movies_list = []
    time_list = []
    for i in range(number_of_movies):
        movie_name = str(input("Enter the name of the movie: "))
        movie_time = str(input("Enter the time of the movie: "))
        movies_list.append(movie_name)
        time_list.append(movie_time)
        f = open( "movieSchedule.txt", "w+")
        for j in range(len(movies_list)):
            f.write(movies_list[j]+",")
            f.write(time_list[j]+",")
        f.close()
    print(movies_list)

    print(time_list)

    # return movie_list, time_list
  
movie_list()
