# gradesBot
a Python Bot to log into and pull academic records from the York University grades site

##Requirements
[Chrome Driver](http://chromedriver.chromium.org/downloads) is required to use selenium.. with chrome at least . Be sure to download correct version for Chrome you have installed
To verify chrome version, enter `chrome://version` in your chrome browser address bar. The first line of the page displays the chrome version
Place the extracted driver file in the root directory of the project

##To Run 
- Change the name of the file named [config_.ini](./config_.ini) to config.ini

- Replace your credentials in the config file for *username* and *password* fields

- Install the dependencies in [requirements.txt](./requirements.txt), with `pip install -r requirements.txt` from the root directory of the project, preferably in a Python 3.7 virtual environment.

- Execute using `python3 gradesBot.py`
