
import re

movie_title = "Sanctuary (221)"  # Replace with your actual movie title

Name = r'^[^\(\)]+\s\(\d{4}\)$'
movie_match = re.match(Name, movie_title)

if movie_match:
    print(movie_match.group(0))
else:
    print("The movie title does not match the pattern.")
