import media    #another file where movie class has been decalred
import fresh_tomatoes  #another file to render html page

# different objects of Movie class
# argument list(movie_title, movie_storyline, movie_poster_image, movie_trailer_youtube_link)

#object1 
dear_zindagi = media.Movie("Dear Zindagi",
                        "Kaira, a young girl, faces problems in her relationships. She meets Dr Jehangir, "
                        "who helps her resolve her issues with her parents and get a new perspective on "
                        "life, which leads to her following her passion and an improvement in her love life.",
                        "http://www.bollywoodlife.com/wp-content/uploads/2016/10/dear-zindagi.jpg",
                        "https://youtu.be/5DkO7ksXY8E" )
#object2
holiday = media.Movie("Holiday",
                     "After a bomb destroys the bus on which he was riding, a military officer (Akshay Kumar) "
                     "foregoes his vacation to hunt down a terrorist and the sleeper cells under his command.",
                     "http://www.bollywoodlife.com/wp-content/uploads/2014/06/poster-3.jpg",
                     "https://youtu.be/_34g6rCe0YY")
#object3
padmavat = media.Movie("Padmavat",
                       "Set in 1303 AD medieval India, Padmaavat is the story of honor, valor and obsession. "
                       "Queen Padmavati is known for her exceptional beauty along with a strong sense of "
                       "justice and is the wife of Maharawal Ratan Singh and pride of the Kingdom of "
                       "Chittor, a prosperous kingdom in the north west of India.",
                       "http://static.koimoi.com/wp-content/new-galleries/2018/01/padmavat-3.jpg",
                       "https://youtu.be/8YaF2m7hCx0")
#object4
dil_to_pagal_hai = media.Movie("Dil To Pagal Hai",
                             "Promised to another via arranged marriage, a dancer (Madhuri Dixit) "
                             "falls in love with her director (Shahrukh Khan).",
                             "https://images-na.ssl-images-amazon.com/images/I/616co2rTKwL._SX342_.jpg",
                             "https://youtu.be/BdhPleFcEJ0")
#object5
badrinath_ki_dulhania = media.Movie("Badrinath Ki Dulhania",
                                "A man (Varun Dhawan) and a woman (Alia Bhatt) fall in love despite "
                                "their opposing views on gender and life in general.",
                                "http://www.media.glamsham.com/download/poster/images/badrinath-ki-dulhaniya/03-badrinath-ki-dulhaniya.jpg",
                                "https://youtu.be/ztX-iGlZ_Ug")
#object6
baahubali2 = media.Movie("Baahubali 2",
                         "When Bhallaladeva conspires against his brother to become the king of Mahishmati, "
                         "he has him killed by Katappa and imprisons his wife. Years later, his brother's"
                         "son returns to avenge his father's death.",
                           "https://images-na.ssl-images-amazon.com/images/I/711eHgGtnFL._SX385_.jpg",
                           "https://youtu.be/G62HrubdD6o")

#all objects has been added to list(movies)
movies = [dear_zindagi, holiday, padmavat, dil_to_pagal_hai, badrinath_ki_dulhania, baahubali2]

#def open_movies_page from fresh_tomatoes file accepts list only.
fresh_tomatoes.open_movies_page(movies)

