import gspread
from google.oauth2.service_account import Credentials
import os
from pprint import pprint
clear = lambda: os.system('clear')


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('movie_ratings_p3')

title_ratings = SHEET.worksheet('title_ratings')




menu_options = {
    1: 'Show Full Movies List',
    2: 'Show Top 10 Movies',
    3: 'Add New Movie & Rating',
    4: 'Delete a Movie From the List',
    5: 'Exit Program',
}


"""

"""

def print_menu():
    """
    """
    print("Welcome movie blabla")
    print("Enter options 1-4")
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def get_full_list():
    """
    """
    clear()
    movies = title_ratings.get_all_records()
    full_list = sorted(movies, key=lambda d: d['Ratings'], reverse=True)
    for movie in full_list:
        print(f'Title: {movie["Title"]} - Ratings: {movie["Ratings"]}')
    input('Press Enter to Return to Menu: ')
    clear()

def get_top_ten():
    """
    """
    clear()
    print("Here is the Top 10 Movies")
    movies = title_ratings.get_all_records()
    newlist = sorted(movies, key=lambda d: d['Ratings'], reverse=True)
    for movie in newlist[0:10]:
        print(f'Title: {movie["Title"]} - Ratings: {movie["Ratings"]}')
    input('Press Enter to Return to Menu: ')
    clear()

def update_worksheet():
    """
    """
    clear()
    title = input('Enter Movie Title: ')
    raiting = input('Enter Movie Rating (Use only point numbers ex. 4.3): ')
    worksheet_to_update = SHEET.worksheet("titel_ratings")
    worksheet_to_update.append_row([title, raiting])
    print(f"Added - Movie: {title} Rating: {raiting}")
    input('Press Enter to Return to Menu: ')
    clear()


def main():
    """
    """
    while(True):
        print_menu()
        option = int(input('Enter your choice: ')) 
        if option == 1:
            get_full_list()
        elif option == 2:
            get_top_ten()
        elif option == 3:
            update_worksheet()
        elif option == 4:
            print('Delete')
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


main()