import webbrowser
#importing webbrowser module

class Movie():
    #this initiates the class behavior adding the information added on entretainment_center.py
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    #this triggers a webbrowser behavior to open the trailer url from a defined movie title.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
