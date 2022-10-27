import gspread
from google.oauth2.service_account import Credentials
import os
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

titel_ratings = SHEET.worksheet('titel_ratings')


menu_options = {
    1: 'Show Full Movies List',
    2: 'Show Top 10 Movies',
    3: 'Add New Movie & Rating',
    4: 'Exit Program',
}


"""

"""

def print_menu():
    print("Welcome movie blabla")
    print("Enter options 1-4")
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

def get_full_list():
    clear()
    movies = titel_ratings.get_all_records()
    for movie in movies:
        print(movie)
    input('Press Enter to Return to Menu: ')
    clear()

def get_top_ten():
    clear()
    movies = titel_ratings.get_all_records()
    newlist = sorted(movies, key=lambda d: d['Ratings'], reverse=True)
    for movie in newlist:
        print(movie)

def update_worksheet():
    """
    Receives a list of integers to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    clear()
    title = input('Enter Movie Title: ')
    raiting = input('Enter Movie Raiting: ')
    worksheet_to_update = SHEET.worksheet("titel_ratings")
    worksheet_to_update.append_row([title, raiting])
    print(f"Added - Movie: {title} Raiting: {raiting}")


def main():
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
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


main()