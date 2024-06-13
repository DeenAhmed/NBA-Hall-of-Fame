## NBA-Hall-of-Fame

### Overview

NBA Hall of Fame is based on a terminal which allows you to view 20 current NBA Hall Of Famer's Career statistics, listing their Player ID, Name, Induction Year, Games Played, Points,Rebounds, Assists, Steals and Blocks, view an individual player's career statistics and add a new Hall of Fame player's statistics.

## Application Aims

This application aims to:

- Provide clear instructions
- Present NBA HOF player statistics
- Allow user to select a specific player statistics to view
- Allow user to add a new HOF player statistics

### Target audience

- People with interest in basketball
- People looking to gain knowledge on NBA basketball Hall of Fame facts

## UX Flow Chart

To allow me to visualise the basic logic flow I would need to implement for a smooth user experience, I created the following flow chart during the planning stages using: [draw.io's flow chart maker](https://app.diagrams.net/)

![Process Flow](assets/images/Process%20Flow.png)

## Features

## Start Menu

The Start Menu presents 4 options allowing the user to enter a number between 1-4 to proceed into the next stage.

![Start Menu](assets/images/Hof%20Start%20Menu.png)

### Start Menu - Invalid Input

When entering an invalid option into the terminal you receive a message stating please select a number between 1 - 4.

![Start Menu - Inavlid Input](assets/images/hof%20start%20menu%20-%20inavlid.png)

## Option 1

Option 1 allows you to view 20 Hall Of Famer statistics in a list ascending from the Induction Year.

![View a list of 20 Hall Of Fame Players and their career total stats](assets/images/hof%20start%20menu%20success.png)

## Option 2

Option 2 allows you to view a specific player on the lists indivdiual stats by entering their name.

![View an individual player's career stats](assets/images/hof%20player%20-%20success.png)

### Option 2 - Invalid Input

When entering an invalid option into the terminal you receive a message stating player not found and the terminal will ask you to input a name again.

![View an individual player's career stats - Invalid Input](assets/images/hof%20player%20-%20invalid.png)

## Option 3

Option 3 allows you to add a new player career stats to the list. Asking for each career stat on a new line and successfully adding this player stats to the list.

![Add a new player's career stats](assets/images/hof%20add%20-%20success.png)

### Option 3 - Invalid Input

Throught adding a new players stats you are met with validation to ensure you enter the correct data and the terminal will present the option to enter the data again.

![Add a new player's career stats - Invalid Input](assets/images/hof%20add%20-%20invalid%20.png)

![Add a new player's career stats - Invalid Input](assets/images/hof%20add%20-%20invalid%202.png)

## Option 4

This allows you to Exit the terminal and does not run the application.

![Exit](assets/images/hof%20exit.png)

## Testing

### Functionality

- Implementation: I wanted to make sure the applcaiton performed as expected from start to finish.
- Test: I ran through the applcation on a local terminal and on Heroku over 20 times.
- Result: The applcation worked as anticipated with no errors.
- Verdict: Test passed.

- Implementation: Check the input validation was working as expected.
- Test: I ran through the applcation on a local terminal and on Heroku over 20 times.
- Result: The validation worked well. There were no instamces when it was possible to enter an invalid input.
- Verdict: Test passed.

- Implementation: Check the data being added to spreadsheet was working as expected.
- Test: I ran through the applcation on a local terminal and on Heroku over 10 times.
- Result: The data was being added with no errors.
- Verdict: Test passed.

### Validation

I used [PEP8](https://pep8ci.herokuapp.com/) to validate the Python on this project with the only warnings for lines being too long. I got this down to being 1-2 character out for these.

<details><summary>PEP8 Validation</summary>
<img src="assets/images/hof validation.png">
</details>

### Issues

- Issue: When trying to run this locally gspread import would show an error
- Fix:   Install pip3 and this resolved the issue

- Issue: Whnen trying to retreive individual player stats terminal would show valid when entering correct name
- Fix:   Within for loop range was set at 1 which was getting incorrect value, changed to 2 and this retreive correct value and presented data

### Deployment

The project was deployed to Heroku using the below procedure:-

1. Log in to Heroku or create an account if required.
2. Click the button labeled New from the dashboard in the top right corner, just below the header.
3. From the drop-down menu select "Create new app".
4. Enter a unique app name. I chose nba-hall-of-fam for this project, for reasons stated above.
5. Once the web portal shows the green tick to confirm the name is original select the relevant region. In my case, I chose Europe as I am in the UK.
6. When happy with your choice of name and that the correct region is selected, click on the "Create app" button.
7. This will bring you to the project "Deploy" tab. From here, navigate to the settings tab and scroll down to the "Config Vars" section.
8. Click the button labelled "Reveal Config Vars" and enter the "key" as port, the "value" as 8000 and click the "add" button.
9. Scroll down to the buildpacks section of the settings page and click the button labeled " add buildpack," select "Python," and click "Save Changes".
10. Repeat step 11 but this time add "node.js" instead of python.
    - IMPORTANT The buildpacks must be in the correct order. If node.js is listed first under this section, you can click on python and drag it upwards to change it to the first buildpack in the list.
11. Scroll back to the top of the settings page, and navigate to the "Deploy" tab.
12. From the deploy tab select Github as the deployment method.
13. Confirm you want to connect to GitHub.
14. Search for the repository name and click the connect button next to the intended repository.
15. From the bottom of the deploy page select your preferred deployment type by follow one of the below steps:
    - Clicking either "Enable Automatic Deploys" for automatic deployment when you push updates to Github.
    - Select the correct branch for deployment from the drop-down menu and click the "Deploy Branch" button for manual deployment.
The final deployment can be viewed [here](https://nba-hall-of-fame-3d4f18769cc0.herokuapp.com/)

## Technologies used

- HTML & Python programming languages
- [VSCode](https://code.visualstudio.com/) - IDE for local developement
- [GIT](https://git-scm.com/) - Version Control
- [GitHub](https://github.com/) - To host the repositories for this project
- [Heruko](https://heroku.com/) - To deploy this application

## Acknowledgements

I would like to take the opportunity to thank:

- My friends and work colleagues for their advice, support and help with testing.
- My mentor [Richard Wells](https://github.com/D0nni387) for his first class support.
