# F1-Discord Bot

A simple discord bot created using python and Discord API wrapper: *discord.py*. The bot displays information about the *2022 Formula 1* season such as, the driver and constructor standings, upcoming schedule, race wins, etc. It uses **webscraping techniques** to obtain the latest, up-to-date information.

This project was created as a Core-Selection evaluation project for **Lambda - the Software Development Club of IITH**.

The bot has been deployed using the free cloud service provider [Heroku.](https://www.heroku.com/)

To add the bot to your server:
[Click here!](https://discord.com/oauth2/authorize?client_id=988392963434508318&permissions=534723950656&scope=bot)

## Libraries used

* [discord.py](https://discordpy.readthedocs.io/en/stable/) - for basic discord bot functionality
* [requests-html](https://requests.readthedocs.io/projects/requests-html/en/latest/) - to webscrape data from static and dynamic webpages
* [pandas](https://pandas.pydata.org/docs/) - to webscrape data in tables from webpages and handle the data
* [table2ascii](https://table2ascii.readthedocs.io/en/latest/) - to make the tabular data pretty
* [Beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) + [requests](https://requests.readthedocs.io/en/latest/) - initially used to webscrape, then I switched to requests-html

## Usage

* All commands start with `.` 
* type `.help <commandname>` to get the description for a specific command

*General Commands*
|Command|Description|
|-------|-----------|
|`.help`|Displays the list of all commands|
|`.hello`|Says hello to the user|
|`.bye`|Says bye to the user|

*F1 Commands*
|Command|Description|
|-------|-----------|
|`.drivers`|Displays the 2022 Driver Standings|
|`.teams`|Displays the 2022 Constructor/Team Standings|
|`.racewins`|Displays the winners of all the races this season|
|`.news`|Gives you the latest F1 news|
|`.nextrace`|Displays the full schedule of the next race|
|`.schedule`|Displays the schedule of the upcoming races this season|

*Fun Commands*
|Command|Description|
|-------|-----------|
|`.fact`|Gives you a random fact about Formula 1|
|`.quiz`|Starts an F1-themed quiz|
|`.quiz quit`|Ends an ongoing quiz|
|`.quiz <option>`|To answer a question|






----
> *Note* : The commands which involve webscraping from dynamic websites (i.e `.nextrace` and `.news`), can't fetch the data when the bot is deployed on the server(due to limited free memory provided by heroku). 

> However, these features work perfectly fine when the bot is run locally.
