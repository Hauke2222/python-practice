import itertools

my_list_of_movies = ["movie1", "movie2", "movie3"]

my_list_of_actors = ["actor1", "actor2"]

for (movie, actor) in itertools.zip_longest(my_list_of_movies, my_list_of_actors):
    print(f"{movie} stars {actor}")