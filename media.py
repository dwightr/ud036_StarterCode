import webbrowser

class Video():
    def __init__(self, title):
        # Initialize Video Class Instance Variables 
        self.title = title

# This class provides a way to store movie related and inherits title from the Video class!!!
class Movie(Video):
    """This class provides a way to store movie related information!!!"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube_url):
        # Initialize Variables Inhertied From Video Class
        Video.__init__(self, title)
        # Initialize Movie Class Instance Variables
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # This Method Shows The Trailer Of The Instance It IS Called From
        webbrowser.open(self.trailer_youtube_url)
