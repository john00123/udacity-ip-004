# Udacity Full Stack Developer Nanodegree Program
### Programming Fundamentals


### Create a movie website Summary
Code was written to store all the list of my favorite current movies, including box art and images hosted on **Wikipedia**. Additionally there is a link to the each movie's trailer that is hoster in **Youtube**. Code is used to generate a static web page allowing browsers to be able to read the information on a index.html file.

### Website functionality
The website allows you to navigate through a grid base interface of box art imagery. Once a movie has been selected, there movie trailer will be shown to the user.

---

### Prerequisites
- Download [Python 2.7](https://www.python.org/download/releases/2.7/#download)
- Terminal or a Command line equivalent interface (Command Prompt on Windows).

### Installation
- Download or clone this [Project](https://github.com/john00123/udacity004).
- Once downloaded, open terminal and navigate to the project's directory on your local machine.
> An easy way to achieve this in Terminal is by typing `cd` and dragging the folder onto the command window)
- Once you are in the correct directory run `python entretainment_center.py` to generate the html.

### Installation Example

```Python
$  cd /Users/Yourname/Downloads/udacity004-master
udacity004-master$  python entretainment_center.py
```
> Ignore everything before `$` as is meant to represent the directory change in the process. 

---

### Developer notes:
The project was built using python.
The movie variables have been created by using Classes defined in `media.py`.
Then the `fresh_tomatoes.py` file defines the html with styles to be created.

There are 3 files in this project:
 - entretainment_center.py - has the main information for the movies metadata.
 - media.py -  uses browser library to open a popup using the classes provided.
 - fresh_tomatoes.py - has the code to render an HTML site using media and entretainment_center.py


## License
MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
