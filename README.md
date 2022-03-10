# Automate python class creation of sObjects in salesforce org

- this program will create a python class for each sObject in your org that you include in the config.py file.
- the results will be saved in the results.py file.
- working on options to create a class for every sObject in your org.
- add a .env file to your project to store your salesforce credentials.

## Usage
install requirements.txt

## create a gitignore file to ingnore the .env file with your secrets before you push code to github

## Create .env file
- in the .env file, add the following:
- USR=<enter userame from org>
- PASSWORD=<enter user's password from org>
- TOKEN=<enter users security token from org>

## Config.py
- there's only one thing to do here right now: enter the sObjets you wish to create classes for.

## to run the program
- to run the program, run the following command:
- `python main.py`

## results.py
- results.py will contain the python classes for each sObject you included in the config.py file.
- they have a default value of `None` so you don't have to enter every value when creating an instance of the object. just use the keyword arguments.