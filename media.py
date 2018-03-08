import webbrowser


class Video():
    """
        Video Class provides a way to store
        video related information
    """
    def __init__(self, title):
        # Initialize Video Class Instance Variables
        self.title = title


class Movie(Video):
    """
        Movie Class provides a way to store
        movie related information  and will inherit 
        Instance Variable from the Video class
    """
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, movie_storyline, poster_image,
                 trailer_youtube_url):
        # Initialize Variables Inhertied From Video Class
        Video.__init__(self, title)
        # Initialize Movie Class Instance Variables
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        # This Method Shows The Trailer Of The Instance It Is Called From
        webbrowser.open(self.trailer_youtube_url)
