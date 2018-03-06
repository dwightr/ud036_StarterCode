import fresh_tomatoes
import media

annabelle = media.Movie("Annabelle Creation",
                        "Scariest movie I've ever watched!",
                        "https://upload.wikimedia.org/wikipedia/en/0/08/Annabelle_Creation.jpg",
                        "https://www.youtube.com/watch?v=EjZkJa6Z-SY")

bad_boys = media.Movie("Bad Boys",
                        "All time favorite comedy!",
                        "https://upload.wikimedia.org/wikipedia/en/a/a8/Bad_Boys.jpg",
                        "https://www.youtube.com/watch?v=APhw7rju-Co")

conjuring = media.Movie("The Conjuring",
                        "Second most scariest movie I've ever watched!",
                        "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg",
                        "https://www.youtube.com/watch?v=k10ETZ41q5o")

elm_street = media.Movie("A nightmare on Elm street",
                        "Growing up I used to be afraid of Freddy Krueger, my parents said he lives close by just to get me to not stay out late!",
                        "https://upload.wikimedia.org/wikipedia/en/2/2e/NightmareOnElmStreetBoxSetSide.jpg",
                        "https://www.youtube.com/watch?v=l74v9D0UHNU")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life!",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

black_panther = media.Movie("Black Panther",
                        "Latest movie I have watched at the cinema!",
                        "https://upload.wikimedia.org/wikipedia/en/0/0c/Black_Panther_film_poster.jpg",
                        "https://www.youtube.com/watch?v=xjDjIWPwcPU")


movies = [annabelle, bad_boys, conjuring, elm_street, toy_story, black_panther]

fresh_tomatoes.open_movies_page(movies)
