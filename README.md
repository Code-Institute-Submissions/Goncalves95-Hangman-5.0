# HANGMAN 5.0!

HELLO, Welcome to HANGMAN 5.0, <br>
I made the decision to create a game after learning Python. During that time, I came up with the idea of creating the hangman game. Like this i can creat a google sheet for the game pick up the words.

The game is designed to be enjoyable and bring back pleasant memories for its users.

![Responsice Mockup]()

[See deployed website](https://hangman50-78a96d76c638.herokuapp.com/)

## Table of content

- [Feed the Snake!](#feed-the-snake)
  - [Table of content](#table-of-content)
  - [Design and User Experience](#design-and-user-experience)
    - [Design](#design)
  - [Features](#features)
    - [Footer](#footer)
    - [Home Page](#home-page)
    - [Game Page](#game-page)
    - [404 Error Page](#404-error-page)
  - [Testing](#testing)
    - [Tests](#tests)
    - [Validator Testing](#validator-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)
    - [Performance](#performance)
  - [Deployment](#deployment)
    - [Live Website](#live-website)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Technologies used](#technologies-used)

## Design and User Experience

### Design

The design of the website is minimalist, yet fun. The user can experience the game on a already creat tamplate from my school @CodeInstitute.

## Features

There are just one page for the python can run

## Testing

To test my game I have opened it on different devices, to see if it was working as expected.

- Browser tested:
  - Chrome
  - Firefox
  - Safari

- Operating systems:
  - Android
  - iOS

### Validator Testing

- CI Python Linter
  - No errors were returned when passing the final version through the [CI Python Linter](https://pep8ci.herokuapp.com/#)

### Fixed Bugs
- Long lines on Python code:
  - The solution was to create strings with the variable name outside the function.
- The prints weren't showing:
  - The "Wrong guess" or "Correct guess!" prints don't appear on the console, so I've created a 1-minute sleep time so that the player can see the prints.

### Unfixed Bugs

### Game in action

- Here are some screenshots of the game in action
<details>
  <summary> Desktop </summary>
  
- Home page:

   ![Desktop - home page](assets/media/main_page_web.png)

- Game page:

   ![Desktop - game page](assets/media/game_page_web.png)

- 404 Error page:

   ![Desktop - 404 error page](assets/media/error_404_page_web.png)

</details>

## Deployment
- The deployment was done through heroku. following the steps below:
  - Preparing for deployment:
      - Add a new line character ("\n") at the end of each input request.
      - Create a list of dependancies to go into the requirements.txt file by typing "pip3 freeze > requirements.txt" into the terminal.
  - Deployment:
      - Log into Heroku and in the dashboard, press the "Create new app" button.
      - Click on the "Settings" tab, scroll down to the "Reveal Config Vars" button and click on it to create config vars.
      - Add the first config vars. The key is "CREDS" and value is the contents of the creds.json file.
      - Add the second config vars. The key is "PORT" and value is "8000".
      - Click on the "Add buildpack" button on the same page and add the buildpacks "python" and "node.js" in this order.
      - Click on the "Deploy" tab.
      - Choose the "GitHub" deployment method and then connect to GitHub.
      - Scroll down to the "Automatic deploys" section, select the "main" branch to deploy from and then press the "Enable Automatic Deploys" button to deploy the project.

### Live Website

The live link can be found here - [Live Website](https://hangman50-78a96d76c638.herokuapp.com/)

## Credits

### Content

- Hangman 5.0 big title from - [Text Editor](https://texteditor.com/)
- Learning to create the game with - [Python for Beginners](https://www.pythonforbeginners.com/code-snippets-source-code/game-hangman) and [Hashtag](https://www.hashtagtreinamentos.com/jogo-da-forca-em-python) and [DIO](https://www.dio.me/articles/jogo-da-forca-em-python)

## Technologies used

- Python
- GitHub
- CodeAnywhere
- Heroku
- Google API (sheets)