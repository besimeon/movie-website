import media
import fresh_tomatoes

terminatorTwo = media.Movie(
    "Terminator 2",
    "The best in the Terminator series",
    "http://vignette3.wikia.nocookie.net/terminator/"
    "images/1/14/Terminator_2_poster.jpg",
    "https://www.youtube.com/watch?v=lwSysg9o7wE")

dumbAndDumber = media.Movie(
    "Dumb and Dumber",
    "A complete classic.  Full of nonstop comedy",
    "http://img.moviepostershop.com/dumb-and-dumber-"
    "movie-poster-1994-1020191993.jpg",
    "https://www.youtube.com/watch?v=MSu25pQ4iFw")

aboveTheLaw = media.Movie(
    "Above The Law",
    "Even though it is Segal's best movie, its still cheesy",
    "http://www.impawards.com/1988/posters/above_the_law.jpg",
    "https://www.youtube.com/watch?v=oiQi0WvS6Sc")

goodfellas = media.Movie(
    "Goodfellas",
    "My favorite mob movie",
    "https://images-na.ssl-images-amazon.com/images/I/51rOnIjLqzL.jpg",
    "https://www.youtube.com/watch?v=qo5jJpHtI1Y")

crocadileDundeeTwo = media.Movie(
    "Crocadile Dundee 2",
    "Don't judge please.  I actually enjoyed this movie.  Rico was hillarious",
    "https://upload.wikimedia.org/wikipedia/en/6/68/"
    "Crocodile_dundee_ii_ver2.jpg",
    "https://www.youtube.com/watch?v=oYaOhlHnuZw")

bigLebowski = media.Movie(
    "The Big Lebowski",
    "How could you forget to include this one in a list of classics?",
    "http://img.moviepostershop.com/the-big-lebowski-"
    "movie-poster-1998-1010475636.jpg",
    "https://www.youtube.com/watch?v=cd-go0oBF4Y")

# store instances in a list to pass to fresh_tomatoes.open_movies_page():
favoriteMovies = [
    terminatorTwo,
    dumbAndDumber,
    goodfellas,
    bigLebowski,
    aboveTheLaw]

# send the list to open_movies_page() function:
fresh_tomatoes.open_movies_page(favoriteMovies)
