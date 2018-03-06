import webbrowser
class Video():
    def __init__(self, title):
        print("Video Constructor Called!!!")
        self.title = title

class Movie(Video):
    """This class provides a way to store movie relates information!!!"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, movie_storyline, poster_image, trailer_youtube_url):
        print("Movie Constructor Called!!!")
        Video.__init__(self, title)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
