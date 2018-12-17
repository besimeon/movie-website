import webbrowser


class Movie():
    """
    Movie class stores movie data.
    """
    def __init__(self, title, storyline, poster_image,
                 trailer):
        """
        Initialize the movie instance, using following inputs:
            title         : Title of movie
            storyline     : The storyline of movie
            poster_image  : The url to the movie poster image
            trailer       : The url to the youtube trailer for the movie
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        """
        opens a webbrowser window to display the youtube trailer
        """
        webbrowser.open(self.trailer)
