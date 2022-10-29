"""
MOVIE DATABASE PROGRAM by Christofer Asplund.
Code Institute, project 3.
"""
import os
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("movie_ratings_p3")

title_ratings = SHEET.worksheet("title_ratings")
menu_options = {
    1: "Show Full Movies List",
    2: "Show Top 10 Movies",
    3: "Add New Movie & Rating",
    4: "Delete a Movie From the List",
    5: "Exit Program",
}


def print_menu():
    """
    Prints welcome message, info message and options menu
    to user from a for loop.
    """
    print("\n    WELCOME TO YOUR OWN MOVIE DATABASE PROGRAM!")
    print("    -------------------------------------------")
    welcome_msg = """
    This program allows you to view your complete movie list and add your
    latest movie you have watched.
    You can give your movies a rating and the program will sort your movies
    from best to worst.
    You can also remove movies from the list using the ID number of the movie.
    """
    print(welcome_msg)
    print("Enter options 1-4\n")
    for key, value in menu_options.items():
        print(key, "--", value)


def clear():
    """
    Function that clears the output.
    """
    os.system("clear")


def get_full_list():
    """
    Function with a for loop that gets all movies from google sheets sorted in
    ratings order from best to worst
    and prints the list to the output.
    """
    clear()
    print("\n\n\n\n")
    print("-------------------------------------------")
    print("ALL MOVIES:\n")
    movies = title_ratings.get_all_records()
    full_list = sorted(movies, key=lambda d: d["Ratings"], reverse=True)
    for movie in full_list:
        print(f'Title: {movie["Title"]}\nRatings: {movie["Ratings"]}\n')
    input("\nPress Enter to Return to Menu:\n")
    clear()


def get_top_ten():
    """
    Function with a for loop that gets the top 10 movies with the best
    rating(best-worst)
    and prints the list to the output.
    """
    clear()
    print("\n\n\n\n")
    print("-------------------------------------------")
    print("TOP 10 MOVIES\n")
    movies = title_ratings.get_all_records()
    newlist = sorted(movies, key=lambda d: d["Ratings"], reverse=True)
    for movie in newlist[0:10]:
        print(f'Title: {movie["Title"]}\nRatings: {movie["Ratings"]}\n')
    input("Press Enter to Return to Menu:\n")
    clear()


def update_worksheet():
    """
    Function with if/else statements for the 'Add New Movie & Rating option'.
    It let's you enter a movie title that is a string and a raiting that is a
    float number.
    Then adds the new movie to the google sheet and gives it a unique ID
    number.
    """
    clear()
    title = input("Enter Movie Title: ")
    if validate_input_title(title):
        rating = input("Enter Movie Rating (0.0 - 5.0):\n")
        if validate_input_rating(rating):
            if float(rating) <= 5.0:
                worksheet_to_update = SHEET.worksheet("title_ratings")
                movies = title_ratings.get_all_records()
                max_value = max(movies, key=lambda x: int(x["Movie_ID"]))
                new_id = int(max_value["Movie_ID"]) + 1
                worksheet_to_update.append_row([title, rating, new_id])
                print(f"\nADDED\nMovie: {title}\nRating: {rating}")
                input("\nPress Enter to Return to Menu:\n")
                clear()
            else:
                clear()
                print("""Invalid data: Rating must
                be a float between 0.0 - 5.0.\n""")
                input("\nPress Enter to return to add new movie option:\n")
                update_worksheet()
        else:
            input("\nPress Enter to return to add new movie option:\n")
            update_worksheet()
    else:
        clear()
        print("Invalid data: Title can't be left empty.\n")
        input("\nPress Enter to return to add new movie option:\n")
        update_worksheet()


def validate_input_title(title):
    """
    Validate that the user input is not empty.
    """
    if len(title) > 0:
        return True
    else:
        return False


def validate_input_rating(value):
    """
    Validates that the user input is a float number.
    """
    try:
        float(value)
    except ValueError:
        clear()
        print("Invalid data: Rating must be a float between 0.0 - 5.0.\n")
        return False

    return True


def delete_movie():
    """
    Function with a for loop that prints a list of all movies with the ID
    numbers and let's you delete a movie from the list by
    entering the movie ID number.
    """
    clear()
    print("\n\n\n\n")
    print("-------------------------------------------")
    print("ALL MOVIES:\n")
    movies = title_ratings.get_all_records()
    full_list = sorted(movies, key=lambda d: d["Ratings"], reverse=True)
    id_list = []
    for movie in full_list:
        id_list.append(str(movie["Movie_ID"]))
        print(f'Title: {movie["Title"]}\nRatings: {movie["Ratings"]}')
        print(f'Movie ID: {movie["Movie_ID"]}\n')
    movie_id = input("Enter Movie ID: ")
    if movie_id in id_list:
        row = title_ratings.find(movie_id, in_column=3).row
        title_ratings.delete_rows(row)
        clear()
        print(f"Deleted movie with ID: {movie_id}\n")
        input("\nPress Enter to return to menu:\n")
        clear()
    else:
        clear()
        print(f"Invalid ID: No movie found with ID: {movie_id}\n")
        input("\nPress Enter to return to menu:\n")
        clear()


def main():
    """
    Main function that runs the different options functions.
    """
    while True:
        print_menu()
        try:
            option = int(input("\nEnter your choice:\n"))
            if option == 1:
                get_full_list()
            elif option == 2:
                get_top_ten()
            elif option == 3:
                update_worksheet()
            elif option == 4:
                delete_movie()
            elif option == 5:
                print("Exit movie database!")
                exit()
            else:
                clear()
                print("""Invalid option:
                Please enter a number between 1 and 4.\n""")
                input("\nPress Enter to return to menu:\n")
                clear()
        except ValueError:
            clear()
            print("Invalid option: Please enter a number between 1 and 4.\n")
            input("\nPress Enter to return to menu:\n")
            clear()


if __name__ == "__main__":
    main()
