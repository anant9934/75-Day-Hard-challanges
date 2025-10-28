"""
Movie Ratings App
A beginner Python project using strings, tuples, dictionaries, and lists.

Features:
- Add a movie to the database
- Add or update ratings/comments for any movie
- View all movies with ratings and comments

Author: ANANT KUMAR
Date: 28-10-2025
"""

# Initialize the list that stores all movie entries
movie_db = []

# Add a new movie entry
def add_movie(title, cast):
    """
    Create and add a new movie dictionary to the movie_db list.
    :param title: Movie title (string)
    :param cast: Cast (tuple of strings)
    """
    movie = {
        "title": title,     # string: movie name
        "cast": cast,       # tuple: actor names
        "ratings": {}       # dict: username -> {'rating': int, 'comment': str}
    }
    movie_db.append(movie)
    print(f"Added movie: {title}")

# Add or update a user's rating and comment for a movie
def rate_movie(title, user, rating, comment):
    """
    Add/update a rating and comment for a specific user on a given movie.
    :param title: Movie title (string)
    :param user: Reviewer name (string)
    :param rating: Number of stars (int)
    :param comment: Text comment (string)
    """
    for movie in movie_db:
        if movie["title"].lower() == title.lower():
            movie["ratings"][user] = {"rating": rating, "comment": comment}
            print(f"{user} rated '{title}' with {rating} stars.")
            return
    print("Movie not found. Please add the movie first.")

# Display all movies with their ratings and reviews
def view_movies():
    """
    Print the details of all movies in the database,
    including cast, ratings, and comments.
    """
    if not movie_db:
        print("No movies found in the database.")
        return
    print("\n--- All Movies ---")
    for movie in movie_db:
        print(f"Title : {movie['title']}")
        print(f"Cast  : {movie['cast']}")
        if movie["ratings"]:
            print("Ratings/Comments:")
            for reviewer, review in movie["ratings"].items():
                print(f" - {reviewer} rated {review['rating']} stars and commented: '{review['comment']}'")
        else:
            print("No ratings/comments yet.")
        print()

# Simple menu-driven interface
def menu():
    print("\n--- Movie Ratings App ---")
    print("1. Add a Movie")
    print("2. Add/Update Rating & Comment")
    print("3. View All Movies")
    print("4. Exit")

# Start interactive program
if __name__ == "__main__":
    while True:
        menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            title = input("Enter the movie title: ")
            cast_input = input("Enter cast members (comma-separated): ")
            cast = tuple(member.strip() for member in cast_input.split(","))
            add_movie(title, cast)
        elif choice == "2":
            title = input("Enter the movie title: ")
            user = input("Your name: ")
            rating = input("Your rating (1-5 stars): ")
            try:
                rating = int(rating)
                if not (1 <= rating <= 5):
                    print("Rating should be between 1 and 5.")
                    continue
            except ValueError:
                print("Please enter a number for rating.")
                continue
            comment = input("Your comment: ")
            rate_movie(title, user, rating, comment)
        elif choice == "3":
            view_movies()
        elif choice == "4":
            print("Goodbye! Your ratings are saved.")
            break
        else:
            print("Invalid choice. Please select from the menu.")

