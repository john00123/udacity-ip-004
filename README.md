# Udacity Full Stack Developer Nanodegree Program
#### Programming Fundamentals
### Create a movie website
Code was written to store all the list of my favorite current movies, including box art and images hoster on **Wikipedia**. Additionally there is a link to the each movie's trailer that is hoster in **Youtube**. Code is used to generate a static web page allowing browsers to be able to read the information on a index.html file.

###### Website functionality
The website allows you to navigate through a grid base interface of box art imagery. Once a movie has been selected, there movie trailer will be shown to the user.

##### How to run the program
To access the final design, you need to open the file `fresh_tomatoes.py` in a terminal or batch interface with python installed. Then an index.html file will be available to be viewed using your browser.

### Developer notes:
The project was built using python.
The movie variables have been created by using Classes defined in `media.py`.
Then the `fresh_tomatoes.py` file defines the html with styles to be created.

There are 3 files in this project:
 - entretainment_center.py - has the main information for the movies metadata.
 - media.py -  uses browser library to open a popup using the classes provided.
 - fresh_tomatoes.py - has the code to render an HTML site using media and entretainment_center.py
