__author__ = "Muhammed Mahir Varlioglu"
__email__ = "mmahirv@hotmail.com"
#Ask the user for 3 favorite movies.
#-Save them in a list.
#-Print:
#   -Full list
#   -First movie
#   -Last movie
#   -Number of movies
first_movie = input('Enter first movie name:')
second_movie = input('Enter second movie name:')
third_movie = input('Enter third movie name:')

movie_list = [first_movie,second_movie,third_movie]


print("Full List:")
for i in movie_list:
    if i != movie_list[-1]:
        print(i, end=' ')
    else:
        print(i)

print(f"First Movie: {movie_list[0]}")
print(f"Last Movie: {movie_list[-1]}")
print(f"Number of Movies: {len(movie_list)}")