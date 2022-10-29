# MOVIE DATABASE (PP3 by Christofer Asplund)

Movie database is a program written in Python, wich runs in the Code Institute mock terminal on Heroku.
The program is connected to a Google Sheet API that stores all data.

The user can view a complete list or a top 10 list of the movies they have watched and rated. The user can also
add new movies to the list and delete movies from the list.

[Link to a live version of my project.](https://movie-database-p3.herokuapp.com/)

<img width="1339" alt="Responsive" src="https://user-images.githubusercontent.com/96183912/198847698-7a7896a6-f0d5-4065-9357-b885b51b4bd0.png">

## Program navigation & Features

### Main Page
  - When the program starts you will be welcomed by a welcome message that gives information about the program. And below the message
  you will see the options menu, read more about this section below.

<img width="727" alt="Main page" src="https://user-images.githubusercontent.com/96183912/198847783-ce33cf06-1376-467d-83f7-6891cb355e01.png">

### Options Menu
  - In the options menu you will be able to choose from 5 different options. To access an option press the desired number and enter.
  
<img width="715" alt="Program navigation" src="https://user-images.githubusercontent.com/96183912/198840787-1f52e538-55df-4820-b76b-f37fc6cf7a62.png">

### Show Full Movies List (1 + Enter)
  - This options alow you to see a list of all movies that you have added to your database. The movies will be displayed in a sorted list from
  best rating to worst. Press enter to return to the options menu.
  
<img width="725" alt="All movies" src="https://user-images.githubusercontent.com/96183912/198846736-22f29be3-5de0-493e-92fd-0441aac59776.png">

### Show Top 10 Movies (2 + Enter)
  - This option will give you a list of your top 10 movies based on rating. The movies will be displayed in a sorted list from best rating to worst.
  Press enter to return to the options menu.
  
<img width="730" alt="Top 10 movies" src="https://user-images.githubusercontent.com/96183912/198846982-8eb300f0-de70-452a-90c5-209e167c504e.png">

### Add New Movie & Rating (3 + Enter)
  - In this option you will be able to add a new movie to your database.
  
- First add a title - this can be either letters and/or numbers but can't be left empty.

<img width="488" alt="Add title" src="https://user-images.githubusercontent.com/96183912/198847877-1d888443-4088-4cb2-bac5-abb9965c96b2.png">

- Then add a rating - this must be a float number between 0.0 - 5.0 and can't be left empty.

<img width="479" alt="Add rating" src="https://user-images.githubusercontent.com/96183912/198848130-0b2774bf-2e83-41d8-8723-e7b2574c51c8.png">

- When all the steps above are correctly filled in you will get a message telling you that your movie have been added.
Press Enter to return to the menu, now you can browse your list of movies to see that your new movie has been added.

<img width="404" alt="Movie added" src="https://user-images.githubusercontent.com/96183912/198848268-c3141ae8-b107-4998-a9d9-58704f2fecde.png">

### Delete a Movie From the List (4 + Enter)
  - In this option you will be able to delete an exsisting movie from the list.
  
- Here you will see a list of all your movies, scroll until you find your desired movie to delete.
In this list all movies have been assigned a "Movie ID", simply enter the ID number of the movie you want to delete and press Enter.

<img width="712" alt="Enter Id" src="https://user-images.githubusercontent.com/96183912/198848544-bdf61a9e-562b-49c6-86e0-e43862cbd1eb.png">

- You will then get a message confirming what Movie ID have been deleted from the list. Press Enter to return to the menu.

<img width="494" alt="Movie deleted" src="https://user-images.githubusercontent.com/96183912/198848598-07431f4a-7f75-4806-8a5d-66e4df31824f.png">

### Exit Program (5 + Enter)
  - This option will close the program.
  
  
## Future Features
 - Allow users to review movies


## Data Model
I used a Movie class as my model. The program uses one instance of the Movie class to hold a movie when adding
a movie to the program.

The Movie class stores the movie title, movie rating and movie id.


## Testing

I have manually tested this program by doing the following:
 - Given invalid inputs: strings, numbers and other keyboard characters(ex. *^/&%€) when the program is expecting the opposite input.
 - Hard testing my local terminal and Code Institute Heroku terminal.
 - Making sure that my IDE isn't giving any type errors that doesn't match with the PEP8 style.


## Bugs



### Solved Bugs

- Option 3 had an input error when entering a string into the rating input. I solved it by making sure the input only accepts a float number between 0.0 - 5.0. And adding a print statement saying "Invalid data: Rating must be a float between 0.0 - 5.0." if a string is entered.

### Unsolved Bugs
 
- No unsolved bugs remaining.


## Deployment

This project was deployed using Code Instute's mock terminal on Heroku.

- Step by step for deployment: 
  - Fork or clone this repository.
  - Create a new Heroku app.
  - Buildbacks should be set in this order Python and NodeJs.
  - The Heroku app should be linked to this repository
  - Then click deploy and wait while the app is being built, when complete click view.

The links for the project can be found here -
- HEROKU LINK: https://movie-database-p3.herokuapp.com/
- GITHUB LINK: https://github.com/Aspen92/movie-rating-p3

## Credits 
- Code Institute for deployment terminal.
- IMDB for inspiration.



