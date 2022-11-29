# **CONNECT 4**

Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravitrips in the Soviet Union) is a two-player connection board game, in which the players choose a color and then take turns dropping colored tokens into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens.

## How to play

In this command line application of Connect 4, the user plays against the computer and the tokens are replaced by letters: 'R' as red and 'Y' as yellow.
User is player 1 (R) and computer is player 2 (Y).

User is prompted to choose a column number for dropping his/her letter and the computer randomly provides a column number for dropping its.
The game will run until someone makes 4 in a row.

![This is an image](assets/images/image-1.webp)

This is the link to the deployed application: [sbo-connect4](https://sbo-connect4.herokuapp.com/)

## Features
### Existing features

## Data Model
## Testing
## Deployment

Before hand, the required dependencies were added to the requirements.txt file on the GitPod template.

Afterwards the application was successfully deployed on Heroku.

These are the steps followed for completing the deployment:

1. On Heroku, from the Dashboard create a new app.
2. On the newly created app click on 'Settings': (insert here image setting)
3. Scroll down to 'Buildpack' section and clic on 'Add buildpack'
4. In this order add, Python and Nodejs buildpacks. The result should look like this: (insert image bp here)
5. Scroll up to 'Config Vars' section and clic on 'Reveal Config Vars'
6. Add 'Port' on the 'KEY' field and '8000' on the 'VALUE' one. Next clic on 'Add': (insert image config)
7. Go up and click on 'Deploy'(insert image?)
8. From the 'Deployment method' section, clic on 'GitHub connect'. The repository is now connected from GitHub to Heroku
9. Finally scroll down to 'Manual deploy' and clic on 'Deploy Branch'. Heroku will make the necessary and a button 'View your page' will redirect you to the deployed application.

## Credits

[Wikipedia](https://en.wikipedia.org/wiki/Connect_Four) for the explanatory text about the Connect 4 game.

Code Institute for the provided template and credits for deploying on Heroku.

## Acknowledgments

As usual, to my patient and loving family.
Warm thanks to the CI community on Slack who remains a source to turn to when searching for answers.

