import media
import fresh_tomatoes

#To be PEP 8 compliant I have wrapped the values in parenthesis.
#In the url cases it was recommended not to break the url.

inception = media.Movie('Inception', ('''A thief, who steals corporate
 secrets through use of dream-sharing technology, is given
 the inverse task of planting an idea into the mind of a CEO.'''), 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=YoHD9XEInc0')

bigHero6 = media.Movie('Big Hero 6', ('''The special bond that develops
 between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada,
 who team up with a group of friends to form a band of high-tech heroes.'''), 'https://images-na.ssl-images-amazon.com/images/M/MV5BMDliOTIzNmUtOTllOC00NDU3LWFiNjYtMGM0NDc1YTMxNjYxXkEyXkFqcGdeQXVyNTM3NzExMDQ@._V1_UY268_CR3,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=z3biFxZIJOQ')

spiderMan = media.Movie('Spider-Man: Homecoming', ('''Spider-Man: Homecoming
 premiered in Hollywood on June 28, 2017, and wasreleased in the United States
 on July 7, 2017, in 3D, IMAX and IMAX 3D. Homecoming has grossed over $257
 million worldwide, and received positive reviews, with critics praising
 Holland and the other cast's performances, the light tone, and the action
 sequences.'''), 'https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg', 'https://www.youtube.com/watch?v=39udgGPyYMg')

theDarkKnight = media.Movie('The Dark Knight', ('''When the menace known as
 the Joker emerges from his mysterious past, he wreaks havoc and chaos on the
 people of Gotham, the Dark Knight must accept one of the greatest
 psychological and physical tests of his ability to fight injustice.'''), 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=kmJLuwP3MbY')

wallE = media.Movie('WALL E', ('''In the distant future, a small waste-collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.'''), 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjExMTg5OTU0NF5BMl5BanBnXkFtZTcwMjMxMzMzMw@@._V1_UX182_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=8-_9n5DtKOc')

pansLabyrinth = media.Movie('''Pan's Labyrinth''', ('''In the falangist Spain
of 1944, the bookish young stepdaughter of a sadistic army officer escapes
into an eerie but captivating fantasy world.'''), 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTU3ODg2NjQ5NF5BMl5BanBnXkFtZTcwMDEwODgzMQ@@._V1_UY268_CR0,0,182,268_AL_.jpg', 'https://www.youtube.com/watch?v=E7XGNPXdlGQ')

movies = [inception, bigHero6, spiderMan, theDarkKnight, wallE, pansLabyrinth]

fresh_tomatoes.open_movies_page(movies)
