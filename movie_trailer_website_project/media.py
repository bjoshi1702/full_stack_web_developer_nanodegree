# Movie class with required arguments
class Movie():
    """ Movie class takes information which suppose to show on website

        Attributes:
        
        movie_title (str): give name of the movie
        movie_storyline (str): give storyline of the movie
        poster_image (str): provide link for movie poster
        trailer_youtube (str): provide youtube movie trailer link
        
    """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    

        
