import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=ZZv1vki4ou4")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet.",
                        "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)

annabelle = media.Movie("Annabelle Creation",
                        "Scariest movie I've ever watched!",
                        "https://upload.wikimedia.org/wikipedia/en/0/08/Annabelle_Creation.jpg",
                        "https://www.youtube.com/watch?v=EjZkJa6Z-SY")

#print(avatar.storyline)
#annabelle.show_trailer()

movies = [toy_story, avatar, annabelle]

fresh_tomatoes.open_movies_page(movies)

#print(media.Movie.VALID_RATINGS)

print(media.Movie.__doc__)
