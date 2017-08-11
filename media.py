import webbrowser
# Importing webbrowser module


class Movie():
    # This initiates the class behavior. Maps movie data to class.
    def __init__(
        self, movie_title, movie_storyline, poster_image,
        trailer_youtube
    ):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # This triggers a webbrowser behavior to open the trailer ur.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
