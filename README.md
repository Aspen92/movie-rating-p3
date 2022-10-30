# MOVIE DATABASE (PP3 by Christofer Asplund)

Movie database is a program written in Python, wich runs in the Code Institute mock terminal on Heroku.
The program is connected to a Google Sheet API that stores all data.

The user can view a complete list or a top 10 list of the movies they have watched and rated. The user can also
add new movies or delete movies from the list.

[Link to a live version of my project.](https://movie-database-p3.herokuapp.com/)

<img width="1339" alt="Responsive" src="https://user-images.githubusercontent.com/96183912/198847698-7a7896a6-f0d5-4065-9357-b885b51b4bd0.png">

## Program navigation & features

### Main Page
  - When the program starts the user will be welcomed by a message that gives them information about the program. Below the message
  the user will see the options menu. Read more about this section below.

<img width="727" alt="Main page" src="https://user-images.githubusercontent.com/96183912/198847783-ce33cf06-1376-467d-83f7-6891cb355e01.png">

### Options Menu
  - In the options menu the user will be able to choose from 5 different options. To access an option press the desired number and enter.
  
<img width="715" alt="Program navigation" src="https://user-images.githubusercontent.com/96183912/198840787-1f52e538-55df-4820-b76b-f37fc6cf7a62.png">

### Show Full Movies List (1 + Enter)
  - This options allows the user to see a list of all movies that the user has added to their database. The movies will be displayed in a sorted list from
  best rating to worst. Press enter to return to the options menu.
  
<img width="725" alt="All movies" src="https://user-images.githubusercontent.com/96183912/198846736-22f29be3-5de0-493e-92fd-0441aac59776.png">

### Show Top 10 Movies (2 + Enter)
  - This option will give the user a list of their top 10 movies based on rating. The movies will be displayed in a sorted list from best rating to worst.
  Press enter to return to the options menu.
  
<img width="730" alt="Top 10 movies" src="https://user-images.githubusercontent.com/96183912/198846982-8eb300f0-de70-452a-90c5-209e167c504e.png">

### Add New Movie & Rating (3 + Enter)
In this option the user will be able to add a new movie to their database.
  
- Enter a title - this can be either letters and/or numbers but can't be left blank.

<img width="488" alt="Add title" src="https://user-images.githubusercontent.com/96183912/198847877-1d888443-4088-4cb2-bac5-abb9965c96b2.png">

- Add a rating - this must be a float number between 0.0 - 5.0 and can't be left blank.

<img width="479" alt="Add rating" src="https://user-images.githubusercontent.com/96183912/198848130-0b2774bf-2e83-41d8-8723-e7b2574c51c8.png">

- When all the steps above are correctly filled in the user will get a message telling them that their movie has been added.
Press Enter to return to the menu. Now the user can browse the list of movies and see that the new movie has been added.

<img width="404" alt="Movie added" src="https://user-images.githubusercontent.com/96183912/198848268-c3141ae8-b107-4998-a9d9-58704f2fecde.png">

### Delete a Movie From the List (4 + Enter)
In this option the user will be able to delete an exsisting movie from the list.
  
- Here the user will see a list of all their movies and be able to scroll and find the desired movie to delete.
In this list all movies have been assigned a "Movie ID". The user can simply enter the ID number of the movie they want to delete and press Enter.

<img width="712" alt="Enter Id" src="https://user-images.githubusercontent.com/96183912/198848544-bdf61a9e-562b-49c6-86e0-e43862cbd1eb.png">

- The user will then get a message confirming what Movie ID has been deleted from the list. Press Enter to return to the menu.

<img width="494" alt="Movie deleted" src="https://user-images.githubusercontent.com/96183912/198848598-07431f4a-7f75-4806-8a5d-66e4df31824f.png">

### Exit Program (5 + Enter)
  - This option will close the program.
  
  
## Future Features
 - Allow for the user to register each movie's realse date.
 - Allow for the user to give a review for each movie.


## Data Model
I used a Movie class as my model. The program uses one instance of the Movie class to hold a movie when adding
a movie to the program.

The Movie class stores the movie title, movie rating and movie id.


## Testing

I have manually tested the program by doing the following:
 - Given invalid inputs: strings when the program expected numbers and vice versa, left empty when input was expected and vice versa.
 - Hard testing my local terminal and Code Institute Heroku terminal.
 - Making sure that my IDE doesn't giving any type errors that don't match with the PEP8 style.


## Bugs


### Solved Bugs

- Option 3 had an input error when entering a string into the rating input. I solved this by making sure the input only accepts a float number between 0.0 - 5.0 and added a print statement saying "Invalid data: Rating must be a float between 0.0 - 5.0." if a string is entered.

- Option 4 when trying to delete a movie I had a bug when I was trying to compare the movie id with the id that the user enters. When reading from the google sheet, gspread returns the movie id as an int and the input from the user is always a string, so the comparison was always returning false. I solved the issue by parsing the movie id when reading from gspread to a string so the two values could be compared correctly.

### Unsolved Bugs
 
- No unsolved bugs remaining.


## Deployment

 This project was deployed using Code Instute's mock terminal on Heroku.

- The application was deployed to Heroku. The steps I took to deploy are as follows:
  - From my IDE I pushed my final code to GitHub, making sure that my creds.json file was mentioned in the gitignore file
to keep confidential information safe.
  - I created an account on Heroku.com.
  - On Heroku I chose the option to create a new application.
  - Here I entered a name for my application and chose Europe as region.
  - In the settings tab I added necessary information to the config vars section.
  - In the deploy tab I chose to connect my application to GitHub and searched for my repository name and pressed connect.
  - Then I chose the manually deploy option and deployed my main branch.
  - When Heroku was done building the application I received a live link to the deployed application.

The live link can be found here - https://movie-database-p3.herokuapp.com/


This project was deployed using Code Instute's mock terminal on Heroku.

- Step by step that I took to deploy my app: 
  - Created an account on Heroku.com.
  - Create a new Heroku app.
  - 
  - Buildbacks should be set in this order: Python and NodeJs.
  - The Heroku app should be linked to this repository
  - Then click deploy and wait while the app is being built, when completed click view.

The links for the project can be found here -
- HEROKU LINK: https://movie-database-p3.herokuapp.com/
- GITHUB LINK: https://github.com/Aspen92/movie-rating-p3

## Credits 
- Code Institute for deployment terminal.
- IMDB for inspiration.



